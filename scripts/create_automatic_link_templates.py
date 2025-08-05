#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Links Automáticos - Task 20.4
Cria templates de links base para cada categoria da wiki
"""

import json
import os
from datetime import datetime
from pathlib import Path

class AutomaticLinkTemplateGenerator:
    def __init__(self):
        self.wiki_path = Path("wiki")
        self.maps_path = self.wiki_path / "maps"
        self.templates_path = self.wiki_path / "templates"
        self.templates_path.mkdir(exist_ok=True)
        
    def load_category_hierarchy(self):
        """Carrega a hierarquia de categorias"""
        hierarchy_file = self.maps_path / "category_hierarchy.json"
        with open(hierarchy_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    
    def create_category_template(self, category_name, category_data):
        """Cria template de links para uma categoria específica"""
        template_content = f"""---
tags: [template, {category_name.lower()}, automatic_links, wiki_navigation]
type: template
category: {category_name}
status: active
created: {datetime.now().strftime('%Y-%m-%d')}
---

# 📋 **Template de Links - {category_name}**

> [!info] **Template Automático**
> Este arquivo é um template para links automáticos da categoria **{category_name}**
> 
> **Descrição**: {category_data.get('description', 'Categoria da wiki')}

## 🎯 **Links Principais**

### **📚 Documentação Base**
- [[../README|Hub Central da Wiki]]
- [[../dashboard/task_master|Task Master]]
- [[../dashboard/integrated_task_manager|Dashboard Central]]

### **🔗 Links da Categoria {category_name}**

"""
        
        # Adicionar subcategorias se existirem
        if 'subcategories' in category_data:
            template_content += "### **📂 Subcategorias**\n\n"
            for subcat, description in category_data['subcategories'].items():
                template_content += f"- **{subcat}**: {description}\n"
            template_content += "\n"
        
        template_content += f"""### **📄 Arquivos da Categoria**
<!-- Lista automática de arquivos será inserida aqui -->

### **🔍 Busca e Navegação**
- [[../maps/search_index|Índice de Busca]]
- [[../maps/tags_index|Índice de Tags]]
- [[../maps/category_indices|Índices por Categoria]]

### **📊 Métricas**
- **Total de arquivos**: <!-- Contador automático -->
- **Arquivos linkados**: <!-- Contador automático -->
- **Taxa de linkagem**: <!-- Percentual automático -->

---

## 🔧 **Configuração Automática**

### **📋 Regras de Linkagem**
1. **Links obrigatórios**: Hub Central, Task Master, Dashboard
2. **Links de categoria**: Todos os arquivos da categoria
3. **Links de navegação**: Índices e mapas
4. **Links de métricas**: Estatísticas atualizadas

### **🔄 Atualização Automática**
- **Frequência**: A cada novo arquivo criado
- **Trigger**: Criação de arquivo na categoria
- **Ação**: Atualização automática do template

---

> [!tip] **Uso do Template**
> Este template é usado automaticamente pelo sistema de linkagem
> para garantir que todos os arquivos da categoria {category_name}
> sejam devidamente linkados e navegáveis.

"""
        
        return template_content
    
    def create_link_rules_template(self):
        """Cria template de regras de linkagem"""
        rules_content = f"""---
tags: [template, link_rules, automatic_system, wiki_navigation]
type: template
status: active
created: {datetime.now().strftime('%Y-%m-%d')}
---

# 🔗 **Regras de Linkagem Automática**

> [!info] **Sistema Automático**
> Este arquivo define as regras para linkagem automática de arquivos na wiki

## 📋 **Regras por Categoria**

### **🎯 Core**
- **Links obrigatórios**: README, Task Master, Dashboard
- **Links específicos**: Módulos, Configuração, Rede
- **Prioridade**: Alta

### **🎮 Game_Systems**
- **Links obrigatórios**: README, Task Master, Dashboard
- **Links específicos**: Combate, Itens, Criaturas, Mundo
- **Prioridade**: Alta

### **🖥️ UI_Systems**
- **Links obrigatórios**: README, Task Master, Dashboard
- **Links específicos**: OTUI, Animações, Gráficos
- **Prioridade**: Média

### **💻 Development**
- **Links obrigatórios**: README, Task Master, Dashboard
- **Links específicos**: API, Exemplos, Melhores Práticas
- **Prioridade**: Alta

### **🤖 BMAD_System**
- **Links obrigatórios**: README, Task Master, Dashboard
- **Links específicos**: Agentes, Workflows, Automação
- **Prioridade**: Média

### **📋 Task_Management**
- **Links obrigatórios**: README, Task Master, Dashboard
- **Links específicos**: Epics, Relatórios, Arquivos
- **Prioridade**: Alta

### **🔗 Integration**
- **Links obrigatórios**: README, Task Master, Dashboard
- **Links específicos**: Arquitetura, Protocolos, Migração
- **Prioridade**: Média

### **🔬 Research**
- **Links obrigatórios**: README, Task Master, Dashboard
- **Links específicos**: Pesquisa Canary, Pesquisa OTClient
- **Prioridade**: Baixa

### **📚 Documentation**
- **Links obrigatórios**: README, Task Master, Dashboard
- **Links específicos**: Guias, Referências, FAQ
- **Prioridade**: Média

### **🔧 Tools**
- **Links obrigatórios**: README, Task Master, Dashboard
- **Links específicos**: Análise, Validação, Relatórios
- **Prioridade**: Baixa

### **📜 Legacy**
- **Links obrigatórios**: README, Task Master, Dashboard
- **Links específicos**: Documentação antiga, Arquivos
- **Prioridade**: Baixa

## 🔄 **Processo Automático**

### **1. Detecção de Novo Arquivo**
- Monitorar criação de arquivos na wiki
- Identificar categoria automaticamente
- Aplicar regras de linkagem

### **2. Criação de Links**
- Gerar links obrigatórios
- Adicionar links específicos da categoria
- Incluir links de navegação

### **3. Validação**
- Verificar se links funcionam
- Validar estrutura de navegação
- Atualizar métricas

### **4. Notificação**
- Alertar sobre arquivos órfãos
- Reportar problemas de linkagem
- Sugerir melhorias

---

> [!warning] **Importante**
> Estas regras são aplicadas automaticamente pelo sistema.
> Modificações devem ser feitas com cuidado para manter consistência.

"""
        
        return rules_content
    
    def create_validation_template(self):
        """Cria template de validação de links"""
        validation_content = f"""---
tags: [template, validation, link_checking, automatic_system]
type: template
status: active
created: {datetime.now().strftime('%Y-%m-%d')}
---

# ✅ **Validação de Links Automática**

> [!info] **Sistema de Validação**
> Este arquivo define o processo de validação automática de links

## 🔍 **Critérios de Validação**

### **✅ Links Válidos**
- Arquivo de destino existe
- Caminho correto
- Formato markdown válido
- Sem caracteres especiais problemáticos

### **❌ Links Inválidos**
- Arquivo não encontrado
- Caminho incorreto
- Formato inválido
- Caracteres especiais não escapados

### **⚠️ Links Suspeitos**
- Arquivo existe mas pode estar obsoleto
- Caminho funciona mas não é ideal
- Formato funciona mas pode ser melhorado

## 🔄 **Processo de Validação**

### **1. Verificação de Existência**
```python
def check_file_exists(file_path):
    return Path(file_path).exists()
```

### **2. Validação de Formato**
```python
def validate_markdown_link(link):
    # Verificar formato [[arquivo|texto]]
    pattern = r'\\[\\[([^\\]]+)\\]\\]'
    return bool(re.match(pattern, link))
```

### **3. Verificação de Caminho**
```python
def validate_path(file_path):
    # Verificar se caminho é válido
    try:
        Path(file_path).resolve()
        return True
    except:
        return False
```

## 📊 **Métricas de Validação**

### **📈 Estatísticas**
- **Total de links**: <!-- Contador automático -->
- **Links válidos**: <!-- Contador automático -->
- **Links inválidos**: <!-- Contador automático -->
- **Taxa de sucesso**: <!-- Percentual automático -->

### **📋 Relatórios**
- **Links quebrados**: Lista de links inválidos
- **Links suspeitos**: Lista de links que precisam atenção
- **Sugestões**: Melhorias recomendadas

---

> [!tip] **Validação Automática**
> O sistema executa validação automática a cada:
> - Criação de novo arquivo
> - Modificação de arquivo existente
> - Execução manual do script de validação

"""
        
        return validation_content
    
    def create_notification_template(self):
        """Cria template de notificação de arquivos órfãos"""
        notification_content = f"""---
tags: [template, notification, orphan_files, automatic_system]
type: template
status: active
created: {datetime.now().strftime('%Y-%m-%d')}
---

# 🔔 **Sistema de Notificação de Arquivos Órfãos**

> [!info] **Notificações Automáticas**
> Este arquivo define o sistema de notificação para arquivos órfãos

## 📋 **Tipos de Notificação**

### **🚨 Arquivos Órfãos Críticos**
- **Critério**: Arquivos importantes sem links
- **Ação**: Notificação imediata
- **Prioridade**: Alta

### **⚠️ Arquivos Órfãos Médios**
- **Critério**: Arquivos com importância média
- **Ação**: Notificação diária
- **Prioridade**: Média

### **ℹ️ Arquivos Órfãos Baixos**
- **Critério**: Arquivos de baixa importância
- **Ação**: Notificação semanal
- **Prioridade**: Baixa

## 🔄 **Processo de Notificação**

### **1. Detecção**
```python
def detect_orphan_files():
    # Analisar todos os arquivos da wiki
    # Identificar arquivos sem links
    # Categorizar por importância
    pass
```

### **2. Categorização**
```python
def categorize_orphan_files(files):
    # Definir critérios de importância
    # Categorizar arquivos
    # Priorizar notificações
    pass
```

### **3. Notificação**
```python
def send_notification(orphan_files):
    # Gerar relatório
    # Enviar notificação
    # Registrar ação
    pass
```

## 📊 **Métricas de Notificação**

### **📈 Estatísticas**
- **Total de arquivos órfãos**: <!-- Contador automático -->
- **Arquivos críticos**: <!-- Contador automático -->
- **Arquivos médios**: <!-- Contador automático -->
- **Arquivos baixos**: <!-- Contador automático -->

### **📋 Relatórios**
- **Relatório diário**: Arquivos órfãos do dia
- **Relatório semanal**: Resumo semanal
- **Relatório mensal**: Análise completa

---

> [!warning] **Notificações Automáticas**
> O sistema envia notificações automaticamente baseado na:
> - Importância do arquivo
> - Frequência de acesso
> - Tempo desde a criação

"""
        
        return notification_content
    
    def generate_all_templates(self):
        """Gera todos os templates de links automáticos"""
        print("🔄 Iniciando geração de templates de links automáticos...")
        
        # Carregar hierarquia de categorias
        hierarchy = self.load_category_hierarchy()
        
        # Criar templates para cada categoria
        templates_created = []
        
        for category_name, category_data in hierarchy.items():
            print(f"📋 Criando template para categoria: {category_name}")
            
            # Criar template da categoria
            template_content = self.create_category_template(category_name, category_data)
            template_file = self.templates_path / f"template_{category_name.lower()}.md"
            
            with open(template_file, 'w', encoding='utf-8') as f:
                f.write(template_content)
            
            templates_created.append(template_file.name)
        
        # Criar template de regras
        print("📋 Criando template de regras de linkagem...")
        rules_content = self.create_link_rules_template()
        rules_file = self.templates_path / "template_link_rules.md"
        
        with open(rules_file, 'w', encoding='utf-8') as f:
            f.write(rules_content)
        
        templates_created.append(rules_file.name)
        
        # Criar template de validação
        print("📋 Criando template de validação...")
        validation_content = self.create_validation_template()
        validation_file = self.templates_path / "template_validation.md"
        
        with open(validation_file, 'w', encoding='utf-8') as f:
            f.write(validation_content)
        
        templates_created.append(validation_file.name)
        
        # Criar template de notificação
        print("📋 Criando template de notificação...")
        notification_content = self.create_notification_template()
        notification_file = self.templates_path / "template_notification.md"
        
        with open(notification_file, 'w', encoding='utf-8') as f:
            f.write(notification_content)
        
        templates_created.append(notification_file.name)
        
        # Gerar relatório
        report = {
            "timestamp": datetime.now().isoformat(),
            "templates_created": len(templates_created),
            "templates": templates_created,
            "categories_processed": len(hierarchy),
            "status": "success"
        }
        
        report_file = self.maps_path / "automatic_link_templates_report.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Templates criados com sucesso: {len(templates_created)}")
        print(f"📊 Relatório salvo em: {report_file}")
        
        return report

def main():
    """Função principal"""
    generator = AutomaticLinkTemplateGenerator()
    report = generator.generate_all_templates()
    
    print("\n🎯 **Task 20.4 - Sub-tarefa 1 Concluída**")
    print("✅ Templates de links base criados para todas as categorias")
    print("📋 Próximo passo: Implementar script de linkagem automática")

if __name__ == "__main__":
    main() 
## 🔗 **Links Automáticos - Scripts**

> [!info] **Script de Automação**
> Este script faz parte do sistema de automação da wiki

### **📚 Links Obrigatórios**
- [[../README|Hub Central da Wiki]]
- [[../dashboard/task_master|Task Master]]
- [[../dashboard/integrated_task_manager|Dashboard Central]]

### **🔧 Links de Scripts**
- [[../update/README|Documentação de Scripts]]
- [[../maps/scripts_index|Índice de Scripts]]
- [[../templates/README|Templates de Scripts]]

### **📊 Scripts Relacionados**
- [[../update/automatic_linkage_system.py|automatic_linkage_system.py]]
- [[../update/orphan_files_analyzer.py|orphan_files_analyzer.py]]
- [[../update/update_json_maps.py|update_json_maps.py]]

### **📈 Métricas do Script**
- **Nome**: create_automatic_link_templates
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

