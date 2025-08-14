---
tags: [integration, monitoring, logging, metrics, otclient, canary]
status: 'in-progress'
aliases:
  - Monitoramento
  - Logging
---

# Página "Monitoramento"

## 1. Explicação Teórica

Monitoramento é o processo de coletar, analisar e usar informações para rastrear o desempenho e a saúde de um sistema de software. Em um ambiente cliente-servidor como o de um MMORPG, o monitoramento é vital para:

-   **Detectar Problemas**: Identificar erros, gargalos de performance e comportamento inesperado em tempo real.
-   **Depuração (Debugging)**: Fornecer logs detalhados que ajudam os desenvolvedores a diagnosticar e corrigir bugs.
-   **Análise de Performance**: Coletar métricas sobre o uso de CPU, memória e rede para otimizar o sistema.
-   **Segurança**: Registrar eventos de segurança importantes para detectar atividades suspeitas.

A principal ferramenta para monitoramento tanto no OTClient quanto no Canary é o **logging**.

---

## 2. Monitoramento no Servidor (Canary)

O Canary utiliza uma abordagem de monitoramento moderna e poderosa, baseada na biblioteca de logging **`spdlog`**. Isso fornece uma base flexível e de alta performance para registrar eventos do servidor.

### a) Implementação com `spdlog`

A biblioteca `spdlog` é integrada através do arquivo `canary/src/lib/logging/log_with_spd_log.hpp`. Ela permite logs assíncronos, formatação customizável e múltiplos "sinks" (saídas), como console, arquivos de log e outros.

```cpp
// Extraído de canary/src/lib/logging/logger.cpp

// Exemplo de como uma mensagem de erro é logada no Canary
// A macro SPDLOG_ERROR é fornecida pela biblioteca spdlog.
SPDLOG_ERROR("Failed to do something: {}", error_message);
```
**Análise**: O uso de `spdlog` permite que o Canary registre mensagens detalhadas com baixo impacto na performance do servidor, o que é crucial para uma aplicação que precisa lidar com milhares de conexões simultâneas.

### b) Sistema de Métricas

O Canary também possui um sistema de métricas dedicado (`canary/src/lib/metrics/metrics.cpp`). Embora os detalhes da implementação não sejam o foco, sua existência indica uma estratégia de monitoramento mais avançada, que vai além de simples logs. Provavelmente, ele coleta dados quantitativos sobre a performance do servidor, como:

-   Número de jogadores online.
-   Tempo de resposta de queries ao banco de dados.
-   Uso de CPU por diferentes subsistemas.

### c) Acesso via Lua

Os scripts Lua no Canary também podem interagir com o sistema de log, permitindo que a lógica de jogo customizada também reporte seus próprios eventos e erros.

---

## 3. Monitoramento no Cliente (OTClient)

O OTClient utiliza um sistema de logging customizado, definido em `otclient/src/framework/core/logger.h`. É uma solução mais simples que o `spdlog`, mas perfeitamente adequada para as necessidades de uma aplicação cliente.

### a) Logger Customizado

O logger do OTClient suporta diferentes níveis de severidade, permitindo filtrar as mensagens por importância.

-   `g_logger.info(...)`
-   `g_logger.warning(...)`
-   `g__logger.error(...)`
-   `g_logger.fatal(...)`

```cpp
// Extraído de otclient/src/framework/core/logger.cpp

void Logger::log(LogLevel level, const std::string& message)
{
    if (level < m_logLevel)
        return;

    std::string levelStr;
    // ... (determina a string do nível: "INFO", "ERROR", etc.)

    // Formata a mensagem com timestamp e nível
    std::string formattedMessage = stdext::format("%s [%s]: %s",
                                                  stdext::timestamp(),
                                                  levelStr,
                                                  message);
    
    // Escreve no arquivo de log e no console
    if (m_outFile.is_open())
        m_outFile << formattedMessage << std::endl;
    std::cout << formattedMessage << std::endl;
}
```
**Análise**: O logger formata cada mensagem com um timestamp e o nível de severidade antes de enviá-la para o console e para um arquivo de log (`otclient.log`, por exemplo).

### Exemplo Prático de Logging de Erro (OTClient)

Quando o cliente falha ao carregar uma textura, ele usa o logger para registrar o erro, o que é imensamente útil para desenvolvedores e modders.

```cpp
// Extraído de otclient/src/framework/graphics/texturemanager.cpp

// ...
try {
    ImagePtr image = Image::load(realPath);
    texture->upload(image);
} catch (const stdext::exception& e) {
    g_logger.error(stdext::format("failed to load texture '%s': %s", fileName, e.what()));
}
// ...
```
**Análise**: Em vez de travar, o cliente registra um erro claro e continua a execução. O log resultante ajuda a identificar rapidamente qual arquivo de imagem está causando o problema.

---

## 4. Conclusão e Boas Práticas

-   **Canary** adota uma abordagem de nível de servidor com uma biblioteca de alta performance (`spdlog`) e um sistema de métricas dedicado, focando na estabilidade e na análise de performance em larga escala.
-   **OTClient** usa uma solução de logging customizada e eficaz para o contexto de uma aplicação desktop, focando na depuração de erros de assets e lógica do cliente.

Para o sistema integrado, a melhor prática é garantir que os logs de ambos, cliente e servidor, sejam correlacionados quando possível (por exemplo, usando um ID de sessão único). Isso permitiria rastrear uma única ação do jogador desde a interface gráfica do OTClient até a sua execução e resposta no Canary, simplificando enormemente a depuração de problemas complexos.
