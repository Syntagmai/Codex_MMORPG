---
tags: [integration, network, optimization, compression, otclient, canary]
status: 'in-progress'
aliases:
  - Otimização de Rede
  - Network Optimization
---

# Página "Otimização de Rede"

## 1. Explicação Teórica

Em jogos online, a otimização de rede é crucial para proporcionar uma experiência de jogo fluida e responsiva. O objetivo é minimizar a latência (delay), reduzir o consumo de banda e garantir a integridade dos dados trocados entre o cliente e o servidor. As principais técnicas de otimização incluem a compressão de dados, o gerenciamento inteligente de pacotes e o uso de protocolos eficientes.

---

## 2. Compressão de Rede (Cliente-Servidor)

Tanto o OTClient quanto o Canary implementam a compressão de pacotes de rede para reduzir a quantidade de dados transmitidos. Isso é especialmente útil para jogadores com conexões de internet mais lentas. A biblioteca utilizada para esta finalidade é a **Zlib**.

### Implementação no Servidor (Canary)

O Canary comprime os pacotes de saída que excedem um determinado tamanho. Isso é uma otimização inteligente, pois evita o custo de processamento (CPU) para comprimir pacotes que já são pequenos.

```cpp
// Extraído de canary/src/server/network/protocol/protocol.cpp

bool Protocol::compression(OutputMessage &outputMessage) const {
	if (checksumMethod != CHECKSUM_METHOD_SEQUENCE) {
		return false;
	}

	static thread_local auto compress_ptr = std::make_unique<ZStream>();
	const auto outputMessageSize = outputMessage.getLength();

	if (outputMessageSize > NETWORKMESSAGE_MAXSIZE) {
		g_logger().error("[NetworkMessage::compression] - Exceded NetworkMessage max size: {}, actually size: {}", NETWORKMESSAGE_MAXSIZE, outputMessageSize);
		return false;
	}
    
	// ... (código de compressão com deflate)
    
	const int32_t ret = deflate(compress_ptr->stream.get(), Z_FINISH);
	if (ret != Z_OK && ret != Z_STREAM_END) {
		return false;
	}
    
	// ...
	outputMessage.addBytes(compress_ptr->buffer.data(), totalSize);
	return true;
}
```
**Análise**: A função `compression` no `protocol.cpp` do Canary usa `deflate` da Zlib para comprimir o buffer de uma `OutputMessage`. A compressão só é aplicada se o método de checksum for `CHECKSUM_METHOD_SEQUENCE`, indicando uma camada adicional de lógica de protocolo.

### Implementação no Cliente (OTClient)

O OTClient está preparado para receber pacotes comprimidos do servidor. A lógica de descompressão também utiliza a Zlib.

```cpp
// Extraído de otclient/src/framework/net/protocol.cpp

void Protocol::parseMessage(InputMessage& msg)
{
    // ...
    bool decompress = false;
    if (m_sequencedPackets) {
        decompress = (m_inputMessage->getU32() & 1 << 31);
    }
    // ...

    if (decompress) {
        static uint8_t zbuffer[InputMessage::BUFFER_MAXSIZE];
        m_zstream.next_in = m_inputMessage->getReadBuffer();
        m_zstream.avail_in = m_inputMessage->getUnreadSize();
        m_zstream.next_out = zbuffer;
        m_zstream.avail_out = sizeof(zbuffer);

        int ret = inflate(&m_zstream, Z_SYNC_FLUSH);
        if (ret != Z_OK && ret != Z_STREAM_END) {
            g_logger.traceError("failed to decompress message - {}", m_zstream.msg);
            return;
        }
        // ... (copia os dados descomprimidos para a mensagem)
    }
    // ...
}
```
**Análise**: A função `parseMessage` verifica um bit de flag para determinar se o pacote precisa ser descomprimido (`decompress`). Se verdadeiro, `inflate` da Zlib é usado para descomprimir os dados em um buffer temporário antes de serem processados.

---

## 3. Compressão de Assets no Cliente (OTClient)

Além da otimização de rede, o OTClient emprega técnicas de compressão para reduzir o uso de recursos locais, como espaço em disco e memória de vídeo (VRAM).

### Compressão de Sprites e Minimapa

O cliente utiliza Zlib e LZMA para comprimir os arquivos de assets do jogo. Isso é evidente no carregamento de sprites e do minimapa.

```cpp
// Extraído de otclient/src/client/minimap.cpp

// ...
std::vector<uint8_t> compressBuffer(compressBound(blockSize));
std::vector<uint8_t> decompressBuffer(blockSize);
// ...
const int ret = uncompress(decompressBuffer.data(), &destLen, compressBuffer.data(), len);
// ...
```
**Análise**: Ao carregar os dados do minimapa, o cliente usa `uncompress` para descomprimir os blocos de dados, reduzindo significativamente o tamanho dos arquivos `.map`.

### Compressão de Texturas

Para otimizar o uso de VRAM, o OTClient pode comprimir texturas ao carregá-las na GPU, usando formatos de compressão nativos do OpenGL.

```cpp
// Extraído de otclient/src/framework/graphics/texture.cpp

void Texture::uploadPixels(const ImagePtr& image, const bool buildMipmaps, const bool compress)
{
    // ...
    if (compress)
        internalFormat = GL_COMPRESSED_RGBA;
    // ...
}
```
**Análise**: A flag `compress` permite que o motor gráfico utilize `GL_COMPRESSED_RGBA`, um formato que economiza uma quantidade substancial de memória de vídeo, permitindo que mais texturas sejam carregadas sem sobrecarregar a GPU.

---

## 4. Conclusão e Boas Práticas

A otimização de rede e de assets é uma parte fundamental da arquitetura do OTClient e do Canary.

-   **Rede**: A compressão de pacotes com Zlib é a principal estratégia para economizar banda e melhorar a responsividade.
-   **Assets**: O OTClient vai além, comprimindo arquivos de jogo e texturas para garantir um desempenho suave e um menor impacto nos recursos do sistema do jogador.

Para futuros desenvolvimentos, é essencial manter e expandir essas estratégias, como explorar algoritmos de compressão mais modernos (como Zstd) ou implementar técnicas mais avançadas de gerenciamento de pacotes, como a agregação de pacotes pequenos.
