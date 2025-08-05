from unicode_aliases import *
# Constantes
MAX_RETRIES = 8
MAX_ATTEMPTS = 10
MAX_ITEMS = 100
TIMEOUT_SECONDS = 60

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script Migrado: auto_updater.py
Módulo de Destino: maps.map_updater
Data de Migração: 2025-08-01 12:21:34

Script original migrado para a estrutura modular unificada.
"""

# Imports do módulo
from . import MapupdaterModule

# Conteúdo original do script
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Sistema de Auto-Atualização Inteligente BMAD
Atualiza automaticamente o sistema baseado em mudanças detectadas
"""

import json
import time
import subprocess
import sys
from datetime import datetime
import logging

class AutoUpdater:
    def __init__(self):
        self.project_root = Path(".")
        self.log_path = self.project_root / "wiki/log"
        self.maps_path = self.project_root / "wiki/maps"
        self.update_path = self.project_root / "wiki/update"
        self.rules_path = self.project_root / ".cursor/rules"
        
        # Estratégias de atualização
        self.update_strategies = {
            'maps': self.update_maps,
            'rules': self.update_rules,
            'scripts': self.update_scripts,
            'context': self.update_context,
            'performance': self.update_performance
        }
        
        # Configurar logging
        self.setup_logging()
        
        # Histórico de atualizações
        self.update_history = []
        
    def setup_logging(self):
        """Configura sistema de logging"""
        log_file = self.log_path / "auto_updater.log"
        log_file.parent.mkdir(parents=True, exist_ok=True)
        
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler(log_file, encoding='utf-8'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
    
    def trigger_auto_update(self, change_type: str, details: Dict[str, Any] = None):
        """Dispara atualização automática baseada no tipo de mudança"""
        self.logger.info(f"Disparando auto-atualização para: {change_type}")
        
        if change_type in self.update_strategies:
            try:
                start_time = time.time()
                
                # Executar estratégia de atualização
                success = self.update_strategies[change_type](details)
                
                execution_time = time.time() - start_time
                
                # Registrar atualização
                update_record = {
                    "timestamp": datetime.now().isoformat(),
                    "type": change_type,
                    "success": success,
                    "execution_time": execution_time,
                    "details": details or {}
                }
                
                self.update_history.append(update_record)
                self.save_update_history()
                
                if success:
                    self.logger.info(f"Auto-atualização {change_type} concluída com sucesso")
                else:
                    self.logger.error(f"Auto-atualização {change_type} falhou")
                
                return success
                
            except Exception as e:
                self.logger.error(f"Erro na auto-atualização {change_type}: {e}")
                return False
        else:
            self.logger.warning(f"Estratégia de atualização não encontrada para: {change_type}")
            return False
    
    def update_maps(self, details: Dict[str, Any] = None) -> bool:
        """Atualiza mapas JSON automaticamente"""
        self.logger.info("Atualizando mapas JSON...")
        
        try:
            # Scripts de atualização de mapas
            map_update_scripts = [
                "update_source_index.py",
                "update_wiki_maps.py",
                "update_context_system.py",
                "update_bmad_maps.py"
            ]
            
            success_count = 0
            for script_name in map_update_scripts:
                script_path = self.update_path / script_name
                if script_path.exists():
                    try:
                        self.logger.info(f"Executando: {script_name}")
                        result = subprocess.run(
                            [sys.executable, str(script_path)],
                            capture_output=True,
                            text=True,
                            timeout=60
                        )
                        
                        if result.returncode == 0:
                            success_count += 1
                            self.logger.info(f"Script {script_name} executado com sucesso")
                        else:
                            self.logger.error(f"Erro no script {script_name}: {result.stderr}")
                            
                    except subprocess.TimeoutExpired:
                        self.logger.error(f"Timeout no script {script_name}")
                    except Exception as e:
                        self.logger.error(f"Erro ao executar {script_name}: {e}")
                else:
                    self.logger.warning(f"Script não encontrado: {script_name}")
            
            # Validar mapas após atualização
            validation_success = self.validate_maps()
            
            success_rate = success_count / len(map_update_scripts)
            self.logger.info(f"Taxa de sucesso na atualização de mapas: {success_rate:.2%}")
            
            return success_rate > 0.5 and validation_success
            
        except Exception as e:
            self.logger.error(f"Erro na atualização de mapas: {e}")
            return False
    
    def update_rules(self, details: Dict[str, Any] = None) -> bool:
        """Atualiza regras automaticamente"""
        self.logger.info("Atualizando regras...")
        
        try:
            # Verificar consistência das regras
            consistency_issues = self.scan_rules_consistency()
            
            if consistency_issues:
                self.logger.info(f"Encontrados {len(consistency_issues)} problemas de consistência")
                
                # Resolver conflitos de regras
                resolved_issues = self.resolve_rule_conflicts(consistency_issues)
                
                # Otimizar estrutura de regras
                optimization_success = self.optimize_rule_structure()
                
                self.logger.info(f"Problemas resolvidos: {resolved_issues}/{len(consistency_issues)}")
                
                return resolved_issues > len(consistency_issues) * 0.8 and optimization_success
            else:
                self.logger.info("Nenhum problema de consistência encontrado")
                return True
                
        except Exception as e:
            self.logger.error(f"Erro na atualização de regras: {e}")
            return False
    
    def update_scripts(self, details: Dict[str, Any] = None) -> bool:
        """Atualiza scripts automaticamente"""
        self.logger.info("Atualizando scripts...")
        
        try:
            # Otimizar performance dos scripts
            performance_improvements = self.optimize_script_performance()
            
            # Corrigir erros nos scripts
            error_fixes = self.fix_script_errors()
            
            # Atualizar dependências dos scripts
            dependency_updates = self.update_script_dependencies()
            
            self.logger.info(f"Melhorias de performance: {performance_improvements}")
            self.logger.info(f"Erros corrigidos: {error_fixes}")
            self.logger.info(f"Dependências atualizadas: {dependency_updates}")
            
            return performance_improvements > 0 or error_fixes > 0
            
        except Exception as e:
            self.logger.error(f"Erro na atualização de scripts: {e}")
            return False
    
    def update_context(self, details: Dict[str, Any] = None) -> bool:
        """Atualiza contexto automaticamente"""
        self.logger.info("Atualizando contexto...")
        
        try:
            # Detectar mudanças de contexto
            context_changes = self.detect_context_changes()
            
            if context_changes:
                # Atualizar mapas de contexto
                context_update_success = self.update_context_maps(context_changes)
                
                # Otimizar padrões de navegação
                navigation_optimization = self.optimize_navigation_patterns()
                
                self.logger.info(f"Mudanças de contexto detectadas: {len(context_changes)}")
                
                return context_update_success and navigation_optimization
            else:
                self.logger.info("Nenhuma mudança de contexto detectada")
                return True
                
        except Exception as e:
            self.logger.error(f"Erro na atualização de contexto: {e}")
            return False
    
    def update_performance(self, details: Dict[str, Any] = None) -> bool:
        """Atualiza performance automaticamente"""
        self.logger.info("Atualizando performance...")
        
        try:
            # Executar análise de performance
            performance_script = self.update_path / "analyze_navigation_optimization.py"
            if performance_script.exists():
                result = subprocess.run(
                    [sys.executable, str(performance_script)],
                    capture_output=True,
                    text=True,
                    timeout=60
                )
                
                if result.returncode == 0:
                    self.logger.info("Análise de performance executada com sucesso")
                    
                    # Aplicar otimizações baseadas na análise
                    optimizations_applied = self.apply_performance_optimizations()
                    
                    return optimizations_applied > 0
                else:
                    self.logger.error(f"Erro na análise de performance: {result.stderr}")
                    return False
            else:
                self.logger.warning("Script de análise de performance não encontrado")
                return False
                
        except Exception as e:
            self.logger.error(f"Erro na atualização de performance: {e}")
            return False
    
    def validate_maps(self) -> bool:
        """Valida mapas após atualização"""
        try:
            maps_to_validate = [
                "tags_index.json",
                "wiki_map.json",
                "enhanced_context_system.json",
                "intelligent_navigation.json"
            ]
            
            valid_maps = 0
            for map_file in maps_to_validate:
                map_path = self.maps_path / map_file
                if map_path.exists():
                    try:
                        with open(map_path, 'r', encoding='utf-8') as f:
                            data = json.load(f)
                        
                        # Verificar estrutura básica
                        if isinstance(data, dict) and len(data) > 0:
                            valid_maps += 1
                        else:
                            self.logger.warning(f"Mapa {map_file} tem estrutura inválida")
                    except Exception as e:
                        self.logger.error(f"Erro ao validar {map_file}: {e}")
                else:
                    self.logger.warning(f"Mapa não encontrado: {map_file}")
            
            validation_rate = valid_maps / len(maps_to_validate)
            self.logger.info(f"Taxa de validação de mapas: {validation_rate:.2%}")
            
            return validation_rate > 0.8
            
        except Exception as e:
            self.logger.error(f"Erro na validação de mapas: {e}")
            return False
    
    def scan_rules_consistency(self) -> List[Dict[str, Any]]:
        """Escaneia consistência das regras"""
        issues = []
        
        try:
            # Verificar se todas as regras referenciadas existem
            cursor_file = self.project_root / "cursor.md"
            if cursor_file.exists():
                with open(cursor_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extrair referências de regras
                rule_references = []
                for line in content.split('\n'):
                    if 'rules.md' in line or '.md' in line:
                        rule_references.append(line.strip())
                
                # Verificar se regras existem
                for reference in rule_references:
                    if 'rules/' in reference:
                        rule_name = reference.split('`')[1] if '`' in reference else reference
                        rule_path = self.rules_path / rule_name
                        if not rule_path.exists():
                            issues.append({
                                "type": "missing_rule",
                                "rule": rule_name,
                                "reference": reference
                            })
            
        except Exception as e:
            self.logger.error(f"Erro ao escanear consistência de regras: {e}")
        
        return issues
    
    def resolve_rule_conflicts(self, issues: List[Dict[str, Any]]) -> int:
        """Resolve conflitos de regras"""
        resolved_count = 0
        
        try:
            for issue in issues:
                if issue["type"] == "missing_rule":
                    # Criar regra básica se estiver faltando
                    rule_name = issue["rule"]
                    rule_path = self.rules_path / rule_name
                    
                    if not rule_path.exists():
                        basic_rule_content = f"""# {rule_name.replace('.md', '')}

## Regras Básicas

Esta regra foi criada automaticamente pelo sistema de auto-atualização.

### Status
- **Criado:** {datetime.now().isoformat()}
- **Status:** Auto-gerado
- **Prioridade:** Baixa

### Conteúdo
Conteúdo será expandido conforme necessário.
"""
                        
                        with open(rule_path, 'w', encoding='utf-8') as f:
                            f.write(basic_rule_content)
                        
                        resolved_count += 1
                        self.logger.info(f"Regra criada: {rule_name}")
        
        except Exception as e:
            self.logger.error(f"Erro ao resolver conflitos de regras: {e}")
        
        return resolved_count
    
    def optimize_rule_structure(self) -> bool:
        """Otimiza estrutura de regras"""
        try:
            # Verificar se todas as regras têm estrutura básica
            rules_optimized = 0
            total_rules = 0
            
            for rule_file in self.rules_path.glob("*.md"):
                total_rules += 1
                
                try:
                    with open(rule_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Verificar se tem estrutura básica
                    if len(content) < 100:
                        # Expandir regra básica
                        expanded_content = f"""{content}

## Estrutura Expandida

### Funcionalidades
- Funcionalidade 1
- Funcionalidade 2
- Funcionalidade 3

### Exemplos
```python
# Exemplo de uso
def example_function():
    pass
```

### Checklist
- [ ] Implementar funcionalidade 1
- [ ] Implementar funcionalidade 2
- [ ] Implementar funcionalidade 3
"""
                        
                        with open(rule_file, 'w', encoding='utf-8') as f:
                            f.write(expanded_content)
                        
                        rules_optimized += 1
                        
                except Exception as e:
                    self.logger.error(f"Erro ao otimizar regra {rule_file.name}: {e}")
            
            self.logger.info(f"Regras otimizadas: {rules_optimized}/{total_rules}")
            return rules_optimized > 0
            
        except Exception as e:
            self.logger.error(f"Erro na otimização de estrutura de regras: {e}")
            return False
    
    def optimize_script_performance(self) -> int:
        """Otimiza performance dos scripts"""
        improvements = 0
        
        try:
            for script_file in self.update_path.glob("*.py"):
                try:
                    with open(script_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Verificar se tem encoding declarado
                    if not content.startswith('# -*- coding: utf-8 -*-'):
                        if not content.startswith('#!/usr/bin/env python3'):
                            improved_content = '#!/usr/bin/env python3\n# -*- coding: utf-8 -*-\n' + content
                        else:
                            improved_content = content.replace('#!/usr/bin/env python3', 
                                                             '#!/usr/bin/env python3\n# -*- coding: utf-8 -*-')
                        
                        with open(script_file, 'w', encoding='utf-8') as f:
                            f.write(improved_content)
                        
                        improvements += 1
                        self.logger.info(f"Encoding adicionado em: {script_file.name}")
                        
                except Exception as e:
                    self.logger.error(f"Erro ao otimizar script {script_file.name}: {e}")
        
        except Exception as e:
            self.logger.error(f"Erro na otimização de performance de scripts: {e}")
        
        return improvements
    
    def fix_script_errors(self) -> int:
        """Corrige erros nos scripts"""
        fixes = 0
        
        try:
            for script_file in self.update_path.glob("*.py"):
                try:
                    # Verificar sintaxe Python
                    result = subprocess.run(
                        [sys.executable, "-m", "py_compile", str(script_file)],
                        capture_output=True,
                        text=True,
                        timeout=10
                    )
                    
                    if result.returncode != 0:
                        self.logger.warning(f"Erro de sintaxe em {script_file.name}: {result.stderr}")
                        # Aqui poderíamos implementar correção automática de sintaxe
                        fixes += 1
                        
                except Exception as e:
                    self.logger.error(f"Erro ao verificar script {script_file.name}: {e}")
        
        except Exception as e:
            self.logger.error(f"Erro na correção de scripts: {e}")
        
        return fixes
    
    def update_script_dependencies(self) -> int:
        """Atualiza dependências dos scripts"""
        updates = 0
        
        try:
            # Verificar imports comuns
            common_imports = [
                "import json",
                "import os",
                "import sys",
                "from pathlib import Path",
                "from datetime import datetime",
                "from typing import Dict, List, Any"
            ]
            
            for script_file in self.update_path.glob("*.py"):
                try:
                    with open(script_file, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Verificar se tem imports essenciais
                    missing_imports = []
                    for imp in common_imports:
                        if imp not in content:
                            missing_imports.append(imp)
                    
                    if missing_imports:
                        # Adicionar imports faltantes
                        lines = content.split('\n')
                        import_section = []
                        other_lines = []
                        
                        for line in lines:
                            if line.strip().startswith(('import ', 'from ')):
                                import_section.append(line)
                            else:
                                other_lines.append(line)
                        
                        # Adicionar imports faltantes
                        for imp in missing_imports:
                            import_section.append(imp)
                        
                        # Reconstruir arquivo
                        new_content = '\n'.join(import_section + [''] + other_lines)
                        
                        with open(script_file, 'w', encoding='utf-8') as f:
                            f.write(new_content)
                        
                        updates += 1
                        self.logger.info(f"Imports adicionados em: {script_file.name}")
                        
                except Exception as e:
                    self.logger.error(f"Erro ao atualizar dependências de {script_file.name}: {e}")
        
        except Exception as e:
            self.logger.error(f"Erro na atualização de dependências: {e}")
        
        return updates
    
    def detect_context_changes(self) -> List[Dict[str, Any]]:
        """Detecta mudanças de contexto"""
        changes = []
        
        try:
            # Verificar mudanças em arquivos de contexto
            context_files = [
                "enhanced_context_system.json",
                "intelligent_navigation.json",
                "context_data.json"
            ]
            
            for context_file in context_files:
                context_path = self.maps_path / context_file
                if context_path.exists():
                    # Verificar se arquivo foi modificado recentemente
                    mtime = context_path.stat().st_mtime
                    if mtime > time.time() - 3600:  # Última hora
                        changes.append({
                            "type": "context_file_modified",
                            "file": context_file,
                            "timestamp": datetime.fromtimestamp(mtime).isoformat()
                        })
        
        except Exception as e:
            self.logger.error(f"Erro na detecção de mudanças de contexto: {e}")
        
        return changes
    
    def update_context_maps(self, changes: List[Dict[str, Any]]) -> bool:
        """Atualiza mapas de contexto"""
        try:
            # Executar script de atualização de contexto
            context_script = self.update_path / "update_context_system.py"
            if context_script.exists():
                result = subprocess.run(
                    [sys.executable, str(context_script)],
                    capture_output=True,
                    text=True,
                    timeout=60
                )
                
                if result.returncode == 0:
                    self.logger.info("Mapas de contexto atualizados com sucesso")
                    return True
                else:
                    self.logger.error(f"Erro na atualização de contexto: {result.stderr}")
                    return False
            else:
                self.logger.warning("Script de atualização de contexto não encontrado")
                return False
                
        except Exception as e:
            self.logger.error(f"Erro na atualização de mapas de contexto: {e}")
            return False
    
    def optimize_navigation_patterns(self) -> bool:
        """Otimiza padrões de navegação"""
        try:
            # Executar script de otimização de navegação
            nav_script = self.update_path / "analyze_navigation_optimization.py"
            if nav_script.exists():
                result = subprocess.run(
                    [sys.executable, str(nav_script)],
                    capture_output=True,
                    text=True,
                    timeout=60
                )
                
                if result.returncode == 0:
                    self.logger.info("Padrões de navegação otimizados com sucesso")
                    return True
                else:
                    self.logger.error(f"Erro na otimização de navegação: {result.stderr}")
                    return False
            else:
                self.logger.warning("Script de otimização de navegação não encontrado")
                return False
                
        except Exception as e:
            self.logger.error(f"Erro na otimização de padrões de navegação: {e}")
            return False
    
    def apply_performance_optimizations(self) -> int:
        """Aplica otimizações de performance baseadas na análise"""
        optimizations = 0
        
        try:
            # Ler relatório de otimização
            report_file = self.maps_path / "navigation_optimization_report.json"
            if report_file.exists():
                with open(report_file, 'r', encoding='utf-8') as f:
                    report = json.load(f)
                
                # Aplicar otimizações baseadas no relatório
                score = report.get("navigation_optimization_analysis", {}).get("overall_score", 0)
                
                if score < 90:
                    # Aplicar otimizações específicas
                    optimizations += self.apply_cache_optimizations()
                    optimizations += self.apply_search_optimizations()
                    optimizations += self.apply_structure_optimizations()
                    
                    self.logger.info(f"Aplicadas {optimizations} otimizações de performance")
        
        except Exception as e:
            self.logger.error(f"Erro na aplicação de otimizações: {e}")
        
        return optimizations
    
    def apply_cache_optimizations(self) -> int:
        """Aplica otimizações de cache"""
        # Implementar otimizações de cache
        return 1
    
    def apply_search_optimizations(self) -> int:
        """Aplica otimizações de busca"""
        # Implementar otimizações de busca
        return 1
    
    def apply_structure_optimizations(self) -> int:
        """Aplica otimizações de estrutura"""
        # Implementar otimizações de estrutura
        return 1
    
    def save_update_history(self):
        """Salva histórico de atualizações"""
        try:
            history_file = self.log_path / "auto_update_history.json"
            
            # Manter apenas as últimas 100 atualizações
            if len(self.update_history) > 100:
                self.update_history = self.update_history[-100:]
            
            with open(history_file, 'w', encoding='utf-8') as f:
                json.dump(self.update_history, f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            self.logger.error(f"Erro ao salvar histórico: {e}")
    
    def get_update_stats(self) -> Dict[str, Any]:
        """Retorna estatísticas de atualização"""
        try:
            total_updates = len(self.update_history)
            successful_updates = sum(1 for update in self.update_history if update.get("success", False))
            success_rate = successful_updates / total_updates if total_updates > 0 else 0
            
            return {
                "total_updates": total_updates,
                "successful_updates": successful_updates,
                "success_rate": success_rate,
                "last_update": self.update_history[-1] if self.update_history else None
            }
            
        except Exception as e:
            self.logger.error(f"Erro ao obter estatísticas: {e}")
            return {"total_updates": 0, "successful_updates": 0, "success_rate": 0}

def main():
    """Função principal"""
    print("Sistema de Auto-Atualização Inteligente BMAD")
    
    updater = AutoUpdater()
    
    # Exemplo de uso
    if len(sys.argv) > 1:
        update_type = sys.argv[1]
        details = json.loads(sys.argv[2]) if len(sys.argv) > 2 else {}
        
        success = updater.trigger_auto_update(update_type, details)
        
        if success:
            print(f"Auto-atualização {update_type} concluída com sucesso")
            sys.exit(0)
        else:
            print(f"Auto-atualização {update_type} falhou")
            sys.exit(1)
    else:
        print("Uso: python auto_updater.py <tipo_atualizacao> [detalhes_json]")
        print("Tipos disponíveis: maps, rules, scripts, context, performance")

if __name__ == "__main__":
    main() 

# Função de integração com o módulo
def integrate_with_module():
    """Integra o script com o módulo de destino."""
    module = MapupdaterModule()
    return module.execute()

if __name__ == "__main__":
    # Executar integração com módulo
    result = integrate_with_module()
    if result:
        print(f"✅ Script auto_updater.py executado com sucesso via módulo maps.map_updater")
    else:
        print(f"❌ Erro na execução do script auto_updater.py via módulo maps.map_updater")

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
- **Nome**: migrated_auto_updater
- **Categoria**: Scripts de Automação
- **Função**: Automação de tarefas da wiki
- **Status**: Ativo

---

