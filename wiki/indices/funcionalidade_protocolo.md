# 📡 Índice de Funcionalidade: Protocolo de Comunicação

Este índice é o guia central para entender a **comunicação entre o cliente (OTClient) e o servidor (Canary)**, detalhando os protocolos, a estrutura de pacotes e a segurança.

---

## 📚 Conceitos Fundamentais
- **[Protocolo de Comunicação](<../integracao_protocolo_comunicacao.md>)**: O documento principal que detalha a arquitetura de comunicação, incluindo OpenCode, ExtendedOpen, criptografia e compressão.
- **[Sistema de Rede (Canary)](<../canary_sistema_rede.md>)**: Como o servidor gerencia as conexões e o fluxo de dados.
- **[Sistema de Rede (OTClient)](<../otclient_sistema_rede.md>)**: Como o cliente gerencia sua comunicação com o servidor.
- **[Sistema de Rede Avançado (OTClient)](<../otclient_sistema_rede_avancado.md>)**: Tópicos avançados, como a implementação de protocolos customizados.

## 🛠️ Como Criar e Modificar
- **[Como Modificar o Protocolo de Rede](<./como_modificar.md#canary-servidor>)**: Guia sobre como customizar a comunicação.
- **[Como Adicionar Suporte a Novos Protocolos](<./como_adicionar.md#otclient-cliente>)**: Para estender a comunicação do cliente.

## 📜 Exemplos de Código
- **`canary/src/network/`**: Código-fonte C++ do sistema de rede do servidor.
- **`otclient/src/framework/net/`**: Código-fonte C++ do sistema de rede do cliente.
- **`canary/src/lua/modules/`**: Módulos Lua no servidor que interceptam pacotes de rede (recvbyte).

## 🔗 Tópicos Relacionados
- **[Segurança](<../INTEGRATION-009_Security.md>)**: Detalhes sobre a criptografia e outras medidas de segurança no protocolo.
- **[Otimização de Rede](<../INTEGRATION-008_Network_Optimization.md>)**: Técnicas para melhorar a performance da comunicação.
- **[Sincronização de Dados](<../integracao_sincronizacao_dados.md>)**: Como o estado do jogo é sincronizado entre cliente e servidor.
