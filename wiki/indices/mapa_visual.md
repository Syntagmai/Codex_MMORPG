# 🗺️ Mapa Visual do Conhecimento

Este mapa visual oferece uma visão geral da estrutura da nossa wiki, mostrando como os principais tópicos se conectam. Use-o para navegar e entender as relações entre **Canary**, **OTClient** e os conceitos de **Integração**.

```mermaid
graph TD
    subgraph Wiki
        A["<a href='../wikipedia_canary_otclient.md'>Wikipedia Principal</a>"]
    end

    subgraph "Navegação Principal"
        B("<a href='./niveis/iniciante.md'>Níveis de Dificuldade</a>")
        C("<a href='./como_criar.md'>Índices Temáticos</a>")
        D("<a href='./funcionalidade_monstros.md'>Índices por Funcionalidade</a>")
    end

    subgraph "Canary - Servidor"
        E["<a href='../canary_arquitetura_core.md'>Arquitetura Core</a>"]
        F["<a href='../canary_sistema_scripting.md'>Sistema de Scripting (Lua)</a>"]
        G["<a href='../canary_sistema_combate.md'>Sistema de Combate</a>"]
        H["<a href='../canary_sistema_monstros.md'>Sistema de Monstros</a>"]
        I["<a href='../canary_sistema_magias.md'>Sistema de Magias</a>"]
    end

    subgraph "OTClient - Cliente"
        J["<a href='../otclient_arquitetura_core.md'>Arquitetura Core</a>"]
        K["<a href='../otclient_sistema_ui.md'>Sistema de UI (OTUI)</a>"]
        L["<a href='../otclient_sistema_modulos.md'>Sistema de Módulos</a>"]
        M["<a href='../otclient_sistema_graficos.md'>Sistema de Gráficos</a>"]
        N["<a href='../otclient_sistema_rede.md'>Sistema de Rede</a>"]
    end

    subgraph "Integração"
        O["<a href='../integracao_protocolo_comunicacao.md'>Protocolo de Comunicação</a>"]
        P["<a href='../integracao_sincronizacao_dados.md'>Sincronização de Dados</a>"]
        Q["<a href='../INTEGRATION-009_Security.md'>Segurança</a>"]
    end

    A --> B
    A --> C
    A --> D
    
    A --o "Tópicos Principais"
    
    subgraph Tópicos
        direction LR
        A --> E
        A --> J
        A --> O
    end
    
    E --> F & G & H & I
    J --> K & L & M & N
    O --> P & Q
    
    E -.-> O
    J -.-> O
```
