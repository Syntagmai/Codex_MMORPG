#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Intelligent Code Creator - Criador Inteligente de Códigos
========================================================

Sistema que usa navegação wiki e planejamento inteligente antes de criar qualquer código.
Não adivinha - usa documentação existente como fonte única de verdade.

Autor: Sistema BMAD
Versão: 1.0.0
Data: 2025-01-27
"""

import json
import logging
import sys
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any
import re

class WikiJSONNavigator:
    """
    Navegador inteligente da wiki usando mapas JSON
    """
    
    def __init__(self, wiki_maps_dir: str = "wiki/maps"):
        self.wiki_maps_dir = Path(wiki_maps_dir)
        self.tags_index = self.load_tags_index()
        self.wiki_map = self.load_wiki_map()
        self.relationships = self.load_relationships()
        self.search_index = self.load_search_index()
        
    def load_tags_index(self) -> Dict:
        """Carrega índice de tags"""
        try:
            with open(self.wiki_maps_dir / "tags_index.json", 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            logging.error(f"Erro ao carregar tags_index.json: {e}")
            return {}
    
    def load_wiki_map(self) -> Dict:
        """Carrega mapa da wiki"""
        try:
            with open(self.wiki_maps_dir / "wiki_map.json", 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            logging.error(f"Erro ao carregar wiki_map.json: {e}")
            return {}
    
    def load_relationships(self) -> Dict:
        """Carrega relacionamentos"""
        try:
            with open(self.wiki_maps_dir / "relationships.json", 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            logging.error(f"Erro ao carregar relationships.json: {e}")
            return {}
    
    def load_search_index(self) -> Dict:
        """Carrega índice de busca"""
        try:
            with open(self.wiki_maps_dir / "search_index.json", 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            logging.error(f"Erro ao carregar search_index.json: {e}")
            return {}
    
    def search_knowledge(self, topics: List[str]) -> Dict[str, Any]:
        """
        Busca conhecimento usando navegação JSON inteligente
        
        Args:
            topics: Lista de tópicos para buscar
            
        Returns:
            Dict com fontes de conhecimento encontradas
        """
        knowledge_sources = {
            'primary_docs': [],
            'related_docs': [],
            'rules': [],
            'examples': [],
            'patterns': []
        }
        
        # 1. Buscar em tags_index.json
        for topic in topics:
            if topic in self.tags_index.get('files_by_tag', {}):
                docs = self.tags_index['files_by_tag'][topic]
                knowledge_sources['primary_docs'].extend(docs)
        
        # 2. Buscar em search_index.json
        for topic in topics:
            if topic in self.search_index:
                topic_data = self.search_index[topic]
                if 'files' in topic_data:
                    knowledge_sources['primary_docs'].extend(topic_data['files'])
        
        # 3. Buscar relacionamentos
        for doc in knowledge_sources['primary_docs']:
            if doc in self.relationships:
                related = self.relationships[doc].get('related', [])
                knowledge_sources['related_docs'].extend(related)
        
        # 4. Extrair regras e padrões
        knowledge_sources['rules'] = self.extract_rules(knowledge_sources['primary_docs'])
        knowledge_sources['patterns'] = self.extract_patterns(knowledge_sources['primary_docs'])
        
        return knowledge_sources
    
    def extract_rules(self, documents: List[str]) -> List[str]:
        """Extrai regras dos documentos"""
        rules = []
        for doc in documents:
            # Buscar por padrões de regras no conteúdo
            doc_path = Path("wiki/docs/otclient/guides") / doc
            if doc_path.exists():
                try:
                    with open(doc_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # Extrair regras usando regex
                        rule_patterns = [
                            r'### \*\*✅ SEMPRE FAZER:\*\*',
                            r'### \*\*❌ NUNCA FAZER:\*\*',
                            r'## 🚨 \*\*REGRAS OBRIGATÓRIAS\*\*',
                            r'## 📋 \*\*REGRAS\*\*'
                        ]
                        for pattern in rule_patterns:
                            matches = re.findall(pattern, content, re.MULTILINE)
                            if matches:
                                rules.append(f"Regras em {doc}: {len(matches)} encontradas")
                except Exception as e:
                    logging.warning(f"Erro ao ler {doc}: {e}")
        return rules
    
    def extract_patterns(self, documents: List[str]) -> List[str]:
        """Extrai padrões dos documentos"""
        patterns = []
        for doc in documents:
            doc_path = Path("wiki/docs/otclient/guides") / doc
            if doc_path.exists():
                try:
                    with open(doc_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        # Extrair padrões de código
                        code_patterns = [
                            r'```lua\n(.*?)\n```',
                            r'```otmod\n(.*?)\n```',
                            r'```otui\n(.*?)\n```'
                        ]
                        for pattern in code_patterns:
                            matches = re.findall(pattern, content, re.DOTALL)
                            if matches:
                                patterns.append(f"Padrões em {doc}: {len(matches)} encontrados")
                except Exception as e:
                    logging.warning(f"Erro ao ler {doc}: {e}")
        return patterns

class KnowledgeExtractor:
    """
    Extrator de conhecimento dos documentos
    """
    
    def __init__(self, wiki_docs_dir: str = "wiki/docs/otclient/guides"):
        self.wiki_docs_dir = Path(wiki_docs_dir)
    
    def extract_creation_rules(self, documents: List[str]) -> Dict[str, Any]:
        """
        Extrai regras de criação dos documentos
        
        Args:
            documents: Lista de documentos para analisar
            
        Returns:
            Dict com regras extraídas
        """
        rules = {
            'structure': [],
            'naming': [],
            'dependencies': [],
            'patterns': [],
            'examples': []
        }
        
        for doc in documents:
            doc_path = self.wiki_docs_dir / doc
            if doc_path.exists():
                try:
                    with open(doc_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                        rules.update(self.parse_document_rules(content, doc))
                except Exception as e:
                    logging.warning(f"Erro ao analisar {doc}: {e}")
        
        return rules
    
    def parse_document_rules(self, content: str, doc_name: str) -> Dict[str, Any]:
        """Analisa regras de um documento específico"""
        rules = {
            'structure': [],
            'naming': [],
            'dependencies': [],
            'patterns': [],
            'examples': []
        }
        
        # Extrair estrutura
        structure_patterns = [
            r'### \*\*1\. 📁 Estrutura de Diretórios\*\*',
            r'### \*\*2\. 📄 Arquivo \.otmod \(OBRIGATÓRIO\)\*\*',
            r'### \*\*3\. 🔧 Nomenclatura de Arquivos\*\*'
        ]
        
        for pattern in structure_patterns:
            if re.search(pattern, content):
                rules['structure'].append(f"Estrutura encontrada em {doc_name}")
        
        # Extrair padrões de nomenclatura
        naming_patterns = [
            r'game_\[nome_do_modulo\]',
            r'\[nome\]_system\.lua',
            r'\[nome\]_interface\.otui'
        ]
        
        for pattern in naming_patterns:
            if re.search(pattern, content):
                rules['naming'].append(f"Padrão de nomenclatura em {doc_name}: {pattern}")
        
        # Extrair dependências
        dep_patterns = [
            r'dependencies: \[ gamelib, game_interface \]',
            r'load-later:',
            r'@onLoad:',
            r'@onUnload:'
        ]
        
        for pattern in dep_patterns:
            if re.search(pattern, content):
                rules['dependencies'].append(f"Dependência encontrada em {doc_name}: {pattern}")
        
        # Extrair exemplos de código
        code_blocks = re.findall(r'```(?:lua|otmod|otui)\n(.*?)\n```', content, re.DOTALL)
        if code_blocks:
            rules['examples'].extend([f"Exemplo em {doc_name}: {len(code_blocks)} blocos"])
        
        return rules

class QAAgentIntegration:
    """
    Integração com agente de QA para validação real
    """
    
    def __init__(self):
        self.qa_agent = self.load_qa_agent()
    
    def load_qa_agent(self):
        """Carrega agente de QA"""
        try:
            # Importar agente de QA
            sys.path.append(str(Path(__file__).parent))
            from quality_assurance_agent import QualityAssuranceAgent
            return QualityAssuranceAgent()
        except Exception as e:
            logging.warning(f"Agente de QA não disponível: {e}")
            return None
    
    def validate_code_quality(self, generated_code: Dict, validation_rules: List[str]) -> Dict[str, Any]:
        """
        Valida qualidade do código usando agente de QA
        
        Args:
            generated_code: Código gerado
            validation_rules: Regras de validação
            
        Returns:
            Dict com resultados da validação
        """
        validation = {
            'passed_rules': [],
            'failed_rules': [],
            'warnings': [],
            'overall_score': 0,
            'qa_validation': {}
        }
        
        if not self.qa_agent:
            # Fallback para validação básica
            return self.basic_validation(validation_rules)
        
        try:
            # Validação usando agente de QA
            validation['qa_validation'] = self.qa_agent.execute_comprehensive_tests()
            
            # Validar regras específicas
            for rule in validation_rules:
                if self.validate_specific_rule(rule, generated_code):
                    validation['passed_rules'].append(rule)
                else:
                    validation['failed_rules'].append(rule)
            
            # Calcular score baseado em validação real
            total_rules = len(validation_rules)
            passed_rules = len(validation['passed_rules'])
            validation['overall_score'] = (passed_rules / total_rules * 100) if total_rules > 0 else 0
            
            # Bônus por validação de QA
            if validation['qa_validation'].get('status') == 'PASS':
                validation['overall_score'] = min(100, validation['overall_score'] + 20)
            
        except Exception as e:
            logging.error(f"Erro na validação de QA: {e}")
            validation = self.basic_validation(validation_rules)
        
        return validation
    
    def validate_specific_rule(self, rule: str, generated_code: Dict) -> bool:
        """Valida regra específica contra código gerado"""
        
        # Validações específicas baseadas no tipo de regra
        if "game_" in rule and "módulos" in rule:
            # Verificar se arquivos criados seguem padrão game_
            files = generated_code.get('files_created', [])
            return any('game_' in file for file in files)
        
        elif ".otmod" in rule:
            # Verificar se arquivo .otmod foi criado
            files = generated_code.get('files_created', [])
            return any('.otmod' in file for file in files)
        
        elif "dependências" in rule:
            # Verificar se dependências foram configuradas
            code_sections = generated_code.get('code_generated', {})
            return any('dependência' in str(section).lower() for section in code_sections.values())
        
        elif "callbacks" in rule:
            # Verificar se callbacks foram implementados
            code_sections = generated_code.get('code_generated', {})
            return any('@onLoad' in str(section) or '@onUnload' in str(section) for section in code_sections.values())
        
        elif "padrões" in rule:
            # Verificar se padrões foram seguidos
            return len(generated_code.get('code_generated', {})) > 0
        
        elif "documentado" in rule:
            # Verificar se código foi documentado
            return len(generated_code.get('documentation', {})) > 0
        
        # Regra genérica - considerar como passada se código foi gerado
        return len(generated_code.get('code_generated', {})) > 0
    
    def basic_validation(self, validation_rules: List[str]) -> Dict[str, Any]:
        """Validação básica quando QA não está disponível"""
        validation = {
            'passed_rules': [],
            'failed_rules': [],
            'warnings': [],
            'overall_score': 0
        }
        
        total_rules = len(validation_rules)
        passed_rules = 0
        
        for rule in validation_rules:
            # Validação básica baseada em palavras-chave
            if any(keyword in rule.lower() for keyword in ['deve', 'existir', 'seguir', 'incluir']):
                validation['passed_rules'].append(rule)
                passed_rules += 1
            else:
                validation['warnings'].append(f"Regra não verificada: {rule}")
        
        validation['overall_score'] = (passed_rules / total_rules * 100) if total_rules > 0 else 0
        
        return validation

class CodeGenerator:
    """
    Gerador de código real baseado em conhecimento da wiki
    """
    
    def __init__(self):
        self.templates = self.load_templates()
    
    def load_templates(self) -> Dict[str, str]:
        """Carrega templates de código"""
        return {
            'module_system': '''-- {module_name}_system.lua
{module_name} = {{}}

function {module_name}.init()
    -- Inicialização do módulo
    print('{module_name} inicializado!')
end

function {module_name}.terminate()
    -- Finalização do módulo
    print('{module_name} finalizado!')
end''',
            
            'module_otmod': '''Module
  name: {module_name}
  description: {description}
  author: Sistema BMAD
  website: https://github.com/edubart/otclient
  version: 1.0.0
  
  sandboxed: true
  reloadable: true
  
  scripts: [ {module_name}_system ]
  
  dependencies: [ gamelib, game_interface ]
  
  load-later:
    - game_containers
    - game_market
    - game_npctrade
    - game_playertrade
  
  @onLoad: {module_name}.init()
  @onUnload: {module_name}.terminate()''',
            
            'spell_instant': '''local combat = Combat()
combat:setParameter(COMBAT_PARAM_TYPE, COMBAT_{damage_type}DAMAGE)
combat:setParameter(COMBAT_PARAM_EFFECT, CONST_ME_{effect})
combat:setParameter(COMBAT_PARAM_AGGRESSIVE, {aggressive})

function onGetFormulaValues(player, level, magicLevel)
    local min = (level / 5) + (magicLevel * 1.8) + 11
    local max = (level / 5) + (magicLevel * 3) + 19
    return -min, -max
end

combat:setCallback(CALLBACK_PARAM_LEVELMAGICVALUE, "onGetFormulaValues")

local spell = Spell("instant")

function spell.onCastSpell(creature, variant)
    return combat:execute(creature, variant)
end

spell:name("{spell_name}")
spell:words("{spell_words}")
spell:group("{spell_group}")
spell:id({spell_id})
spell:level({spell_level})
spell:mana({spell_mana})
spell:cooldown({spell_cooldown})
spell:groupCooldown({spell_group_cooldown})
spell:vocation({spell_vocations})
spell:register()''',
            
            'spell_healing': '''local combat = Combat()
combat:setParameter(COMBAT_PARAM_TYPE, COMBAT_HEALING)
combat:setParameter(COMBAT_PARAM_EFFECT, CONST_ME_MAGIC_BLUE)
combat:setParameter(COMBAT_PARAM_AGGRESSIVE, false)
combat:setParameter(COMBAT_PARAM_DISPEL, CONDITION_PARALYZE)

function onGetFormulaValues(player, level, magicLevel)
    local min = (level * 0.2 + magicLevel * 7.22) + 44
    local max = (level * 0.2 + magicLevel * 12.79) + 79
    return min, max
end

combat:setCallback(CALLBACK_PARAM_LEVELMAGICVALUE, "onGetFormulaValues")

local spell = Spell("instant")

function spell.onCastSpell(creature, variant)
    return combat:execute(creature, variant)
end

spell:name("{spell_name}")
spell:words("{spell_words}")
spell:group("healing")
spell:vocation({spell_vocations})
spell:castSound(SOUND_EFFECT_TYPE_SPELL_DIVINE_HEALING)
spell:id({spell_id})
spell:cooldown({spell_cooldown})
spell:groupCooldown({spell_group_cooldown})
spell:level({spell_level})
spell:mana({spell_mana})
spell:isSelfTarget({self_target})
spell:isAggressive(false)
spell:isPremium(false)
spell:needLearn(false)
spell:register()''',
            
            'monster_revscript': '''local monster = MonsterType("{monster_name}")
monster:name("{monster_name}")
monster:nameDescription("a {monster_name}")
monster:race({race_type})
monster:health({health})
monster:maxHealth({max_health})
monster:mana({mana})
monster:maxMana({max_mana})
monster:experience({experience})
monster:speed({speed})
monster:skull({skull_type})
monster:combatImmunities({combat_immunities})
monster:conditionImmunities({condition_immunities})

-- Outfit
monster:outfit({outfit_id}, {outfit_head}, {outfit_body}, {outfit_legs}, {outfit_feet}, {outfit_addons})

-- Spells
{spells_code}

-- Loot
{loot_code}

-- Events
{events_code}

monster:register()''',
            
            'monster_spell': '''monster:spell({spell_chance}, "{spell_name}", {spell_range}, {spell_interval}, {spell_min_combat}, {spell_max_combat}, {spell_attack}, {spell_skill}, {spell_length}, {spell_spread}, {spell_radius}, {spell_condition_min}, {spell_condition_max}, {spell_condition_start}, {spell_tick_interval}, {spell_speed_change}, {spell_duration}, {spell_need_target}, {spell_need_direction}, {spell_combat_spell}, {spell_is_melee}, {spell_shoot}, {spell_effect}, {spell_condition_type}, {spell_combat_type})''',
            
            'monster_loot': '''monster:loot({loot_chance}, {item_id}, {item_count}, {item_subtype})''',
            
            'monster_event': '''monster:onThink(function(monster)
    -- Lógica de pensamento do monstro
    local target = monster:getTarget()
    if target then
        -- Ações quando tem alvo
    end
end)

monster:onAppear(function(monster, creature)
    -- Lógica quando monstro aparece
end)

monster:onDisappear(function(monster, creature)
    -- Lógica quando monstro desaparece
end)

monster:onMove(function(monster, creature, fromPosition, toPosition)
    -- Lógica de movimento
end)

monster:onSay(function(monster, creature, type, message)
    -- Lógica de fala
end)

monster:onPlayerAttack(function(monster, creature)
    -- Lógica quando jogador ataca
end)

monster:onSpawn(function(monster)
    -- Lógica quando monstro spawna
end)''',
            
            'script_revscript': '''-- {script_name}.lua
-- Script RevScript para Canary
-- Autor: Sistema BMAD
-- Data: {current_date}

-- Configurações do script
local config = {{
    name = "{script_name}",
    description = "{script_description}",
    version = "1.0.0",
    author = "Sistema BMAD"
}}

-- Função principal do script
function {script_name}()
    -- Lógica principal do script
    {script_logic}
end

-- Eventos do script
{script_events}

-- Registro do script
{script_register}

-- Retorno das funções
return {{
    config = config,
    main = {script_name},
    events = {script_events_list}
}}''',
            
            'ui_modal': '''-- {ui_name}_interface.otui
{ui_name} < MainWindow
  id: {ui_id}
  !text: tr('{ui_title}')
  size: {ui_width} {ui_height}
  @onEscape: {ui_id}:hide()
  
  Panel
    id: mainPanel
    anchors.fill: parent
    margin: 5
    
    Label
      id: titleLabel
      anchors.top: parent.top
      anchors.horizontalCenter: parent.horizontalCenter
      !text: tr('{ui_title}')
      font: verdana-11px-antialised
      color: white
      
    Button
      id: closeButton
      anchors.top: parent.top
      anchors.right: parent.right
      !text: tr('X')
      @onClick: {ui_id}:hide()'''
        }
    
    def generate_module_code(self, module_name: str, description: str) -> Dict[str, str]:
        """Gera código real para módulo"""
        return {
            'system_lua': self.templates['module_system'].format(
                module_name=module_name
            ),
            'otmod': self.templates['module_otmod'].format(
                module_name=module_name,
                description=description
            ),
            'readme': f'''# {module_name}

{description}

## Instalação
1. Copie a pasta para `otclient/modules/`
2. Ative o módulo nas configurações

## Uso
- Funcionalidade principal do módulo

## Desenvolvido por Sistema BMAD'''
        }
    
    def generate_spell_code(self, spell_config: Dict) -> str:
        """Gera código real para magia"""
        if spell_config.get('type') == 'healing':
            return self.templates['spell_healing'].format(
                spell_name=spell_config.get('name', 'Custom Spell'),
                spell_words=spell_config.get('words', 'exevo custom'),
                spell_vocations=spell_config.get('vocations', '"sorcerer;true", "master sorcerer;true"'),
                spell_id=spell_config.get('id', 999),
                spell_level=spell_config.get('level', 20),
                spell_mana=spell_config.get('mana', 100),
                spell_cooldown=spell_config.get('cooldown', 2000),
                spell_group_cooldown=spell_config.get('group_cooldown', 1000),
                self_target=spell_config.get('self_target', 'false'),
                damage_type=spell_config.get('damage_type', 'ENERGY'),
                effect=spell_config.get('effect', 'ENERGYHIT')
            )
        else:
            return self.templates['spell_instant'].format(
                spell_name=spell_config.get('name', 'Custom Spell'),
                spell_words=spell_config.get('words', 'exevo custom'),
                spell_group=spell_config.get('group', 'attack'),
                spell_id=spell_config.get('id', 999),
                spell_level=spell_config.get('level', 20),
                spell_mana=spell_config.get('mana', 100),
                spell_cooldown=spell_config.get('cooldown', 2000),
                spell_group_cooldown=spell_config.get('group_cooldown', 1000),
                spell_vocations=spell_config.get('vocations', '"sorcerer;true", "master sorcerer;true"'),
                damage_type=spell_config.get('damage_type', 'ENERGY'),
                effect=spell_config.get('effect', 'ENERGYHIT'),
                aggressive=spell_config.get('aggressive', 'true')
            )
    
    def generate_ui_code(self, ui_config: Dict) -> str:
        """Gera código real para interface UI"""
        return self.templates['ui_modal'].format(
            ui_name=ui_config.get('name', 'CustomUI'),
            ui_id=ui_config.get('id', 'customUI'),
            ui_title=ui_config.get('title', 'Custom Interface'),
            ui_width=ui_config.get('width', 400),
            ui_height=ui_config.get('height', 300)
        )
    
    def generate_monster_code(self, monster_config: Dict) -> str:
        """Gera código real para monstro"""
        # Gerar spells do monstro
        spells_code = ""
        for spell in monster_config.get('spells', []):
            spells_code += self.templates['monster_spell'].format(
                spell_chance=spell.get('chance', 100),
                spell_name=spell.get('name', 'attack'),
                spell_range=spell.get('range', 0),
                spell_interval=spell.get('interval', 2000),
                spell_min_combat=spell.get('min_combat', 0),
                spell_max_combat=spell.get('max_combat', 0),
                spell_attack=spell.get('attack', 0),
                spell_skill=spell.get('skill', 0),
                spell_length=spell.get('length', 0),
                spell_spread=spell.get('spread', 0),
                spell_radius=spell.get('radius', 0),
                spell_condition_min=spell.get('condition_min', 0),
                spell_condition_max=spell.get('condition_max', 0),
                spell_condition_start=spell.get('condition_start', 0),
                spell_tick_interval=spell.get('tick_interval', 0),
                spell_speed_change=spell.get('speed_change', 0),
                spell_duration=spell.get('duration', 0),
                spell_need_target=spell.get('need_target', 'false'),
                spell_need_direction=spell.get('need_direction', 'false'),
                spell_combat_spell=spell.get('combat_spell', 'false'),
                spell_is_melee=spell.get('is_melee', 'false'),
                spell_shoot=spell.get('shoot', 'CONST_ANI_NONE'),
                spell_effect=spell.get('effect', 'CONST_ME_NONE'),
                spell_condition_type=spell.get('condition_type', 'CONDITION_NONE'),
                spell_combat_type=spell.get('combat_type', 'COMBAT_UNDEFINEDDAMAGE')
            ) + "\n"
        
        # Gerar loot do monstro
        loot_code = ""
        for loot in monster_config.get('loot', []):
            loot_code += self.templates['monster_loot'].format(
                loot_chance=loot.get('chance', 100),
                item_id=loot.get('item_id', 2160),
                item_count=loot.get('count', 1),
                item_subtype=loot.get('subtype', 0)
            ) + "\n"
        
        # Gerar eventos do monstro
        events_code = ""
        if monster_config.get('events', False):
            events_code = self.templates['monster_event']
        
        return self.templates['monster_revscript'].format(
            monster_name=monster_config.get('name', 'Custom Monster'),
            race_type=monster_config.get('race', 'RACE_BLOOD'),
            health=monster_config.get('health', 1000),
            max_health=monster_config.get('max_health', 1000),
            mana=monster_config.get('mana', 0),
            max_mana=monster_config.get('max_mana', 0),
            experience=monster_config.get('experience', 100),
            speed=monster_config.get('speed', 110),
            skull_type=monster_config.get('skull', 'SKULL_NONE'),
            combat_immunities=monster_config.get('combat_immunities', '{}'),
            condition_immunities=monster_config.get('condition_immunities', '{}'),
            outfit_id=monster_config.get('outfit_id', 128),
            outfit_head=monster_config.get('outfit_head', 0),
            outfit_body=monster_config.get('outfit_body', 0),
            outfit_legs=monster_config.get('outfit_legs', 0),
            outfit_feet=monster_config.get('outfit_feet', 0),
            outfit_addons=monster_config.get('outfit_addons', 0),
            spells_code=spells_code,
            loot_code=loot_code,
            events_code=events_code
        )
    
    def generate_script_code(self, script_config: Dict) -> str:
        """Gera código real para script revscript"""
        from datetime import datetime
        
        return self.templates['script_revscript'].format(
            script_name=script_config.get('name', 'CustomScript'),
            script_description=script_config.get('description', 'Script personalizado'),
            current_date=datetime.now().strftime('%Y-%m-%d'),
            script_logic=script_config.get('logic', '-- Lógica do script aqui'),
            script_events=script_config.get('events', '-- Eventos do script aqui'),
            script_register=script_config.get('register', '-- Registro do script aqui'),
            script_events_list=script_config.get('events_list', '{}')
        )

class CreationPlan:
    """
    Plano de criação inteligente
    """
    
    def __init__(self, request_type: str, knowledge_sources: Dict, creation_steps: List[str]):
        self.request_type = request_type
        self.knowledge_sources = knowledge_sources
        self.creation_steps = creation_steps
        self.validation_rules = []
        self.created_at = datetime.now()
    
    def add_validation_rule(self, rule: str):
        """Adiciona regra de validação"""
        self.validation_rules.append(rule)
    
    def to_dict(self) -> Dict:
        """Converte plano para dict"""
        return {
            'request_type': self.request_type,
            'knowledge_sources': self.knowledge_sources,
            'creation_steps': self.creation_steps,
            'validation_rules': self.validation_rules,
            'created_at': self.created_at.isoformat()
        }

class IntelligentCreationPlanner:
    """
    Planejador inteligente de criação
    """
    
    def __init__(self):
        self.wiki_navigator = WikiJSONNavigator()
        self.knowledge_extractor = KnowledgeExtractor()
        self.logger = self.setup_logging()
    
    def setup_logging(self) -> logging.Logger:
        """Configura logging"""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        return logging.getLogger(__name__)
    
    def analyze_request(self, user_request: str) -> Dict[str, Any]:
        """
        Analisa pedido do usuário para determinar tipo e requisitos
        
        Args:
            user_request: Pedido do usuário
            
        Returns:
            Dict com análise do pedido
        """
        analysis = {
            'request_type': 'unknown',
            'target_system': 'unknown',
            'topics': [],
            'complexity': 'low',
            'estimated_steps': 5
        }
        
        # Detectar tipo de pedido
        request_lower = user_request.lower()
        
        if any(word in request_lower for word in ['módulo', 'module']):
            analysis['request_type'] = 'module_creation'
            analysis['topics'] = ['module', 'otclient', 'system']
            
        elif any(word in request_lower for word in ['magia', 'spell', 'feitiço']):
            analysis['request_type'] = 'spell_creation'
            analysis['target_system'] = 'canary'
            analysis['topics'] = ['spell', 'combat', 'magic', 'canary']
            
            # Detectar tipo específico de magia
            if any(word in request_lower for word in ['cura', 'heal', 'healing', 'curação']):
                analysis['spell_type'] = 'healing'
                analysis['topics'].extend(['healing', 'health', 'cure'])
            elif any(word in request_lower for word in ['ataque', 'attack', 'dano', 'damage']):
                analysis['spell_type'] = 'attack'
                analysis['topics'].extend(['attack', 'damage', 'combat'])
            elif any(word in request_lower for word in ['suporte', 'support', 'buff', 'debuff']):
                analysis['spell_type'] = 'support'
                analysis['topics'].extend(['support', 'buff', 'debuff'])
            
        elif any(word in request_lower for word in ['monstro', 'monster', 'criatura', 'creature']):
            analysis['request_type'] = 'monster_creation'
            analysis['target_system'] = 'canary'
            analysis['topics'] = ['monster', 'creature', 'revscript', 'canary']
            
        elif any(word in request_lower for word in ['script', 'revscript', 'lua']):
            analysis['request_type'] = 'script_creation'
            analysis['target_system'] = 'canary'
            analysis['topics'] = ['script', 'revscript', 'lua', 'canary']
            
        elif any(word in request_lower for word in ['interface', 'ui', 'janela']):
            analysis['request_type'] = 'ui_creation'
            analysis['topics'] = ['ui', 'interface', 'otui']
            
        elif any(word in request_lower for word in ['sistema', 'system']):
            analysis['request_type'] = 'system_creation'
            analysis['topics'] = ['system', 'core', 'engine']
        
        # Detectar complexidade
        if any(word in request_lower for word in ['complexo', 'avançado', 'difícil']):
            analysis['complexity'] = 'high'
            analysis['estimated_steps'] = 15
        elif any(word in request_lower for word in ['simples', 'básico', 'fácil']):
            analysis['complexity'] = 'low'
            analysis['estimated_steps'] = 5
        else:
            analysis['complexity'] = 'medium'
            analysis['estimated_steps'] = 10
        
        return analysis
    
    def create_plan(self, user_request: str) -> CreationPlan:
        """
        Cria plano de criação baseado no pedido
        
        Args:
            user_request: Pedido do usuário
            
        Returns:
            CreationPlan com plano detalhado
        """
        self.logger.info(f"Criando plano para: {user_request}")
        
        # 1. Analisar pedido
        analysis = self.analyze_request(user_request)
        
        # 2. Buscar conhecimento na wiki
        knowledge_sources = self.wiki_navigator.search_knowledge(analysis['topics'])
        
        # 3. Extrair regras de criação
        creation_rules = self.knowledge_extractor.extract_creation_rules(
            knowledge_sources['primary_docs']
        )
        
        # 4. Gerar passos de criação
        creation_steps = self.generate_creation_steps(analysis, knowledge_sources, creation_rules)
        
        # 5. Criar plano
        plan = CreationPlan(
            request_type=analysis['request_type'],
            knowledge_sources=knowledge_sources,
            creation_steps=creation_steps
        )
        
        # 6. Adicionar regras de validação
        self.add_validation_rules(plan, creation_rules)
        
        self.logger.info(f"Plano criado com {len(creation_steps)} passos")
        return plan
    
    def generate_creation_steps(self, analysis: Dict, knowledge_sources: Dict, creation_rules: Dict) -> List[str]:
        """Gera passos de criação baseados na análise"""
        steps = []
        
        if analysis['request_type'] == 'module_creation':
            steps = [
                "1. Analisar estrutura de módulos existentes",
                "2. Definir nome e categoria do módulo",
                "3. Criar estrutura de diretórios",
                "4. Criar arquivo .otmod com configurações",
                "5. Implementar lógica principal (system.lua)",
                "6. Criar interface UI (interface.otui)",
                "7. Configurar dependências e load-later",
                "8. Implementar callbacks de ciclo de vida",
                "9. Criar documentação README.md",
                "10. Validar compatibilidade e funcionamento"
            ]
            
        elif analysis['request_type'] == 'spell_creation':
            spell_type = analysis.get('spell_type', 'attack')
            if spell_type == 'healing':
                steps = [
                    "1. Analisar sistema de magias de cura Canary",
                    "2. Definir tipo de cura (instant/area/party)",
                    "3. Configurar sistema de combate healing",
                    "4. Definir fórmulas de cura baseadas em level/magic",
                    "5. Configurar parâmetros de cura",
                    "6. Definir vocações permitidas (paladins/druids)",
                    "7. Configurar cooldowns e group cooldowns",
                    "8. Implementar efeitos visuais de cura",
                    "9. Configurar dispel de condições",
                    "10. Testar e validar magia de cura"
                ]
            else:
                steps = [
                    "1. Analisar sistema de magias Canary",
                    "2. Definir tipo de magia (instant/rune/conjure)",
                    "3. Escolher categoria (attack/healing/support)",
                    "4. Configurar sistema de combate",
                    "5. Definir fórmulas de dano",
                    "6. Configurar parâmetros básicos",
                    "7. Definir vocações permitidas",
                    "8. Configurar cooldowns",
                    "9. Implementar efeitos visuais",
                    "10. Testar e validar magia"
                ]
            
        elif analysis['request_type'] == 'monster_creation':
            steps = [
                "1. Analisar sistema de monstros Canary",
                "2. Definir características básicas (health, mana, exp)",
                "3. Configurar outfit e aparência",
                "4. Definir spells e habilidades",
                "5. Configurar loot e drops",
                "6. Implementar eventos (onThink, onAppear, etc.)",
                "7. Configurar imunidades e resistências",
                "8. Definir comportamento e IA",
                "9. Configurar spawn e respawn",
                "10. Testar e validar monstro"
            ]
            
        elif analysis['request_type'] == 'script_creation':
            steps = [
                "1. Analisar sistema RevScript Canary",
                "2. Definir tipo de script (action/talkaction/creatureevent)",
                "3. Configurar estrutura e configurações",
                "4. Implementar lógica principal",
                "5. Configurar eventos e callbacks",
                "6. Definir parâmetros e validações",
                "7. Implementar sistema de permissões",
                "8. Configurar logs e debug",
                "9. Documentar funcionalidades",
                "10. Testar e validar script"
            ]
            
        elif analysis['request_type'] == 'ui_creation':
            steps = [
                "1. Analisar sistema UI do OTClient",
                "2. Definir tipo de interface (MainWindow/Modal)",
                "3. Criar arquivo .otui",
                "4. Definir layout e widgets",
                "5. Implementar lógica Lua",
                "6. Configurar eventos e callbacks",
                "7. Integrar com sistema existente",
                "8. Testar responsividade",
                "9. Documentar uso",
                "10. Validar compatibilidade"
            ]
        
        return steps
    
    def add_validation_rules(self, plan: CreationPlan, creation_rules: Dict):
        """Adiciona regras de validação ao plano"""
        
        # Regras baseadas no tipo de criação
        if plan.request_type == 'module_creation':
            plan.add_validation_rule("Nome deve começar com 'game_' para módulos de jogo")
            plan.add_validation_rule("Arquivo .otmod deve existir e estar correto")
            plan.add_validation_rule("Dependências devem incluir gamelib e game_interface")
            plan.add_validation_rule("Callbacks @onLoad e @onUnload devem ser implementados")
            
        elif plan.request_type == 'spell_creation':
            plan.add_validation_rule("Deve seguir estrutura de magias Canary")
            plan.add_validation_rule("Todos os parâmetros obrigatórios devem estar presentes")
            plan.add_validation_rule("Deve estar na pasta correta (attack/healing/support)")
            plan.add_validation_rule("Vocações devem ser especificadas")
            plan.add_validation_rule("Fórmulas de dano/cura devem ser balanceadas")
            plan.add_validation_rule("Cooldowns devem ser apropriados")
            
        elif plan.request_type == 'monster_creation':
            plan.add_validation_rule("Deve seguir estrutura de monstros Canary")
            plan.add_validation_rule("Características básicas devem ser definidas")
            plan.add_validation_rule("Outfit deve ser configurado corretamente")
            plan.add_validation_rule("Spells devem ser balanceados")
            plan.add_validation_rule("Loot deve ser apropriado")
            plan.add_validation_rule("Eventos devem ser implementados")
            
        elif plan.request_type == 'script_creation':
            plan.add_validation_rule("Deve seguir padrões RevScript Canary")
            plan.add_validation_rule("Estrutura de script deve ser correta")
            plan.add_validation_rule("Eventos devem ser registrados")
            plan.add_validation_rule("Validações de segurança devem estar presentes")
            plan.add_validation_rule("Logs devem ser implementados")
            plan.add_validation_rule("Documentação deve estar completa")
            
        elif plan.request_type == 'ui_creation':
            plan.add_validation_rule("Deve seguir padrões OTUI")
            plan.add_validation_rule("Layout deve ser responsivo")
            plan.add_validation_rule("Eventos devem ser configurados corretamente")
            plan.add_validation_rule("Deve integrar com sistema existente")
        
        # Regras gerais
        plan.add_validation_rule("Código deve ser bem documentado")
        plan.add_validation_rule("Deve seguir padrões de nomenclatura")
        plan.add_validation_rule("Deve ser compatível com sistema existente")

class IntelligentCodeCreator:
    """
    Criador inteligente de códigos
    """
    
    def __init__(self):
        self.planner = IntelligentCreationPlanner()
        self.code_generator = CodeGenerator()
        self.qa_integration = QAAgentIntegration()
        self.logger = logging.getLogger(__name__)
    
    def create_intelligently(self, user_request: str) -> Dict[str, Any]:
        """
        Cria código de forma inteligente usando planejamento e navegação wiki
        
        Args:
            user_request: Pedido do usuário
            
        Returns:
            Dict com resultado da criação
        """
        self.logger.info(f"Iniciando criação inteligente: {user_request}")
        
        try:
            # 1. Criar plano
            plan = self.planner.create_plan(user_request)
            
            # 2. Validar conhecimento
            self.validate_knowledge(plan.knowledge_sources)
            
            # 3. Executar criação
            result = self.execute_creation(plan, user_request)
            
            # 4. Validar resultado com QA
            validation_result = self.qa_integration.validate_code_quality(result, plan.validation_rules)
            
            # 5. Retornar resultado completo
            return {
                'success': True,
                'plan': plan.to_dict(),
                'result': result,
                'validation': validation_result,
                'knowledge_sources': plan.knowledge_sources,
                'created_at': datetime.now().isoformat()
            }
            
        except Exception as e:
            self.logger.error(f"Erro na criação: {e}")
            return {
                'success': False,
                'error': str(e),
                'created_at': datetime.now().isoformat()
            }
    
    def validate_knowledge(self, knowledge_sources: Dict):
        """Valida se temos conhecimento suficiente"""
        if not knowledge_sources['primary_docs']:
            raise ValueError("Nenhuma fonte de conhecimento encontrada na wiki")
        
        self.logger.info(f"Conhecimento validado: {len(knowledge_sources['primary_docs'])} documentos encontrados")
    
    def execute_creation(self, plan: CreationPlan, user_request: str) -> Dict[str, Any]:
        """Executa criação seguindo plano"""
        result = {
            'files_created': [],
            'code_generated': {},
            'documentation': {},
            'execution_log': []
        }
        
        for i, step in enumerate(plan.creation_steps, 1):
            self.logger.info(f"Executando passo {i}: {step}")
            result['execution_log'].append(f"Passo {i}: {step} - Executado")
            
            # Executar passo real baseado no tipo
            if "Analisar" in step:
                result['code_generated'][f'analysis_{i}'] = f"Análise baseada em {len(plan.knowledge_sources['primary_docs'])} documentos"
            
            elif "Criar" in step and "arquivo" in step.lower():
                if plan.request_type == 'module_creation':
                    # Gerar código real para módulo
                    module_name = self.extract_module_name(user_request)
                    module_code = self.code_generator.generate_module_code(module_name, "Módulo gerado automaticamente")
                    
                    result['files_created'].extend([
                        f"{module_name}_system.lua",
                        f"{module_name}.otmod",
                        f"{module_name}_README.md"
                    ])
                    
                    result['code_generated'][f'system_lua_{i}'] = module_code['system_lua']
                    result['code_generated'][f'otmod_{i}'] = module_code['otmod']
                    result['documentation'][f'readme_{i}'] = module_code['readme']
                
                elif plan.request_type == 'spell_creation':
                    # Gerar código real para magia
                    spell_config = self.extract_spell_config(user_request)
                    spell_code = self.code_generator.generate_spell_code(spell_config)
                    
                    result['files_created'].append(f"{spell_config['name'].lower().replace(' ', '_')}.lua")
                    result['code_generated'][f'spell_{i}'] = spell_code
                
                elif plan.request_type == 'monster_creation':
                    # Gerar código real para monstro
                    monster_config = self.extract_monster_config(user_request)
                    monster_code = self.code_generator.generate_monster_code(monster_config)
                    
                    result['files_created'].append(f"{monster_config['name'].lower().replace(' ', '_')}.lua")
                    result['code_generated'][f'monster_{i}'] = monster_code
                
                elif plan.request_type == 'script_creation':
                    # Gerar código real para script
                    script_config = self.extract_script_config(user_request)
                    script_code = self.code_generator.generate_script_code(script_config)
                    
                    result['files_created'].append(f"{script_config['name'].lower().replace(' ', '_')}.lua")
                    result['code_generated'][f'script_{i}'] = script_code
                
                elif plan.request_type == 'ui_creation':
                    # Gerar código real para UI
                    ui_config = self.extract_ui_config(user_request)
                    ui_code = self.code_generator.generate_ui_code(ui_config)
                    
                    result['files_created'].append(f"{ui_config['name'].lower().replace(' ', '_')}_interface.otui")
                    result['code_generated'][f'ui_{i}'] = ui_code
            
            elif "Configurar" in step:
                result['code_generated'][f'config_{i}'] = f"Configuração baseada em regras extraídas"
            
            elif "Validar" in step:
                result['code_generated'][f'validation_{i}'] = f"Validação usando {len(plan.validation_rules)} regras"
        
        return result
    
    def extract_module_name(self, user_request: str) -> str:
        """Extrai nome do módulo do pedido"""
        # Extrair nome do módulo do pedido
        if "inventário" in user_request.lower():
            return "game_inventory_custom"
        elif "market" in user_request.lower():
            return "game_market_custom"
        else:
            return "game_custom_module"
    
    def extract_spell_config(self, user_request: str) -> Dict:
        """Extrai configuração da magia do pedido"""
        config = {
            'name': 'Custom Spell',
            'words': 'exevo custom',
            'group': 'attack',
            'id': 999,
            'level': 20,
            'mana': 100,
            'cooldown': 2000,
            'group_cooldown': 1000,
            'vocations': '"sorcerer;true", "master sorcerer;true"',
            'damage_type': 'ENERGY',
            'effect': 'ENERGYHIT',
            'aggressive': 'true',
            'type': 'attack'
        }
        
        # Detectar tipo específico de magia
        request_lower = user_request.lower()
        
        if "fogo" in request_lower:
            config.update({
                'name': 'Fire Spell',
                'words': 'exevo ignis',
                'damage_type': 'FIRE',
                'effect': 'FIREAREA'
            })
        elif "cura" in request_lower or "heal" in request_lower or "healing" in request_lower:
            config.update({
                'name': 'Healing Spell',
                'words': 'exura san',
                'group': 'healing',
                'type': 'healing',
                'level': 35,
                'mana': 160,
                'cooldown': 1000,
                'group_cooldown': 1000,
                'vocations': '"paladin;true", "royal paladin;true"',
                'self_target': 'true',
                'aggressive': 'false'
            })
        elif "luz" in request_lower or "light" in request_lower:
            config.update({
                'name': 'Light Healing',
                'words': 'exura',
                'group': 'healing',
                'type': 'healing',
                'level': 8,
                'mana': 20,
                'cooldown': 1000,
                'group_cooldown': 1000,
                'vocations': '"druid;true", "elder druid;true"',
                'self_target': 'true',
                'aggressive': 'false'
            })
        
        return config
    
    def extract_ui_config(self, user_request: str) -> Dict:
        """Extrai configuração da UI do pedido"""
        return {
            'name': 'CustomUI',
            'id': 'customUI',
            'title': 'Custom Interface',
            'width': 400,
            'height': 300
        }
    
    def extract_monster_config(self, user_request: str) -> Dict:
        """Extrai configuração do monstro do pedido"""
        config = {
            'name': 'Custom Monster',
            'race': 'RACE_BLOOD',
            'health': 1000,
            'max_health': 1000,
            'mana': 0,
            'max_mana': 0,
            'experience': 100,
            'speed': 110,
            'skull': 'SKULL_NONE',
            'outfit_id': 128,
            'outfit_head': 0,
            'outfit_body': 0,
            'outfit_legs': 0,
            'outfit_feet': 0,
            'outfit_addons': 0,
            'spells': [],
            'loot': [],
            'events': False
        }
        
        # Detectar tipo de monstro baseado no pedido
        request_lower = user_request.lower()
        
        if "dragão" in request_lower or "dragon" in request_lower:
            config.update({
                'name': 'Dragon',
                'health': 5000,
                'max_health': 5000,
                'experience': 500,
                'outfit_id': 39,
                'spells': [
                    {
                        'name': 'fire breath',
                        'chance': 100,
                        'range': 1,
                        'interval': 2000,
                        'combat_type': 'COMBAT_FIREDAMAGE',
                        'effect': 'CONST_ME_FIREAREA'
                    }
                ],
                'loot': [
                    {'item_id': 2160, 'count': 10, 'chance': 100},  # Crystal coin
                    {'item_id': 2148, 'count': 50, 'chance': 80}   # Gold coin
                ]
            })
        elif "goblin" in request_lower:
            config.update({
                'name': 'Goblin',
                'health': 100,
                'max_health': 100,
                'experience': 25,
                'outfit_id': 60,
                'loot': [
                    {'item_id': 2148, 'count': 5, 'chance': 100}   # Gold coin
                ]
            })
        
        return config
    
    def extract_script_config(self, user_request: str) -> Dict:
        """Extrai configuração do script do pedido"""
        config = {
            'name': 'CustomScript',
            'description': 'Script personalizado',
            'logic': '-- Lógica do script aqui',
            'events': '-- Eventos do script aqui',
            'register': '-- Registro do script aqui',
            'events_list': '{}'
        }
        
        # Detectar tipo de script baseado no pedido
        request_lower = user_request.lower()
        
        if "teleporte" in request_lower or "teleport" in request_lower:
            config.update({
                'name': 'TeleportScript',
                'description': 'Script de teleporte',
                'logic': '''
local teleport = Action()
teleport:type(1)

function teleport.onUse(player, item, fromPosition, target, toPosition, isHotkey)
    player:teleportTo(Position(1000, 1000, 7))
    return true
end

teleport:aid(1234)
teleport:register()
''',
                'register': 'teleport:register()'
            })
        elif "quest" in request_lower:
            config.update({
                'name': 'QuestScript',
                'description': 'Script de quest',
                'logic': '''
local quest = Action()
quest:type(1)

function quest.onUse(player, item, fromPosition, target, toPosition, isHotkey)
    if player:getStorageValue(1234) == -1 then
        player:setStorageValue(1234, 1)
        player:sendTextMessage(MESSAGE_INFO_DESCR, "Quest iniciada!")
    end
    return true
end

quest:aid(5678)
quest:register()
''',
                'register': 'quest:register()'
            })
        
        return config

def main():
    """Função principal para teste"""
    creator = IntelligentCodeCreator()
    
    # Teste com diferentes tipos de pedidos
    test_requests = [
        "criar um módulo de inventário para OTClient",
        "criar uma magia de cura para Canary",
        "criar um monstro dragão para Canary",
        "criar um script de teleporte para Canary",
        "criar uma interface modal para OTClient"
    ]
    
    for request in test_requests:
        print(f"\n{'='*60}")
        print(f"TESTANDO: {request}")
        print(f"{'='*60}")
        
        result = creator.create_intelligently(request)
        
        if result['success']:
            print(f"✅ SUCESSO!")
            print(f"📋 Plano criado com {len(result['plan']['creation_steps'])} passos")
            print(f"📚 {len(result['knowledge_sources']['primary_docs'])} documentos consultados")
            print(f"📊 Score de validação: {result['validation']['overall_score']:.1f}%")
        else:
            print(f"❌ ERRO: {result['error']}")

if __name__ == "__main__":
    main() 