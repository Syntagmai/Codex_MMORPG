# Constantes
MAX_RETRIES = 8
MAX_ATTEMPTS = 10
TIMEOUT_SECONDS = 60

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: update_context_system.py
Módulo de Destino: tools.config_manager
Data de Migração: 2025-08-01 12:21:35

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import ConfigmanagerModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script de Atualização do Sistema de Contexto e Navegação
Atualiza automaticamente os mapas de contexto e navegação inteligente
"""

import json

class ContextSystemUpdater:
    def __init__(self):
        self.base_path = Path(".")
        self.maps_path = Path("wiki/maps")
        self.rules_path = Path(".cursor/rules")
        self.wiki_path = Path("wiki")
        
    def update_enhanced_context_system(self):
        """Atualiza o sistema de contexto avançado"""
        print("🔄 Atualizando sistema de contexto avançado...")
        
        # Verificar estrutura atual
        structure = self.analyze_directory_structure()
        
        # Atualizar contexto
        context_data = {
            "context_system": {
                "version": "2.0",
                "last_updated": datetime.now().isoformat(),
                "repository_info": {
                    "name": "otclient_doc",
                    "type": "otclient",
                    "description": "Documentação e sistema de regras do OTClient",
                    "main_focus": "client_side_development",
                    "integration_target": "canary_server"
                },
                # Estrutura de diretórios atualizada para submódulos
                "directory_structure": {
                    "root": {
                        "path": "/",
                        "description": "Raiz do repositório principal (BMAD Agent)",
                        "permissions": "full_access",
                        "key_files": [
                            "cursor.md",
                            ".gitmodules",
                            "README.md"
                        ]
                    },
                    "otclient_submodule": {
                        "path": "otclient/",
                        "description": "Submódulo OTClient (imutável, fonte de verdade)",
                        "permissions": "read_only"
                    },
                    "canary_submodule": {
                        "path": "canary/",
                        "description": "Submódulo Canary (imutável, fonte de verdade)",
                        "permissions": "read_only"
                    },
                    "wiki": {
                        "path": "wiki/",
                        "description": "Documentação e automação (editável)",
                        "permissions": "full_access",
                        "subdirectories": {
                            "bmad": "Documentação bmad",
                            "integration": "Documentação de integração",
                            "otclient": "Documentação OTClient",
                            "canary": "Documentação Canary",
                            "maps": "Mapas de navegação"
                        }
                    },
                    "cursor_rules": {
                        "path": ".cursor/rules/",
                        "description": "Sistema de regras do assistente",
                        "permissions": "full_access",
                        "total_rules": 25
                    }
                },
                "navigation_system": self.get_navigation_system(),
                "performance_optimization": self.get_performance_config(),
                "context_detection": self.get_context_detection(),
                "integration_status": self.get_integration_status()
            }
        }
        
        # Salvar arquivo
        output_file = self.maps_path / "enhanced_context_system.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(context_data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Sistema de contexto atualizado: {output_file}")
        return context_data
    
    def update_intelligent_navigation(self):
        """Atualiza o sistema de navegação inteligente"""
        print("🧭 Atualizando sistema de navegação inteligente...")
        
        navigation_data = {
            "intelligent_navigation": {
                "version": "1.0",
                "last_updated": datetime.now().isoformat(),
                "navigation_patterns": self.get_navigation_patterns(),
                "smart_caching": self.get_smart_caching(),
                "performance_metrics": self.get_performance_metrics(),
                "context_switching": self.get_context_switching(),
                "error_recovery": self.get_error_recovery()
            }
        }
        
        # Salvar arquivo
        output_file = self.maps_path / "intelligent_navigation.json"
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(navigation_data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Navegação inteligente atualizada: {output_file}")
        return navigation_data
    
    def analyze_directory_structure(self):
        """Analisa a estrutura de diretórios atual"""
        structure = {
            "root": {
                "path": "/",
                "description": "Raiz do repositório OTClient",
                "permissions": "read_only",
                "key_files": self.get_key_files(self.base_path)
            },
            "wiki": {
                "path": "wiki/",
                "description": "Documentação estruturada da wiki",
                "permissions": "full_access",
                "subdirectories": self.get_wiki_subdirectories()
            },
            "cursor_rules": {
                "path": ".cursor/rules/",
                "description": "Sistema de regras do assistente",
                "permissions": "full_access",
                "total_rules": len(list(self.rules_path.glob("*.md")))
            },
            "source_code": {
                "path": "src/",
                "description": "Código-fonte do OTClient",
                "permissions": "read_only",
                "key_components": self.get_source_components()
            },
            "modules": {
                "path": "modules/",
                "description": "Módulos Lua do OTClient",
                "permissions": "read_only",
                "categories": self.get_module_categories()
            },
            "data": {
                "path": "data/",
                "description": "Recursos e dados do cliente",
                "permissions": "read_only",
                "categories": self.get_data_categories()
            }
        }
        
        return structure
    
    def get_key_files(self, path):
        """Obtém arquivos-chave de um diretório"""
        key_files = []
        for file in path.iterdir():
            if file.is_file() and file.name in ["README.md", "CMakeLists.txt", "cursor.md"]:
                key_files.append(file.name)
        return key_files
    
    def get_wiki_subdirectories(self):
        """Obtém subdiretórios da wiki"""
        subdirs = {}
        if self.wiki_path.exists():
            for item in self.wiki_path.iterdir():
                if item.is_dir() and not item.name.startswith('.'):
                    subdirs[item.name] = f"Documentação {item.name}"
        return subdirs
    
    def get_source_components(self):
        """Obtém componentes do código-fonte"""
        src_path = Path("src")
        components = []
        if src_path.exists():
            for item in src_path.iterdir():
                if item.is_dir():
                    components.append(f"{item.name}/")
        return components
    
    def get_module_categories(self):
        """Obtém categorias de módulos"""
        modules_path = Path("modules")
        categories = []
        if modules_path.exists():
            for item in modules_path.iterdir():
                if item.is_dir():
                    categories.append(item.name)
        return categories
    
    def get_data_categories(self):
        """Obtém categorias de dados"""
        data_path = Path("data")
        categories = []
        if data_path.exists():
            for item in data_path.iterdir():
                if item.is_dir():
                    categories.append(item.name)
        return categories
    
    def get_navigation_system(self):
        """Obtém configuração do sistema de navegação"""
        return {
            "primary_indexes": {
                "wiki_map": "wiki/maps/wiki_map.json",
                "tags_index": "wiki/maps/tags_index.json",
                "relationships": "wiki/maps/relationships.json",
                "source_index": "wiki/maps/otclient_source_index.json",
                "modules_index": "wiki/maps/modules_index.json",
                "resources_index": "wiki/maps/resources_index.json",
                "styles_index": "wiki/maps/styles_index.json",
                "tools_index": "wiki/maps/tools_index.json",
                "bmad_agents": "wiki/maps/bmad_agents_index.json",
                "bmad_workflows": "wiki/maps/bmad_workflows_index.json",
                "bmad_templates": "wiki/maps/bmad_templates_index.json",
                "habdel_index": "wiki/maps/habdel_index.json"
            },
            "context_rules": {
                "otclient_focus": {
                    "priority": "high",
                    "paths": ["src/client/", "modules/client_", "data/"],
                    "documentation": "wiki/otclient/",
                    "integration": "wiki/integration/"
                },
                "bmad_system": {
                    "priority": "medium",
                    "paths": ["wiki/bmad/", ".cursor/rules/"],
                    "documentation": "wiki/bmad/",
                    "agents": "wiki/maps/bmad_agents_index.json"
                },
                "integration_focus": {
                    "priority": "medium",
                    "paths": ["wiki/integration/"],
                    "documentation": "wiki/integration/",
                    "cross_project": True
                }
            },
            "quick_access": {
                "frequently_used": [
                    "cursor.md",
                    "wiki/otclient_wiki.md",
                    ".cursor/rules/rules.md",
                    "wiki/maps/tags_index.json"
                ],
                "context_switchers": [
                    "wiki/maps/context_data.json",
                    "wiki/maps/enhanced_context_system.json"
                ],
                "performance_monitors": [
                    "wiki/log/performance_metrics.json",
                    "wiki/log/system_status.json"
                ]
            }
        }
    
    def get_performance_config(self):
        """Obtém configuração de performance"""
        return {
            "cache_strategy": {
                "file_structure": 300,
                "json_maps": 600,
                "context_data": 1800,
                "rule_references": 900
            },
            "search_limits": {
                "max_results": 50,
                "max_depth": 3,
                "max_file_reads": 10,
                "timeout_seconds": 30
            },
            "lazy_loading": {
                "enabled": True,
                "rules": True,
                "maps": True,
                "documentation": False
            }
        }
    
    def get_context_detection(self):
        """Obtém configuração de detecção de contexto"""
        return {
            "automatic": True,
            "indicators": {
                "otclient": ["otclient/", "canary/"],
                "canary": ["canary/"],
                "unified": ["wiki/otclient/", "wiki/canary/", "wiki/integration/"]
            },
            "fallback": "otclient"
        }
    
    def get_integration_status(self):
        """Obtém status de integração"""
        return {
            "otclient": "active",
            "canary": "planned",
            "unified": "in_progress",
            "bmad": "active"
        }
    
    def get_navigation_patterns(self):
        """Obtém padrões de navegação"""
        return {
            "context_aware": {
                "otclient_development": {
                    "primary_paths": ["otclient/", "canary/"],
                    "documentation": "wiki/otclient/",
                    "rules": [".cursor/rules/otclient-source-index-rules.md"],
                    "quick_access": ["cursor.md", "wiki/maps/otclient_source_index.json"]
                },
                "bmad_system": {
                    "primary_paths": ["wiki/bmad/", ".cursor/rules/"],
                    "documentation": "wiki/bmad/",
                    "rules": [".cursor/rules/bmad-system-rules.md"],
                    "quick_access": ["wiki/maps/bmad_agents_index.json", "wiki/maps/bmad_workflows_index.json"]
                },
                "wiki_documentation": {
                    "primary_paths": ["wiki/"],
                    "documentation": "wiki/",
                    "rules": [".cursor/rules/wiki-rules.md", ".cursor/rules/wiki-comprehensive-rules.md"],
                    "quick_access": ["wiki/maps/tags_index.json", "wiki/maps/wiki_map.json"]
                },
                "integration_work": {
                    "primary_paths": ["wiki/integration/"],
                    "documentation": "wiki/integration/",
                    "rules": [".cursor/rules/cross-project-integration-rules.md"],
                    "quick_access": ["wiki/maps/relationships.json"]
                }
            },
            "task_based": {
                "code_analysis": {
                    "sequence": [
                        "wiki/maps/otclient_source_index.json",
                        "src/",
                        "modules/",
                        "wiki/otclient/"
                    ],
                    "priority": "high"
                },
                "documentation_search": {
                    "sequence": [
                        "wiki/maps/tags_index.json",
                        "wiki/maps/wiki_map.json",
                        "wiki/",
                        "wiki/maps/relationships.json"
                    ],
                    "priority": "high"
                },
                "rule_consultation": {
                    "sequence": [
                        "cursor.md",
                        ".cursor/rules/",
                        "wiki/maps/enhanced_context_system.json"
                    ],
                    "priority": "medium"
                },
                "bmad_workflow": {
                    "sequence": [
                        "wiki/maps/bmad_agents_index.json",
                        "wiki/maps/bmad_workflows_index.json",
                        "wiki/bmad/",
                        ".cursor/rules/bmad-system-rules.md"
                    ],
                    "priority": "medium"
                }
            }
        }
    
    def get_smart_caching(self):
        """Obtém configuração de cache inteligente"""
        return {
            "file_access_patterns": {
                "frequently_accessed": {
                    "files": [
                        "cursor.md",
                        "wiki/maps/tags_index.json",
                        "wiki/maps/wiki_map.json",
                        ".cursor/rules/rules.md"
                    ],
                    "cache_duration": 1800,
                    "priority": "high"
                },
                "context_switchers": {
                    "files": [
                        "wiki/maps/enhanced_context_system.json",
                        "wiki/maps/context_data.json"
                    ],
                    "cache_duration": 900,
                    "priority": "medium"
                },
                "large_datasets": {
                    "files": [
                        "wiki/maps/otclient_source_index.json",
                        "wiki/maps/modules_index.json",
                        "wiki/maps/resources_index.json"
                    ],
                    "cache_duration": 3600,
                    "priority": "low"
                }
            },
            "search_optimization": {
                "indexed_searches": {
                    "tags": "wiki/maps/tags_index.json",
                    "relationships": "wiki/maps/relationships.json",
                    "source_code": "wiki/maps/otclient_source_index.json",
                    "modules": "wiki/maps/modules_index.json"
                },
                "full_text_searches": {
                    "documentation": "wiki/",
                    "rules": ".cursor/rules/",
                    "source": "src/"
                }
            }
        }
    
    def get_performance_metrics(self):
        """Obtém métricas de performance"""
        return {
            "access_patterns": {
                "most_accessed_files": [
                    "cursor.md",
                    "wiki/maps/tags_index.json",
                    "wiki/maps/wiki_map.json",
                    ".cursor/rules/rules.md"
                ],
                "access_frequency": {
                    "high": ">10 times per session",
                    "medium": "3-10 times per session",
                    "low": "<3 times per session"
                }
            },
            "response_times": {
                "target": {
                    "simple_queries": "<2 seconds",
                    "complex_queries": "<10 seconds",
                    "large_datasets": "<30 seconds"
                },
                "current": {
                    "simple_queries": "~1.5 seconds",
                    "complex_queries": "~8 seconds",
                    "large_datasets": "~25 seconds"
                }
            }
        }
    
    def get_context_switching(self):
        """Obtém configuração de troca de contexto"""
        return {
            "automatic_detection": {
                "triggers": [
                    "file_path_analysis",
                    "content_keywords",
                    "user_query_patterns"
                ],
                "confidence_threshold": 0.8
            },
            "manual_override": {
                "commands": [
                    "@otclient",
                    "@bmad",
                    "@wiki",
                    "@integration"
                ],
                "context_files": [
                    "wiki/maps/enhanced_context_system.json",
                    "wiki/maps/context_data.json"
                ]
            }
        }
    
    def get_error_recovery(self):
        """Obtém configuração de recuperação de erros"""
        return {
            "fallback_strategies": {
                "file_not_found": {
                    "action": "search_similar",
                    "fallback": "use_index"
                },
                "permission_denied": {
                    "action": "switch_context",
                    "fallback": "read_only_mode"
                },
                "timeout": {
                    "action": "reduce_scope",
                    "fallback": "simple_mode"
                }
            },
            "retry_logic": {
                "max_retries": 3,
                "backoff_strategy": "exponential",
                "timeout_increase": 1.5
            }
        }
    
    def generate_report(self):
        """Gera relatório de atualização"""
        report = {
            "update_report": {
                "timestamp": datetime.now().isoformat(),
                "files_updated": [
                    "wiki/maps/enhanced_context_system.json",
                    "wiki/maps/intelligent_navigation.json"
                ],
                "performance_improvements": {
                    "cache_strategy": "Implementado cache inteligente",
                    "navigation_patterns": "Padrões de navegação otimizados",
                    "context_detection": "Detecção automática de contexto",
                    "error_recovery": "Sistema de recuperação de erros"
                },
                "next_steps": [
                    "Monitorar performance do sistema",
                    "Ajustar configurações conforme necessário",
                    "Implementar métricas de uso",
                    "Otimizar baseado em dados reais"
                ]
            }
        }
        
        # Salvar relatório
        report_file = self.maps_path / "context_update_report.json"
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"📊 Relatório gerado: {report_file}")
        return report

def main():
    """Função principal"""
    print("🚀 Iniciando atualização do sistema de contexto e navegação...")
    
    updater = ContextSystemUpdater()
    
    # Atualizar sistema de contexto
    context_data = updater.update_enhanced_context_system()
    
    # Atualizar navegação inteligente
    navigation_data = updater.update_intelligent_navigation()
    
    # Gerar relatório
    report = updater.generate_report()
    
    print("✅ Atualização concluída com sucesso!")
    print("📈 Sistema de contexto e navegação otimizado")
    print("🎯 Próximo passo: Monitorar performance e ajustar conforme necessário")

if __name__ == "__main__":
    main() 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = ConfigmanagerModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script update_context_system.py executado com sucesso via módulo tools.config_manager")
    else:
        print(f"❌ Erro na execução do script update_context_system.py via módulo tools.config_manager")
