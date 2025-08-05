#!/usr/bin/env python3
"""
Script para otimização de tokens nos mapas JSON
Converte descrições para inglês (IA) mantendo tags em português (usuário)
"""
import json
import re
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any

class TokenOptimizer:
    def __init__(self, wiki_dir: str = "wiki"):
        self.wiki_dir = Path(wiki_dir)
        self.maps_dir = self.wiki_dir / "maps"
        
        # Mapeamento de traduções para otimização
        self.translations = {
            # Metadados
            "Índice de tags da wiki do OTClient": "OTClient wiki tags index",
            "Mapa completo da wiki do OTClient": "Complete OTClient wiki map",
            "Relacionamentos entre documentos da wiki": "Wiki document relationships",
            "Documentação sobre": "Documentation about",
            "Sistema de": "System of",
            "Interface do Usuário": "User Interface",
            "Sistema Core": "Core System",
            "Sistema de Jogo": "Game System",
            "APIs e Desenvolvimento": "APIs and Development",
            "Guias e Tutoriais": "Guides and Tutorials",
            "Referências": "References",
            "Outros": "Others",
            "Ferramentas de Build": "Build Tools",
            "Geradores": "Generators",
            "APIs e Interfaces": "APIs and Interfaces",
            "Utilitários": "Utilities",
            "Outras Ferramentas": "Other Tools",
            "Imagens": "Images",
            "Sons": "Sounds",
            "Fontes": "Fonts",
            "Localização": "Localization",
            "Partículas": "Particles",
            "Outros Recursos": "Other Resources",
            "Módulos do Cliente": "Client Modules",
            "Módulos de Jogo": "Game Modules",
            "Módulos Core": "Core Modules",
            "Módulos de Interface": "Interface Modules",
            "Outros Módulos": "Other Modules",
            "Estilos de Botões": "Button Styles",
            "Estilos de Janelas": "Window Styles",
            "Estilos de Widgets": "Widget Styles",
            "Estilos de Layout": "Layout Styles",
            "Outros Estilos": "Other Styles",
            "Documentação Original": "Original Documentation",
            "Sistema de Interface": "Interface System",
            "Sistema de Jogo": "Game System",
            "Sistema Central": "Central System",
            "Guias e Tutoriais": "Guides and Tutorials",
            "Referências": "References",
            "Desconhecido": "Unknown",
            "Sem descrição disponível": "No description available",
            "Informações não disponíveis": "Information not available",
            "Sem descrição": "No description",
            "Arquivo": "File",
            "Diretório": "Directory",
            "Diretório com": "Directory with",
            "itens": "items",
            "subdiretórios": "subdirectories",
            "Fonte": "Font",
            "Localização": "Locale",
            "Partícula": "Particle",
            "Imagem": "Image",
            "Formato": "Format",
            "Tipo": "Type",
            "Idioma": "Language",
            "Traduções": "Translations",
            "Partículas": "Particles",
            "Função": "Function",
            "Classe": "Class",
            "Propriedade": "Property",
            "Widget": "Widget",
            "Dependência": "Dependency",
            "Categoria": "Category",
            "Status": "Status",
            "Prioridade": "Priority",
            "Alias": "Alias",
            "Relacionamento": "Relationship",
            "Caminho": "Path",
            "Navegação": "Navigation",
            "Cluster": "Cluster",
            "Grafo": "Graph",
            "Nó": "Node",
            "Aresta": "Edge",
            "Peso": "Weight",
            "Busca": "Search",
            "Índice": "Index",
            "Mapeamento": "Mapping",
            "Estrutura": "Structure",
            "Organização": "Organization",
            "Sistema": "System",
            "Interface": "Interface",
            "Desenvolvimento": "Development",
            "Programação": "Programming",
            "Configuração": "Configuration",
            "Recurso": "Resource",
            "Ferramenta": "Tool",
            "Módulo": "Module",
            "Estilo": "Style",
            "Documento": "Document",
            "Arquivo": "File",
            "Pasta": "Folder",
            "Diretório": "Directory",
            "Conteúdo": "Content",
            "Informação": "Information",
            "Dados": "Data",
            "Metadados": "Metadata",
            "Estatísticas": "Statistics",
            "Métricas": "Metrics",
            "Performance": "Performance",
            "Tempo": "Time",
            "Execução": "Execution",
            "Processamento": "Processing",
            "Análise": "Analysis",
            "Extração": "Extraction",
            "Geração": "Generation",
            "Atualização": "Update",
            "Validação": "Validation",
            "Verificação": "Verification",
            "Contagem": "Count",
            "Total": "Total",
            "Médio": "Average",
            "Mínimo": "Minimum",
            "Máximo": "Maximum",
            "Última": "Last",
            "Modificação": "Modification",
            "Criação": "Creation",
            "Acesso": "Access",
            "Permissão": "Permission",
            "Autorização": "Authorization",
            "Proteção": "Protection",
            "Segurança": "Security",
            "Integridade": "Integrity",
            "Consistência": "Consistency",
            "Confiabilidade": "Reliability",
            "Disponibilidade": "Availability",
            "Manutenibilidade": "Maintainability",
            "Escalabilidade": "Scalability",
            "Flexibilidade": "Flexibility",
            "Compatibilidade": "Compatibility",
            "Interoperabilidade": "Interoperability",
            "Portabilidade": "Portability",
            "Reutilização": "Reuse",
            "Modularidade": "Modularity",
            "Abstração": "Abstraction",
            "Encapsulamento": "Encapsulation",
            "Herança": "Inheritance",
            "Polimorfismo": "Polymorphism",
            "Composição": "Composition",
            "Agregação": "Aggregation",
            "Associação": "Association",
            "Dependência": "Dependency",
            "Acoplamento": "Coupling",
            "Coesão": "Cohesion",
            "Responsabilidade": "Responsibility",
            "Separação": "Separation",
            "Divisão": "Division",
            "Organização": "Organization",
            "Estruturação": "Structuring",
            "Categorização": "Categorization",
            "Classificação": "Classification",
            "Agrupamento": "Grouping",
            "Ordenação": "Sorting",
            "Filtragem": "Filtering",
            "Busca": "Search",
            "Localização": "Location",
            "Navegação": "Navigation",
            "Exploração": "Exploration",
            "Descoberta": "Discovery",
            "Identificação": "Identification",
            "Reconhecimento": "Recognition",
            "Compreensão": "Understanding",
            "Interpretação": "Interpretation",
            "Análise": "Analysis",
            "Processamento": "Processing",
            "Transformação": "Transformation",
            "Conversão": "Conversion",
            "Adaptação": "Adaptation",
            "Otimização": "Optimization",
            "Melhoria": "Improvement",
            "Aprimoramento": "Enhancement",
            "Refinamento": "Refinement",
            "Ajuste": "Adjustment",
            "Configuração": "Configuration",
            "Personalização": "Customization",
            "Especialização": "Specialization",
            "Generalização": "Generalization",
            "Abstração": "Abstraction",
            "Implementação": "Implementation",
            "Execução": "Execution",
            "Processamento": "Processing",
            "Computação": "Computation",
            "Cálculo": "Calculation",
            "Operação": "Operation",
            "Função": "Function",
            "Método": "Method",
            "Procedimento": "Procedure",
            "Algoritmo": "Algorithm",
            "Lógica": "Logic",
            "Regra": "Rule",
            "Condição": "Condition",
            "Decisão": "Decision",
            "Controle": "Control",
            "Fluxo": "Flow",
            "Sequência": "Sequence",
            "Iteração": "Iteration",
            "Repetição": "Repetition",
            "Recursão": "Recursion",
            "Paralelismo": "Parallelism",
            "Concorrência": "Concurrency",
            "Sincronização": "Synchronization",
            "Comunicação": "Communication",
            "Troca": "Exchange",
            "Transferência": "Transfer",
            "Transmissão": "Transmission",
            "Recepção": "Reception",
            "Armazenamento": "Storage",
            "Persistência": "Persistence",
            "Cache": "Cache",
            "Buffer": "Buffer",
            "Memória": "Memory",
            "Disco": "Disk",
            "Arquivo": "File",
            "Diretório": "Directory",
            "Pasta": "Folder",
            "Caminho": "Path",
            "URL": "URL",
            "URI": "URI",
            "Endereço": "Address",
            "Localização": "Location",
            "Posição": "Position",
            "Coordenada": "Coordinate",
            "Dimensão": "Dimension",
            "Tamanho": "Size",
            "Largura": "Width",
            "Altura": "Height",
            "Profundidade": "Depth",
            "Volume": "Volume",
            "Área": "Area",
            "Perímetro": "Perimeter",
            "Distância": "Distance",
            "Velocidade": "Speed",
            "Aceleração": "Acceleration",
            "Tempo": "Time",
            "Duração": "Duration",
            "Intervalo": "Interval",
            "Frequência": "Frequency",
            "Período": "Period",
            "Ciclo": "Cycle",
            "Fase": "Phase",
            "Estado": "State",
            "Condição": "Condition",
            "Situação": "Situation",
            "Contexto": "Context",
            "Ambiente": "Environment",
            "Configuração": "Configuration",
            "Parâmetro": "Parameter",
            "Argumento": "Argument",
            "Valor": "Value",
            "Dado": "Data",
            "Informação": "Information",
            "Conteúdo": "Content",
            "Texto": "Text",
            "String": "String",
            "Número": "Number",
            "Inteiro": "Integer",
            "Decimal": "Decimal",
            "Real": "Real",
            "Booleano": "Boolean",
            "Lógico": "Logical",
            "Verdadeiro": "True",
            "Falso": "False",
            "Nulo": "Null",
            "Indefinido": "Undefined",
            "Vazio": "Empty",
            "Ocupado": "Occupied",
            "Disponível": "Available",
            "Indisponível": "Unavailable",
            "Ativo": "Active",
            "Inativo": "Inactive",
            "Habilitado": "Enabled",
            "Desabilitado": "Disabled",
            "Visível": "Visible",
            "Invisível": "Invisible",
            "Aberto": "Open",
            "Fechado": "Closed",
            "Iniciado": "Started",
            "Parado": "Stopped",
            "Executando": "Running",
            "Pausado": "Paused",
            "Concluído": "Completed",
            "Finalizado": "Finished",
            "Terminado": "Ended",
            "Cancelado": "Cancelled",
            "Interrompido": "Interrupted",
            "Suspenso": "Suspended",
            "Esperando": "Waiting",
            "Processando": "Processing",
            "Carregando": "Loading",
            "Salvando": "Saving",
            "Enviando": "Sending",
            "Recebendo": "Receiving",
            "Transmitindo": "Transmitting",
            "Baixando": "Downloading",
            "Fazendo upload": "Uploading",
            "Sincronizando": "Synchronizing",
            "Atualizando": "Updating",
            "Modificando": "Modifying",
            "Alterando": "Changing",
            "Editando": "Editing",
            "Criando": "Creating",
            "Removendo": "Removing",
            "Deletando": "Deleting",
            "Excluindo": "Excluding",
            "Adicionando": "Adding",
            "Inserindo": "Inserting",
            "Anexando": "Attaching",
            "Separando": "Separating",
            "Dividindo": "Dividing",
            "Combinando": "Combining",
            "Mesclando": "Merging",
            "Unindo": "Joining",
            "Conectando": "Connecting",
            "Desconectando": "Disconnecting",
            "Ligando": "Linking",
            "Desligando": "Unlinking",
            "Associando": "Associating",
            "Dissociando": "Dissociating",
            "Vinculando": "Binding",
            "Desvinculando": "Unbinding",
            "Referenciando": "Referencing",
            "Dereferenciando": "Dereferencing",
            "Apontando": "Pointing",
            "Indicando": "Indicating",
            "Mostrando": "Showing",
            "Exibindo": "Displaying",
            "Apresentando": "Presenting",
            "Demonstrando": "Demonstrating",
            "Ilustrando": "Illustrating",
            "Exemplificando": "Exemplifying",
            "Representando": "Representing",
            "Simbolizando": "Symbolizing",
            "Significando": "Meaning",
            "Denotando": "Denoting",
            "Conotando": "Connoting",
            "Expressando": "Expressing",
            "Comunicando": "Communicating",
            "Transmitindo": "Transmitting",
            "Conveying": "Conveying",
            "Passando": "Passing",
            "Transferindo": "Transferring",
            "Movendo": "Moving",
            "Deslocando": "Displacing",
            "Transportando": "Transporting",
            "Carregando": "Carrying",
            "Levando": "Taking",
            "Trazendo": "Bringing",
            "Enviando": "Sending",
            "Recebendo": "Receiving",
            "Aceitando": "Accepting",
            "Rejeitando": "Rejecting",
            "Aprovando": "Approving",
            "Reprovando": "Disapproving",
            "Validando": "Validating",
            "Verificando": "Verifying",
            "Confirmando": "Confirming",
            "Negando": "Denying",
            "Permitindo": "Allowing",
            "Proibindo": "Prohibiting",
            "Bloqueando": "Blocking",
            "Liberando": "Releasing",
            "Desbloqueando": "Unblocking",
            "Habilitando": "Enabling",
            "Desabilitando": "Disabling",
            "Ativando": "Activating",
            "Desativando": "Deactivating",
            "Ligando": "Turning on",
            "Desligando": "Turning off",
            "Abrindo": "Opening",
            "Fechando": "Closing",
            "Iniciando": "Starting",
            "Parando": "Stopping",
            "Executando": "Running",
            "Pausando": "Pausing",
            "Continuando": "Continuing",
            "Retomando": "Resuming",
            "Reiniciando": "Restarting",
            "Resetando": "Resetting",
            "Limpar": "Clear",
            "Limpar": "Clean",
            "Organizar": "Organize",
            "Ordenar": "Sort",
            "Filtrar": "Filter",
            "Buscar": "Search",
            "Encontrar": "Find",
            "Localizar": "Locate",
            "Identificar": "Identify",
            "Reconhecer": "Recognize",
            "Detectar": "Detect",
            "Descobrir": "Discover",
            "Explorar": "Explore",
            "Investigar": "Investigate",
            "Analisar": "Analyze",
            "Examinar": "Examine",
            "Estudar": "Study",
            "Pesquisar": "Research",
            "Consultar": "Consult",
            "Verificar": "Check",
            "Testar": "Test",
            "Validar": "Validate",
            "Confirmar": "Confirm",
            "Aprovar": "Approve",
            "Rejeitar": "Reject",
            "Aceitar": "Accept",
            "Negar": "Deny",
            "Permitir": "Allow",
            "Proibir": "Prohibit",
            "Bloquear": "Block",
            "Liberar": "Release",
            "Desbloquear": "Unblock",
            "Habilitar": "Enable",
            "Desabilitar": "Disable",
            "Ativar": "Activate",
            "Desativar": "Deactivate",
            "Ligar": "Turn on",
            "Desligar": "Turn off",
            "Abrir": "Open",
            "Fechar": "Close",
            "Iniciar": "Start",
            "Parar": "Stop",
            "Executar": "Run",
            "Pausar": "Pause",
            "Continuar": "Continue",
            "Retomar": "Resume",
            "Reiniciar": "Restart",
            "Resetar": "Reset"
        }
    
    def translate_text(self, text: str) -> str:
        """Traduz texto para inglês para otimizar tokens"""
        if not text:
            return text
        
        # Aplicar traduções conhecidas
        for pt, en in self.translations.items():
            text = text.replace(pt, en)
        
        return text
    
    def optimize_metadata(self, metadata: Dict[str, Any]) -> Dict[str, Any]:
        """Otimiza metadados convertendo para inglês"""
        optimized = metadata.copy()
        
        # Traduzir descrição
        if "description" in optimized:
            optimized["description"] = self.translate_text(optimized["description"])
        
        return optimized
    
    def optimize_tags_index(self, tags_data: Dict[str, Any]) -> Dict[str, Any]:
        """Otimiza tags_index.json"""
        optimized = tags_data.copy()
        
        # Otimizar metadados
        optimized["metadata"] = self.optimize_metadata(optimized["metadata"])
        
        # Manter tags em português (para usuário)
        # Manter files_by_tag em inglês (para IA)
        
        return optimized
    
    def optimize_wiki_map(self, wiki_data: Dict[str, Any]) -> Dict[str, Any]:
        """Otimiza wiki_map.json"""
        optimized = wiki_data.copy()
        
        # Otimizar metadados
        optimized["metadata"] = self.optimize_metadata(optimized["metadata"])
        
        # Otimizar categorias
        for category, cat_data in optimized["categories"].items():
            if "name" in cat_data:
                cat_data["name"] = self.translate_text(cat_data["name"])
            
            # Otimizar arquivos
            for file_info in cat_data.get("files", []):
                if "description" in file_info:
                    file_info["description"] = self.translate_text(file_info["description"])
                
                # Manter tags em português (para usuário)
                # Manter aliases em português (para usuário)
        
        return optimized
    
    def optimize_relationships(self, rel_data: Dict[str, Any]) -> Dict[str, Any]:
        """Otimiza relationships.json"""
        optimized = rel_data.copy()
        
        # Otimizar metadados
        optimized["metadata"] = self.optimize_metadata(optimized["metadata"])
        
        return optimized
    
    def optimize_all_maps(self):
        """Otimiza todos os mapas JSON"""
        print("Otimizando mapas JSON para redução de tokens...")
        
        # Otimizar tags_index.json
        tags_path = self.maps_dir / "tags_index.json"
        if tags_path.exists():
            print("Otimizando tags_index.json...")
            with open(tags_path, 'r', encoding='utf-8') as f:
                tags_data = json.load(f)
            
            optimized_tags = self.optimize_tags_index(tags_data)
            
            with open(tags_path, 'w', encoding='utf-8') as f:
                json.dump(optimized_tags, f, indent=2, ensure_ascii=False)
        
        # Otimizar wiki_map.json
        wiki_path = self.maps_dir / "wiki_map.json"
        if wiki_path.exists():
            print("Otimizando wiki_map.json...")
            with open(wiki_path, 'r', encoding='utf-8') as f:
                wiki_data = json.load(f)
            
            optimized_wiki = self.optimize_wiki_map(wiki_data)
            
            with open(wiki_path, 'w', encoding='utf-8') as f:
                json.dump(optimized_wiki, f, indent=2, ensure_ascii=False)
        
        # Otimizar relationships.json
        rel_path = self.maps_dir / "relationships.json"
        if rel_path.exists():
            print("Otimizando relationships.json...")
            with open(rel_path, 'r', encoding='utf-8') as f:
                rel_data = json.load(f)
            
            optimized_rel = self.optimize_relationships(rel_data)
            
            with open(rel_path, 'w', encoding='utf-8') as f:
                json.dump(optimized_rel, f, indent=2, ensure_ascii=False)
        
        print("Otimização concluída!")

def main():
    """Função principal"""
    optimizer = TokenOptimizer("wiki")
    optimizer.optimize_all_maps()

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
- [[../update/create_automatic_link_templates.py|create_automatic_link_templates.py]]
- [[../update/orphan_files_analyzer.py|orphan_files_analyzer.py]]
- [[../update/update_json_maps.py|update_json_maps.py]]

### **📈 Métricas do Script**
- **Nome**: optimize_maps_for_tokens
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

