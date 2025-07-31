#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🤖 Module Creator Agent
Responsável por criar módulos OTClient do zero baseado na wiki
"""
import os
import json
import re
import random
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime
from itertools import count

class ModuleCreatorAgent:
    def __init__(self, workspace_path: str = None):
        self.workspace_path = workspace_path or os.getcwd()
        # Ajustar caminho para encontrar módulos na raiz do projeto
        if os.path.basename(self.workspace_path) == "bmad":
            # Se estamos na pasta bmad, subir um nível
            self.workspace_path = os.path.dirname(self.workspace_path)
        if os.path.basename(self.workspace_path) == "wiki":
            # Se estamos na pasta wiki, subir um nível
            self.workspace_path = os.path.dirname(self.workspace_path)
        
        self.modules_path = os.path.join(self.workspace_path, "modules")
        self.wiki_path = os.path.join(self.workspace_path, "wiki")
        self.results_path = os.path.join(self.workspace_path, "wiki/bmad/results")
        
        # Criar diretórios se não existirem
        os.makedirs(self.results_path, exist_ok=True)
        os.makedirs(os.path.join(self.results_path, "created_modules"), exist_ok=True)
        
        # Carregar mapas da wiki
        self.load_wiki_maps()
        
    def load_wiki_maps(self):
        """Carrega mapas da wiki para navegação inteligente"""
        try:
            maps_path = os.path.join(self.wiki_path, "maps")
            
            # Carregar índice de tags
            tags_file = os.path.join(maps_path, "tags_index.json")
            if os.path.exists(tags_file):
                with open(tags_file, 'r', encoding='utf-8') as f:
                    self.tags_index = json.load(f)
            else:
                self.tags_index = {}
                
            # Carregar mapa da wiki
            wiki_map_file = os.path.join(maps_path, "wiki_map.json")
            if os.path.exists(wiki_map_file):
                with open(wiki_map_file, 'r', encoding='utf-8') as f:
                    self.wiki_map = json.load(f)
            else:
                self.wiki_map = {}
                
        except Exception as e:
            print(f"⚠️ Erro ao carregar mapas da wiki: {e}")
            self.tags_index = {}
            self.wiki_map = {}
    
    def analyze_existing_game_modules(self) -> Dict[str, Any]:
        """Analisa módulos game_ existentes para entender padrões"""
        game_modules = {}
        
        try:
            for item in os.listdir(self.modules_path):
                if item.startswith("game_") and os.path.isdir(os.path.join(self.modules_path, item)):
                    module_path = os.path.join(self.modules_path, item)
                    game_modules[item] = self.analyze_single_module(module_path)
                    
        except Exception as e:
            print(f"⚠️ Erro ao analisar módulos game_: {e}")
            
        return game_modules
    
    def analyze_single_module(self, module_path: str) -> Dict[str, Any]:
        """Analisa um módulo específico"""
        analysis = {
            "path": module_path,
            "files": {},
            "structure": {},
            "patterns": {}
        }
        
        try:
            for file_name in os.listdir(module_path):
                file_path = os.path.join(module_path, file_name)
                if os.path.isfile(file_path):
                    file_ext = os.path.splitext(file_name)[1]
                    analysis["files"][file_name] = {
                        "path": file_path,
                        "size": os.path.getsize(file_path),
                        "extension": file_ext
                    }
                    
                    # Analisar conteúdo de arquivos principais
                    if file_ext in ['.lua', '.otmod', '.otui']:
                        analysis["files"][file_name]["content"] = self.analyze_file_content(file_path, file_ext)
                        
        except Exception as e:
            print(f"⚠️ Erro ao analisar módulo {module_path}: {e}")
            
        return analysis
    
    def analyze_file_content(self, file_path: str, file_ext: str) -> Dict[str, Any]:
        """Analisa conteúdo de um arquivo"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                
            analysis = {
                "lines": len(content.split('\n')),
                "size": len(content),
                "patterns": {}
            }
            
            if file_ext == '.lua':
                analysis["patterns"] = self.analyze_lua_patterns(content)
            elif file_ext == '.otmod':
                analysis["patterns"] = self.analyze_otmod_patterns(content)
            elif file_ext == '.otui':
                analysis["patterns"] = self.analyze_otui_patterns(content)
                
            return analysis
            
        except Exception as e:
            print(f"⚠️ Erro ao analisar arquivo {file_path}: {e}")
            return {}
    
    def analyze_lua_patterns(self, content: str) -> Dict[str, Any]:
        """Analisa padrões em arquivos Lua"""
        patterns = {
            "functions": [],
            "variables": [],
            "events": [],
            "ui_references": [],
            "api_calls": []
        }
        
        # Extrair funções
        function_pattern = r'function\s+(\w+)\s*\('
        patterns["functions"] = re.findall(function_pattern, content)
        
        # Extrair variáveis
        var_pattern = r'local\s+(\w+)\s*='
        patterns["variables"] = re.findall(var_pattern, content)
        
        # Extrair eventos
        event_pattern = r'connect\s*\(\s*(\w+)\s*,'
        patterns["events"] = re.findall(event_pattern, content)
        
        # Extrair referências UI
        ui_pattern = r'g_ui\.(\w+)'
        patterns["ui_references"] = re.findall(ui_pattern, content)
        
        # Extrair chamadas de API
        api_pattern = r'g_game\.(\w+)'
        patterns["api_calls"] = re.findall(api_pattern, content)
        
        return patterns
    
    def analyze_otmod_patterns(self, content: str) -> Dict[str, Any]:
        """Analisa padrões em arquivos OTMod"""
        patterns = {
            "name": "",
            "description": "",
            "author": "",
            "scripts": [],
            "events": []
        }
        
        # Extrair nome
        name_match = re.search(r'name:\s*(.+)', content)
        if name_match:
            patterns["name"] = name_match.group(1).strip()
            
        # Extrair descrição
        desc_match = re.search(r'description:\s*(.+)', content)
        if desc_match:
            patterns["description"] = desc_match.group(1).strip()
            
        # Extrair autor
        author_match = re.search(r'author:\s*(.+)', content)
        if author_match:
            patterns["author"] = author_match.group(1).strip()
            
        # Extrair scripts
        scripts_match = re.search(r'scripts:\s*\[(.*?)\]', content)
        if scripts_match:
            scripts_str = scripts_match.group(1)
            patterns["scripts"] = [s.strip() for s in scripts_str.split(',') if s.strip()]
            
        # Extrair eventos
        event_pattern = r'@(\w+):\s*(.+)'
        patterns["events"] = re.findall(event_pattern, content)
        
        return patterns
    
    def analyze_otui_patterns(self, content: str) -> Dict[str, Any]:
        """Analisa padrões em arquivos OTUI"""
        patterns = {
            "widgets": [],
            "layouts": [],
            "styles": []
        }
        
        # Extrair widgets
        widget_pattern = r'(\w+)\s*<'
        patterns["widgets"] = list(set(re.findall(widget_pattern, content)))
        
        # Extrair layouts
        layout_pattern = r'layout:\s*(\w+)'
        patterns["layouts"] = re.findall(layout_pattern, content)
        
        # Extrair estilos
        style_pattern = r'style:\s*(\w+)'
        patterns["styles"] = re.findall(style_pattern, content)
        
        return patterns
    
    def search_wiki_knowledge(self, query: str) -> List[Dict[str, Any]]:
        """Busca conhecimento na wiki"""
        results = []
        
        try:
            # Buscar em arquivos da wiki baseado em tags
            for file_path, tags in self.tags_index.items():
                if any(tag.lower() in query.lower() for tag in tags):
                    full_path = os.path.join(self.wiki_path, file_path)
                    if os.path.exists(full_path):
                        with open(full_path, 'r', encoding='utf-8') as f:
                            content = f.read()
                            results.append({
                                "file": file_path,
                                "content": content[:500],  # Primeiros 500 chars
                                "tags": tags
                            })
                            
        except Exception as e:
            print(f"⚠️ Erro ao buscar na wiki: {e}")
            
        return results
    
    def generate_module_concept(self) -> Dict[str, Any]:
        """Gera conceito para novo módulo baseado na wiki"""
        # Buscar conhecimento sobre módulos na wiki
        wiki_knowledge = self.search_wiki_knowledge("módulo game interface")
        
        # Conceitos possíveis para módulos game_
        concepts = [
            {
                "name": "game_achievements",
                "description": "Sistema de conquistas e progresso do jogador",
                "features": ["Lista de conquistas", "Progresso visual", "Recompensas", "Notificações"]
            },
            {
                "name": "game_automap_enhanced",
                "description": "Mapa automático aprimorado com marcadores e filtros",
                "features": ["Marcadores personalizados", "Filtros de criaturas", "Rotas salvas", "Zoom avançado"]
            },
            {
                "name": "game_combat_analyzer",
                "description": "Analisador de combate com estatísticas em tempo real",
                "features": ["DPS tracker", "Análise de dano", "Histórico de combate", "Gráficos"]
            },
            {
                "name": "game_party_manager",
                "description": "Gerenciador de grupo com ferramentas avançadas",
                "features": ["Lista de membros", "Distribuição de loot", "Comunicação", "Status do grupo"]
            },
            {
                "name": "game_equipment_planner",
                "description": "Planejador de equipamentos com comparações",
                "features": ["Comparação de itens", "Sets de equipamento", "Recomendações", "Simulador"]
            }
        ]
        
        # Escolher conceito aleatório
        chosen_concept = random.choice(concepts)
        
        return {
            "concept": chosen_concept,
            "wiki_knowledge": wiki_knowledge,
            "creation_time": datetime.now().isoformat()
        }
    
    def create_module_structure(self, concept: Dict[str, Any]) -> Dict[str, Any]:
        """Cria estrutura do módulo baseada no conceito"""
        module_name = concept["name"]
        module_path = os.path.join(self.modules_path, module_name)
        
        # Criar diretório do módulo
        os.makedirs(module_path, exist_ok=True)
        
        # Gerar arquivos do módulo
        files_created = {}
        
        # 1. Arquivo .otmod
        otmod_content = self.generate_otmod_content(concept)
        otmod_file = os.path.join(module_path, f"{module_name.split('_', 1)[1]}.otmod")
        with open(otmod_file, 'w', encoding='utf-8') as f:
            f.write(otmod_content)
        files_created["otmod"] = otmod_file
        
        # 2. Arquivo .lua
        lua_content = self.generate_lua_content(concept)
        lua_file = os.path.join(module_path, f"{module_name.split('_', 1)[1]}.lua")
        with open(lua_file, 'w', encoding='utf-8') as f:
            f.write(lua_content)
        files_created["lua"] = lua_file
        
        # 3. Arquivo .otui
        otui_content = self.generate_otui_content(concept)
        otui_file = os.path.join(module_path, f"{module_name.split('_', 1)[1]}.otui")
        with open(otui_file, 'w', encoding='utf-8') as f:
            f.write(otui_content)
        files_created["otui"] = otui_file
        
        return {
            "module_path": module_path,
            "files_created": files_created,
            "concept": concept
        }
    
    def generate_otmod_content(self, concept: Dict[str, Any]) -> str:
        """Gera conteúdo do arquivo .otmod"""
        module_name = concept["name"]
        script_name = module_name.split('_', 1)[1]
        
        content = f"""Module
  name: {module_name}
  description: {concept["description"]}
  author: BMAD AI Agent
  website: https://github.com/edubart/otclient
  sandboxed: true
  scripts: [ {script_name} ]
  @onLoad: {script_name}Controller:init()
  @onUnload: {script_name}Controller:terminate()
"""
        return content
    
    def generate_lua_content(self, concept: Dict[str, Any]) -> str:
        """Gera conteúdo do arquivo .lua"""
        module_name = concept["name"]
        script_name = module_name.split('_', 1)[1]
        controller_name = f"{script_name}Controller"
        
        content = f"""-- {concept["description"]}
-- Criado automaticamente pelo BMAD AI Agent

{script_name}Window = nil
{script_name}Button = nil
{script_name}Settings = nil

function init()
    connect(LocalPlayer, {{
        onExperienceChange = onExperienceChange,
        onLevelChange = onLevelChange,
        onHealthChange = onHealthChange,
        onManaChange = onManaChange
    }})
    connect(g_game, {{
        onGameStart = online,
        onGameEnd = offline
    }})

    {script_name}Button = modules.game_mainpanel.addToggleButton('{script_name}Button', tr('{concept["name"].replace("_", " ").title()}') .. ' (Alt+{script_name[0].upper()})',
                                                                   '/images/options/button_{script_name}', toggle, false, 1)
    {script_name}Button:setOn(true)
    {script_name}Window = g_ui.loadUI('{script_name}')

    Keybind.new("Windows", "Show/hide {script_name} window", "Alt+{script_name[0].upper()}", "")
    Keybind.bind("Windows", "Show/hide {script_name} window", {{
      {{
        type = KEY_DOWN,
        callback = toggle,
      }}
    }})

    {script_name}Settings = g_settings.getNode('{script_name}-hide')
    if not {script_name}Settings then
        {script_name}Settings = {{}}
    end

    refresh()
    {script_name}Window:setup()
    if g_game.isOnline() then
        {script_name}Window:setupOnStart()
    end
end

function terminate()
    disconnect(LocalPlayer, {{
        onExperienceChange = onExperienceChange,
        onLevelChange = onLevelChange,
        onHealthChange = onHealthChange,
        onManaChange = onManaChange
    }})
    disconnect(g_game, {{
        onGameStart = online,
        onGameEnd = offline
    }})

    Keybind.delete("Windows", "Show/hide {script_name} window")
    {script_name}Window:destroy()
    {script_name}Button:destroy()

    {script_name}Window = nil
    {script_name}Button = nil
end

function toggle()
    if {script_name}Window:isVisible() then
        {script_name}Window:hide()
        {script_name}Button:setOn(false)
    else
        {script_name}Window:show()
        {script_name}Window:focus()
        {script_name}Button:setOn(true)
    end
end

function refresh()
    if not {script_name}Window then
        return
    end
    
    -- Implementar lógica de refresh específica do módulo
    if g_game.isOnline() then
        update{script_name.title()}Data()
    end
end

function update{script_name.title()}Data()
    -- Implementar atualização de dados do módulo
    if not g_game.isOnline() then
        return
    end
    
            -- Exemplo de implementação
        local player = g_game.getLocalPlayer()
        if player then
            -- Atualizar dados baseados no conceito do módulo
            -- Implementar cada feature do módulo
        end
end

function online()
    refresh()
end

function offline()
    -- Limpar dados quando desconectar
end

function onExperienceChange(localPlayer, exp)
    refresh()
end

function onLevelChange(localPlayer, level)
    refresh()
end

function onHealthChange(localPlayer, health, maxHealth)
    refresh()
end

function onManaChange(localPlayer, mana, maxMana)
    refresh()
end
"""
        return content
    
    def generate_otui_content(self, concept: Dict[str, Any]) -> str:
        """Gera conteúdo do arquivo .otui"""
        module_name = concept["name"]
        script_name = module_name.split('_', 1)[1]
        
        content = f"""-- {concept["description"]}
-- Interface criada automaticamente pelo BMAD AI Agent

{script_name}Window < MainWindow
  id: {script_name}Window
  size: 400 300
  @onEscape: self:close()
  
  Panel
    id: mainPanel
    anchors.fill: parent
    layout: verticalBox
    
    Panel
      id: titlePanel
      height: 30
      layout: horizontalBox
      margin: 5
      
      Label
        id: titleLabel
        text: tr('{concept["name"].replace("_", " ").title()}')
        font: verdana-11px-antialised
        color: white
        anchors.verticalCenter: parent.verticalCenter
        
      Button
        id: closeButton
        text: "X"
        width: 20
        height: 20
        anchors.right: parent.right
        anchors.verticalCenter: parent.verticalCenter
        @onClick: parent.parent.parent:close()
    
    Panel
      id: contentPanel
      layout: verticalBox
      margin: 10
      
      Label
        id: descriptionLabel
        text: tr('{concept["description"]}')
        font: verdana-10px-antialised
        color: #cccccc
        text-wrap: true
        margin-bottom: 10
      
      Panel
        id: featuresPanel
        layout: verticalBox
        
        Label
          id: featuresTitle
          text: tr('Funcionalidades:')
          font: verdana-11px-antialised
          color: white
          margin-bottom: 5
        
        ScrollablePanel
          id: featuresList
          layout: verticalBox
          height: 150
          margin: 5
          
          -- Lista de features será preenchida dinamicamente
"""
        
        # Adicionar features como labels
        for i, feature in zip(count(1), concept["features"]):
            content += f"""
          Label
            id: feature{i}
            text: tr('• {feature}')
            font: verdana-10px-antialised
            color: #aaaaaa
            margin: 2
"""
        
        content += f"""
      
      Panel
        id: statusPanel
        layout: horizontalBox
        margin-top: 10
        
        Label
          id: statusLabel
          text: tr('Status: Pronto')
          font: verdana-10px-antialised
          color: #00ff00
          anchors.verticalCenter: parent.verticalCenter
        
        Button
          id: refreshButton
          text: tr('Atualizar')
          width: 80
          height: 25
          anchors.right: parent.right
          anchors.verticalCenter: parent.verticalCenter
          @onClick: refresh()
"""
        
        return content
    
    def create_module_from_scratch(self) -> Dict[str, Any]:
        """Cria um módulo completo do zero baseado na wiki"""
        print("🤖 Iniciando criação de módulo do zero...")
        
        # 1. Analisar módulos existentes para entender padrões
        print("📊 Analisando módulos game_ existentes...")
        existing_modules = self.analyze_existing_game_modules()
        
        # 2. Gerar conceito baseado na wiki
        print("💡 Gerando conceito baseado na wiki...")
        concept_data = self.generate_module_concept()
        
        # 3. Criar estrutura do módulo
        print("🏗️ Criando estrutura do módulo...")
        module_structure = self.create_module_structure(concept_data["concept"])
        
        # 4. Salvar relatório
        report = {
            "creation_time": datetime.now().isoformat(),
            "concept": concept_data["concept"],
            "module_structure": module_structure,
            "existing_modules_analyzed": len(existing_modules),
            "wiki_knowledge_used": len(concept_data["wiki_knowledge"])
        }
        
        report_file = os.path.join(self.results_path, "created_modules", f"{concept_data['concept']['name']}_creation_report.json")
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Módulo criado com sucesso: {concept_data['concept']['name']}")
        print(f"📁 Localização: {module_structure['module_path']}")
        print(f"📄 Arquivos criados: {list(module_structure['files_created'].keys())}")
        
        return {
            "success": True,
            "module_name": concept_data["concept"]["name"],
            "module_path": module_structure["module_path"],
            "files_created": module_structure["files_created"],
            "report_file": report_file
        }

if __name__ == "__main__":
    creator = ModuleCreatorAgent()
    result = creator.create_module_from_scratch()
    print(f"Resultado: {result}") 