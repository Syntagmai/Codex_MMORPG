from unicode_aliases import *
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any
import json
import os
import re

#!/usr/bin/env python3
"""
Script para preparar a wiki do OTClient para integração com Canary
Adiciona tags de integração, referências cruzadas e estrutura para ecossistema completo
"""

class CanaryIntegrationPreparer:
    def __init__(self, wiki_dir: str = "wiki"):
        self.wiki_dir = Path(wiki_dir)
        self.docs_dir = self.wiki_dir / "docs"
        self.integration_dir = self.docs_dir / "integration"
        
        # Áreas que precisam de integração com Canary
        self.integration_areas = {
            "protocol": {
                "files": [
                    "Network_System_Guide.md",
                    "Protocol_System_Guide.md"
                ],
                "tags": ["protocol-opencode", "protocol-extendedopen", "canary", "integration"]
            },
            "network": {
                "files": [
                    "Network_System_Guide.md"
                ],
                "tags": ["network-communication", "client-server-interface", "canary", "integration"]
            },
            "game_state": {
                "files": [
                    "Creature_System_Guide.md",
                    "Item_System_Guide.md",
                    "World_System_Guide.md",
                    "Combat_System_Guide.md"
                ],
                "tags": ["game-state-sync", "canary", "integration"]
            }
        }
        
        # Referências para Canary Wiki (placeholders)
        self.canary_references = {
            "protocol": "https://canary-wiki-url/protocol",
            "network": "https://canary-wiki-url/network", 
            "game_logic": "https://canary-wiki-url/game-logic",
            "database": "https://canary-wiki-url/database",
            "world_management": "https://canary-wiki-url/world-management"
        }
    
    def create_integration_structure(self):
        """Cria estrutura de pastas para integração"""
        print("Criando estrutura de integração...")
        
        # Criar pasta de integração
        self.integration_dir.mkdir(exist_ok=True)
        
        # Criar subpastas
        subdirs = ["protocol", "network", "game_state", "testing"]
        for subdir in subdirs:
            (self.integration_dir / subdir).mkdir(exist_ok=True)
        
        print("  Estrutura de integração criada")
    
    def add_integration_tags(self):
        """Adiciona tags de integração aos documentos existentes"""
        print("Adicionando tags de integração...")
        
        for area, config in self.integration_areas.items():
            for file_name in config["files"]:
                file_path = self.docs_dir / file_name
                if file_path.exists():
                    self.add_tags_to_file(file_path, config["tags"])
        
        print("  Tags de integração adicionadas")
    
    def add_tags_to_file(self, file_path: Path, tags: List[str]):
        """Adiciona tags de integração a um arquivo específico"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Verificar se já tem frontmatter
        if content.startswith("---"):
            # Extrair frontmatter existente
            parts = content.split("---", 2)
            if len(parts) >= 3:
                frontmatter = parts[1]
                content_body = parts[2]
                
                # Adicionar tags de integração
                current_tags = re.search(r'tags:\s*\[(.*?)\]', frontmatter)
                if current_tags:
                    existing_tags = [tag.strip() for tag in current_tags.group(1).split(",")]
                    # Adicionar novas tags sem duplicar
                    for tag in tags:
                        if tag not in existing_tags:
                            existing_tags.append(tag)
                    
                    new_tags_str = ", ".join(existing_tags)
                    frontmatter = re.sub(
                        r'tags:\s*\[.*?\]',
                        f'tags: [{new_tags_str}]',
                        frontmatter
                    )
                
                # Adicionar metadados de integração
                if "cross_project: true" not in frontmatter:
                    frontmatter += "\ncross_project: true\nintegration_areas: [protocol, network, game_state]\nrelated_projects: [canary-wiki]\n"
                
                content = f"---{frontmatter}---{content_body}"
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
    
    def add_integration_sections(self):
        """Adiciona seções de integração aos documentos"""
        print("Adicionando seções de integração...")
        
        for area, config in self.integration_areas.items():
            for file_name in config["files"]:
                file_path = self.docs_dir / file_name
                if file_path.exists():
                    self.add_integration_section_to_file(file_path, area)
        
        print("  Seções de integração adicionadas")
    
    def add_integration_section_to_file(self, file_path: Path, area: str):
        """Adiciona seção de integração a um arquivo específico"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Verificar se já tem seção de integração
        if "## 🔗 **Integração com Canary**" in content:
            return
        
        # Criar seção de integração baseada na área
        integration_section = self.create_integration_section(area)
        
        # Adicionar antes da seção de navegação
        if "> [!success] **Navegação**" in content:
            content = content.replace(
                "> [!success] **Navegação**",
                f"{integration_section}\n\n---\n\n> [!success] **Navegação**"
            )
        else:
            content += f"\n\n{integration_section}"
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    def create_integration_section(self, area: str) -> str:
        """Cria seção de integração baseada na área"""
        if area == "protocol":
            return """## 🔗 **Integração com Canary**

### **Lado Cliente (OTClient)**
- Implementação do protocolo OpenCode e ExtendedOpen
- Gerenciamento de conexão e autenticação
- Processamento de mensagens do servidor

### **Lado Servidor (Canary)**
- [Ver implementação do protocolo no Canary Wiki](https://canary-wiki-url/protocol)
- Gerenciamento de sessões e autenticação
- Processamento de mensagens do cliente

### **Protocolo Compartilhado**
- [Especificação OpenCode](https://shared-specs-url/opencode)
- [Extensões ExtendedOpen](https://shared-specs-url/extendedopen)
- [Testes de Integração](https://canary-wiki-url/integration-tests)

> [!info] **Nota de Integração**
> Este sistema implementa o protocolo de comunicação entre OTClient e Canary. 
> Para desenvolvimento, consulte a documentação do Canary para detalhes do lado servidor."""
        
        elif area == "network":
            return """## 🔗 **Integração com Canary**

### **Lado Cliente (OTClient)**
- Conexão TCP assíncrona com o servidor
- Gerenciamento de sessões e reconexão
- Criptografia XTEA e RSA

### **Lado Servidor (Canary)**
- [Ver sistema de rede no Canary Wiki](https://canary-wiki-url/network)
- Aceitação de conexões e gerenciamento de clientes
- Implementação de criptografia

### **Comunicação Compartilhada**
- [Especificação de rede](https://shared-specs-url/network)
- [Protocolo de handshake](https://shared-specs-url/handshake)
- [Testes de conectividade](https://canary-wiki-url/network-tests)

> [!info] **Nota de Integração**
> Este sistema gerencia a comunicação de rede entre cliente e servidor.
> Para debugging, use as ferramentas de rede do Canary."""
        
        elif area == "game_state":
            return """## 🔗 **Integração com Canary**

### **Lado Cliente (OTClient)**
- Renderização e interface do usuário
- Processamento de entrada do jogador
- Sincronização de estado local

### **Lado Servidor (Canary)**
- [Ver lógica de jogo no Canary Wiki](https://canary-wiki-url/game-logic)
- Validação de ações do jogador
- Gerenciamento de estado do mundo

### **Sincronização Compartilhada**
- [Protocolo de sincronização](https://shared-specs-url/sync)
- [Validação de estado](https://shared-specs-url/validation)
- [Testes de sincronização](https://canary-wiki-url/sync-tests)

> [!info] **Nota de Integração**
> Este sistema sincroniza o estado do jogo entre cliente e servidor.
> Para desenvolvimento, consulte a lógica de jogo do Canary."""
        
        return """## 🔗 **Integração com Canary**

### **Lado Cliente (OTClient)**
- Implementação do lado cliente
- APIs e interfaces disponíveis

### **Lado Servidor (Canary)**
- [Ver implementação no Canary Wiki](https://canary-wiki-url)
- Detalhes do lado servidor

### **Interface Compartilhada**
- [Especificação compartilhada](https://shared-specs-url)
- [Testes de integração](https://canary-wiki-url/tests)

> [!info] **Nota de Integração**
> Este sistema se integra com o servidor Canary.
> Para detalhes completos, consulte a documentação do Canary."""
    
    def create_integration_documents(self):
        """Cria documentos específicos de integração"""
        print("Criando documentos de integração...")
        
        # Documento principal de integração
        main_integration = """---
tags: [otclient, canary, integration, protocol, network, game_state]
status: completed
aliases: [Integração Canary, Cross Project Integration, Client Server Integration]
cross_project: true
integration_areas: [protocol, network, game_state]
related_projects: [canary-wiki]
---

# Integração OTClient + Canary

> [!info] **Ecosistema Completo do Jogo MMORPG**
> Este documento descreve a integração entre o OTClient (cliente) e o Canary (servidor), 
> formando um ecossistema completo para desenvolvimento de jogos MMORPG.

## 🎯 **Visão Geral da Integração**

### **Arquitetura do Sistema**
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   OTClient      │    │  Protocol Layer │    │     Canary      │
│   (Cliente)     │◄──►│  (OpenCode +    │◄──►│   (Servidor)    │
│                 │    │   ExtendedOpen) │    │                 │
│ • UI System     │    │ • Message Types │    │ • Game Logic    │
│ • Client Logic  │    │ • Encryption    │    │ • Server Logic  │
│ • Rendering     │    │ • Validation    │    │ • Database      │
│ • Modules       │    │ • Synchronization│   │ • World Mgmt    │
└─────────────────┘    └─────────────────┘    └─────────────────┘
```

## 🔐 **Protocolo de Comunicação**

### **OpenCode (Protocolo Base)**
- **Versões Suportadas**: 7.72 até 14.12
- **Implementação**: OTClient ↔ Canary
- **Funcionalidades**: Comunicação básica cliente-servidor

### **ExtendedOpen (Extensões)**
- **Funcionalidades**: Features avançadas customizadas
- **Implementação**: Módulos OTClient ↔ Scripts Canary
- **Flexibilidade**: Extensível para necessidades específicas

## 🌐 **Sistema de Rede**

### **Conexão e Autenticação**
- **Login Protocol**: Handshake inicial
- **Session Management**: Gerenciamento de sessões
- **Security**: Criptografia XTEA, RSA

### **Comunicação em Tempo Real**
- **Game Protocol**: Dados do jogo
- **Chat System**: Sistema de comunicação
- **World Updates**: Atualizações do mundo

## 🎮 **Sincronização de Estado**

### **Game State**
- **Player Position**: Posição do jogador
- **Inventory**: Inventário e itens
- **Skills**: Habilidades e progressão
- **Combat**: Sistema de combate

### **World State**
- **Map Data**: Dados do mapa
- **Creatures**: Criaturas e NPCs
- **Items**: Itens no mundo
- **Effects**: Efeitos visuais

## 📚 **Documentação Relacionada**

### **OTClient Wiki**
- [[Network_System_Guide]] - Sistema de rede
- [[Protocol_System_Guide]] - Protocolo de comunicação
- [[Creature_System_Guide]] - Sistema de criaturas
- [[Item_System_Guide]] - Sistema de itens

### **Canary Wiki**
- [Protocol Implementation](https://canary-wiki-url/protocol)
- [Game Logic](https://canary-wiki-url/game-logic)
- [Database Management](https://canary-wiki-url/database)
- [World Management](https://canary-wiki-url/world-management)

### **Especificações Compartilhadas**
- [OpenCode Protocol](https://shared-specs-url/opencode)
- [ExtendedOpen Extensions](https://shared-specs-url/extendedopen)
- [Integration Tests](https://canary-wiki-url/integration-tests)

## 🧪 **Testes de Integração**

### **Ferramentas de Teste**
- **Protocol Testing**: Validação de mensagens
- **Network Testing**: Testes de conectividade
- **State Sync Testing**: Validação de sincronização
- **Performance Testing**: Testes de performance

### **Cenários de Teste**
1. **Conexão e Login**: Validação do processo de login
2. **Comunicação Básica**: Troca de mensagens simples
3. **Sincronização de Estado**: Validação de dados do jogo
4. **Recuperação de Erros**: Reconexão e recuperação
5. **Performance**: Latência e throughput

## 🔄 **Desenvolvimento Coordenado**

### **Fluxo de Desenvolvimento**
1. **Especificação**: Definir interface compartilhada
2. **Implementação OTClient**: Desenvolver lado cliente
3. **Implementação Canary**: Desenvolver lado servidor
4. **Testes de Integração**: Validar funcionamento
5. **Documentação**: Atualizar ambas as wikis

### **Boas Práticas**
- **Sempre documentar interfaces** compartilhadas
- **Manter compatibilidade** entre versões
- **Testar integração** antes de releases
- **Atualizar documentação** em ambos os projetos

---

> [!success] **Navegação**
> - [[Network_System_Guide]] - Sistema de rede
> - [[Protocol_System_Guide]] - Protocolo de comunicação
> - [Canary Wiki](https://canary-wiki-url) - Documentação do servidor
> - [Especificações Compartilhadas](https://shared-specs-url) - Protocolos oficiais

"""
        
        with open(self.integration_dir / "OTClient_Canary_Integration.md", 'w', encoding='utf-8') as f:
            f.write(main_integration)
        
        print("  Documento principal de integração criado")
    
    def update_maps_for_integration(self):
        """Atualiza mapas JSON para incluir informações de integração"""
        print("Atualizando mapas para integração...")
        
        # Atualizar tags_index.json
        tags_file = self.wiki_dir / "maps" / "tags_index.json"
        if tags_file.exists():
            with open(tags_file, 'r', encoding='utf-8') as f:
                tags_data = json.load(f)
            
            # Adicionar tags de integração
            integration_tags = [
                "canary", "integration", "protocol-opencode", "protocol-extendedopen",
                "network-communication", "client-server-interface", "game-state-sync"
            ]
            
            for tag in integration_tags:
                if tag not in tags_data["files_by_tag"]:
                    tags_data["files_by_tag"][tag] = []
            
            # Adicionar arquivos de integração às tags
            integration_files = [
                "OTClient_Canary_Integration.md",
                "Network_System_Guide.md",
                "Protocol_System_Guide.md",
                "Creature_System_Guide.md",
                "Item_System_Guide.md"
            ]
            
            for tag in integration_tags:
                for file_name in integration_files:
                    if file_name not in tags_data["files_by_tag"][tag]:
                        tags_data["files_by_tag"][tag].append(file_name)
            
            with open(tags_file, 'w', encoding='utf-8') as f:
                json.dump(tags_data, f, indent=2, ensure_ascii=False)
        
        print("  Mapas atualizados para integração")
    
    def prepare_integration(self):
        """Executa todo o processo de preparação para integração"""
        print("🚀 Preparando wiki para integração com Canary...")
        
        # 1. Criar estrutura de pastas
        self.create_integration_structure()
        
        # 2. Adicionar tags de integração
        self.add_integration_tags()
        
        # 3. Adicionar seções de integração
        self.add_integration_sections()
        
        # 4. Criar documentos de integração
        self.create_integration_documents()
        
        # 5. Atualizar mapas JSON
        self.update_maps_for_integration()
        
        print("✅ Preparação para integração com Canary concluída!")
        print("🎯 Wiki agora está preparada para ecossistema completo do jogo!")

if __name__ == "__main__":
    preparer = CanaryIntegrationPreparer()
    preparer.prepare_integration() 