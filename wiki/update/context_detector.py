#!/usr/bin/env python3
"""
Script para detecção automática de contexto do repositório
Detecta se estamos em OTClient, Canary, ou futuro repositório unificado
"""
import os
import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Any

# Indicadores de contexto para OTClient
OTCLIENT_INDICATORS = [
    'otclient/',
    'otclient/src/',
    'otclient/modules/',
    'otclient/data/',
    'CMakeLists.txt',
]

# Indicadores de contexto para Canary
CANARY_INDICATORS = [
    'canary/',
    'canary/src/',
    'canary/modules/',
    'canary/data/',
]

class ContextDetector:
    def __init__(self, project_root: str = "."):
        self.project_root = Path(project_root)
        self.context = None
        self.context_data = {}
        
        # Indicadores de contexto
        self.context_indicators = {
            'otclient': {
                'files': OTCLIENT_INDICATORS,
                'content_keywords': [
                    'OTClient', 'client', 'UI', 'widgets', 'rendering',
                    'g_ui', 'UIWidget', 'modules'
                ],
                'structure': [
                    'wiki/otclient/', 'wiki/integration/', 'wiki/update/'
                ]
            },
            'canary': {
                'files': CANARY_INDICATORS,
                'content_keywords': [
                    'Canary', 'server', 'game logic', 'database',
                    'creatures', 'items', 'world management'
                ],
                'structure': [
                    'wiki/canary/', 'wiki/integration/', 'wiki/update/'
                ]
            },
            'unified': {
                'files': [
                    'wiki/otclient/', 'wiki/canary/', 'wiki/integration/',
                    'unified_wiki_index.json'
                ],
                'content_keywords': [
                    'integration', 'cross-project', 'OTClient + Canary',
                    'ecosystem', 'protocol layer'
                ],
                'structure': [
                    'wiki/otclient/', 'wiki/canary/', 'wiki/integration/'
                ]
            }
        }
    
    def detect_context(self) -> str:
        """Detecta o contexto do repositório atual"""
        print("🔍 Detectando contexto do repositório...")
        
        # 1. Análise de estrutura de arquivos
        file_score = self.analyze_file_structure()
        
        # 2. Análise de conteúdo
        content_score = self.analyze_content()
        
        # 3. Análise de estrutura de pastas
        structure_score = self.analyze_folder_structure()
        
        # 4. Determinar contexto
        self.context = self.determine_context(file_score, content_score, structure_score)
        
        # 5. Gerar dados de contexto
        self.context_data = self.generate_context_data()
        
        print(f"✅ Contexto detectado: {self.context.upper()}")
        return self.context
    
    def analyze_file_structure(self) -> Dict[str, int]:
        """Analisa a estrutura de arquivos para detectar contexto"""
        scores = {'otclient': 0, 'canary': 0, 'unified': 0}
        
        for context, indicators in self.context_indicators.items():
            for file_path in indicators['files']:
                if (self.project_root / file_path).exists():
                    scores[context] += 1
        
        return scores
    
    def analyze_content(self) -> Dict[str, int]:
        """Analisa o conteúdo dos arquivos principais"""
        scores = {'otclient': 0, 'canary': 0, 'unified': 0}
        
        # Arquivos para análise
        content_files = ['README.md', 'CMakeLists.txt', 'cursor.md']
        
        for file_name in content_files:
            file_path = self.project_root / file_name
            if file_path.exists():
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read().lower()
                    
                    for context, indicators in self.context_indicators.items():
                        for keyword in indicators['content_keywords']:
                            if keyword.lower() in content:
                                scores[context] += 1
                except Exception as e:
                    print(f"⚠️ Erro ao analisar {file_name}: {e}")
        
        return scores
    
    def analyze_folder_structure(self) -> Dict[str, int]:
        """Analisa a estrutura de pastas"""
        scores = {'otclient': 0, 'canary': 0, 'unified': 0}
        
        for context, indicators in self.context_indicators.items():
            for folder_path in indicators['structure']:
                if (self.project_root / folder_path).exists():
                    scores[context] += 1
        
        return scores
    
    def determine_context(self, file_score: Dict[str, int], 
                         content_score: Dict[str, int], 
                         structure_score: Dict[str, int]) -> str:
        """Determina o contexto baseado nos scores"""
        
        # Calcular score total
        total_scores = {}
        for context in ['otclient', 'canary', 'unified']:
            total_scores[context] = (
                file_score[context] * 2 +      # Peso maior para arquivos
                content_score[context] * 1.5 + # Peso médio para conteúdo
                structure_score[context] * 1   # Peso menor para estrutura
            )
        
        # Encontrar contexto com maior score
        max_score = max(total_scores.values())
        detected_context = max(total_scores, key=total_scores.get)
        
        # Se unified tem score alto, verificar se realmente é unificado
        if detected_context == 'unified' and total_scores['unified'] > 3:
            # Verificar se temos tanto OTClient quanto Canary
            if total_scores['otclient'] > 2 and total_scores['canary'] > 2:
                return 'unified'
            else:
                # Se não temos ambos, usar o que tem maior score
                if total_scores['otclient'] > total_scores['canary']:
                    return 'otclient'
                else:
                    return 'canary'
        
        return detected_context
    
    def generate_context_data(self) -> Dict[str, Any]:
        """Gera dados completos do contexto"""
        context_rules = {
            'otclient': {
                'docs_path': 'wiki/otclient/',
                'integration_path': 'wiki/integration/',
                'focus': 'client_side',
                'integration_enabled': True,
                'description': 'Repositório do cliente OTClient'
            },
            'canary': {
                'docs_path': 'wiki/canary/',
                'integration_path': 'wiki/integration/',
                'focus': 'server_side',
                'integration_enabled': True,
                'description': 'Repositório do servidor Canary'
            },
            'unified': {
                'docs_path': 'wiki/',
                'integration_path': 'wiki/integration/',
                'focus': 'ecosystem',
                'integration_enabled': True,
                'description': 'Repositório unificado OTClient + Canary'
            }
        }
        
        return {
            'context': self.context,
            'detected_at': datetime.now().isoformat(),
            'repository_type': context_rules[self.context]['focus'],
            'integration_enabled': context_rules[self.context]['integration_enabled'],
            'description': context_rules[self.context]['description'],
            'paths': {
                'docs': context_rules[self.context]['docs_path'],
                'integration': context_rules[self.context]['integration_path'],
                'update': 'wiki/update/',
                'maps': 'wiki/maps/'
            },
            'rules': context_rules[self.context]
        }
    
    def save_context_data(self):
        """Salva dados do contexto em arquivo JSON"""
        context_file = self.project_root / "wiki/maps/context_data.json"
        
        # Criar pasta se não existir
        context_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(context_file, 'w', encoding='utf-8') as f:
            json.dump(self.context_data, f, indent=2, ensure_ascii=False)
        
        print(f"💾 Dados de contexto salvos em: {context_file}")
    
    def get_context_rules(self) -> Dict[str, Any]:
        """Retorna regras específicas do contexto detectado"""
        if not self.context:
            self.detect_context()
        
        return self.context_data['rules']
    
    def validate_context_consistency(self) -> bool:
        """Valida se a estrutura está consistente com o contexto"""
        if not self.context:
            self.detect_context()
        
        expected_paths = self.context_data['paths']
        inconsistencies = []
        
        for path_name, path_value in expected_paths.items():
            if not (self.project_root / path_value).exists():
                inconsistencies.append(f"Missing: {path_value}")
        
        if inconsistencies:
            print(f"⚠️ Inconsistências de contexto detectadas:")
            for issue in inconsistencies:
                print(f"  - {issue}")
            return False
        
        print("✅ Estrutura consistente com o contexto")
        return True
    
    def print_context_summary(self):
        """Imprime resumo do contexto detectado"""
        if not self.context:
            self.detect_context()
        
        print(f"\n📊 RESUMO DO CONTEXTO DETECTADO")
        print(f"==================================")
        print(f"🎯 Contexto: {self.context.upper()}")
        print(f"📝 Descrição: {self.context_data['description']}")
        print(f"🎮 Tipo: {self.context_data['repository_type']}")
        print(f"🔗 Integração: {'✅ Habilitada' if self.context_data['integration_enabled'] else '❌ Desabilitada'}")
        print(f"📁 Documentação: {self.context_data['paths']['docs']}")
        print(f"🔗 Integração: {self.context_data['paths']['integration']}")
        print(f"🗺️ Mapas: {self.context_data['paths']['maps']}")
        print(f"🔄 Update: {self.context_data['paths']['update']}")
        print(f"⏰ Detectado em: {self.context_data['detected_at']}")
        print(f"==================================\n")

if __name__ == "__main__":
    detector = ContextDetector()
    detector.detect_context()
    detector.save_context_data()
    detector.validate_context_consistency()
    detector.print_context_summary() 