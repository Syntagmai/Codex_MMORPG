---
tags: [integration, security, encryption, otclient, canary]
status: 'in-progress'
aliases:
  - Segurança
  - Security Measures
---

# Página "Segurança"

## 1. Explicação Teórica

A segurança em jogos online é uma faceta multidimensional que visa proteger tanto os jogadores quanto a integridade do servidor. As medidas de segurança são essenciais para prevenir trapaças (cheating), proteger dados sensíveis dos usuários (como senhas) e garantir que a comunicação entre o cliente e o servidor não possa ser interceptada ou manipulada.

---

## 2. Segurança no Servidor (Canary)

O Canary implementa medidas de segurança robustas para proteger os dados em seus domínios de responsabilidade: o banco de dados e a comunicação inicial.

### a) Hashing de Senhas com Argon2

Para proteger as credenciais dos usuários, o Canary utiliza **Argon2**, um algoritmo de hashing de senha de última geração, vencedor da Password Hashing Competition.

```cpp
// Extraído de canary/src/security/argon.cpp

bool Argon::hash(const std::string& password, std::string& hash)
{
    // ...
    int rc = argon2i_hash_encoded(t_cost, m_cost, parallelism,
                                  password.c_str(), password.length(),
                                  salt, sizeof(salt),
                                  hash.data(), hash.length(),
                                  Argon2_i, ARGON2_VERSION_NUMBER);
    // ...
}
```
**Análise**: Em vez de armazenar senhas em texto plano, o Canary armazena um *hash* seguro gerado pelo Argon2. Isso significa que, mesmo que o banco de dados seja comprometido, as senhas dos usuários não podem ser recuperadas diretamente.

### b) Troca de Chaves com RSA

Para iniciar uma comunicação segura, o Canary utiliza o algoritmo de criptografia assimétrica **RSA**. Durante o processo de login, o RSA é usado para criptografar a chave de sessão (geralmente uma chave simétrica como XTEA), que será usada para o resto da comunicação.

```cpp
// Extraído de canary/src/security/rsa.hpp

class RSA
{
public:
    // ...
    bool encrypt(const std::string& message, std::string& encrypted_message);
    bool decrypt(const std::string& encrypted_message, std::string& decrypted_message);
    // ...
};
```
**Análise**: O uso de RSA garante que apenas o servidor possa descriptografar as informações iniciais enviadas pelo cliente, tornando o *handshake* inicial seguro.

---

## 3. Segurança no Cliente (OTClient)

O OTClient implementa a outra metade do esquema de segurança, garantindo que a comunicação seja criptografada e íntegra.

### a) Criptografia da Comunicação com XTEA

Após o handshake de login com RSA, o tráfego principal do jogo é criptografado usando **XTEA**, um cifrador de bloco simétrico rápido e eficiente, ideal para o grande volume de pacotes de um MMORPG.

```cpp
// Extraído de otclient/src/framework/net/protocol.cpp

bool Protocol::xteaEncrypt(OutputMessage_ptr outputMessage)
{
    // ... (lógica de padding)
    
    // Criptografa o buffer usando a chave XTEA
    for (uint32_t i = 0, sum = 0, next_sum = sum + delta; i < 32; ++i, sum = next_sum, next_sum += delta) {
        apply_rounds(outputMessage->getXteaEncryptionBuffer(), encryptedSize, [&, sum, next_sum, this](uint32_t& left, uint32_t& right) mutable {
            left += ((right << 4 ^ right >> 5) + right) ^ (sum + m_xteaKey[sum & 3]);
            right += ((left << 4 ^ left >> 5) + left) ^ (next_sum + m_xteaKey[(next_sum >> 11) & 3]);
        });
    }
    return true;
}
```
**Análise**: Antes de enviar um pacote, o cliente o criptografa com a chave XTEA previamente negociada. Isso impede que intermediários na rede (como provedores de internet) possam ler o conteúdo dos pacotes do jogo.

### b) Verificação de Integridade com Checksum

Para garantir que os pacotes não sejam corrompidos (acidentalmente ou maliciosamente) durante a transmissão, cada pacote inclui um *checksum* (soma de verificação).

```cpp
// Extraído de otclient/src/framework/net/protocol.cpp

void Protocol::parseMessage(InputMessage& msg)
{
    // ...
    if (m_checksumEnabled && !m_inputMessage->readChecksum()) {
        g_logger.traceError("got a network message with invalid checksum...");
        return;
    }
    // ...
}
```
**Análise**: Ao receber um pacote, o cliente primeiro calcula seu checksum e o compara com o checksum enviado. Se eles não corresponderem, o pacote é descartado, prevenindo erros causados por dados corrompidos.

---

## 4. Fluxo de Comunicação Segura (Resumo)

1.  **Login**: O cliente solicita a chave pública RSA do servidor.
2.  **Troca de Chave**: O cliente gera uma chave simétrica (XTEA), a criptografa com a chave RSA do servidor e a envia.
3.  **Estabelecimento do Canal Seguro**: Apenas o servidor pode descriptografar a chave XTEA. A partir deste ponto, toda a comunicação do jogo é criptografada com esta chave simétrica.
4.  **Comunicação Contínua**: Cada pacote enviado é criptografado com XTEA e assinado com um checksum. Cada pacote recebido é verificado pelo checksum e depois descriptografado.
5.  **Armazenamento de Senha**: No servidor, a senha do usuário é validada usando o hash Argon2.

Este fluxo combinado oferece uma segurança robusta em múltiplas camadas.
