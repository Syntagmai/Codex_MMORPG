#!/usr/bin/env python3
"""
Configuration Correction Agent - Epic 18 Task 18.6
Corrige configurações obsoletas e parâmetros inconsistentes identificados na Epic 17
"""
import os
import json
import re
import shutil
from datetime import datetime
from pathlib import Path

class ConfigCorrectionAgent:
    def __init__(self, project_root):
        self.project_root = Path(project_root)
        self.audit_reports_dir = self.project_root / "wiki" / "docs" / "audit_reports"
        self.config_report = self.audit_reports_dir / "config_audit_report.json"
        self.correction_report = {
            "timestamp": datetime.now().isoformat(),
            "obsolete_configs_fixed": [],
            "inconsistent_params_fixed": [],
            "config_files_updated": [],
            "backup_files_created": [],
            "new_configs_created": [],
            "validation_rules_added": [],
            "total_fixes": 0
        }
    
    def load_config_audit(self):
        """Carrega o relatório de auditoria de configuração"""
        try:
            with open(self.config_report, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Erro ao carregar relatório de configuração: {e}")
            return None
    
    def backup_file(self, file_path):
        """Cria backup de um arquivo antes de modificá-lo"""
        try:
            backup_path = str(file_path) + ".backup"
            shutil.copy2(file_path, backup_path)
            self.correction_report["backup_files_created"].append(backup_path)
            return True
        except Exception as e:
            print(f"Erro ao criar backup de {file_path}: {e}")
            return False
    
    def fix_obsolete_configs(self, obsolete_configs):
        """Corrige configurações obsoletas"""
        fixes = []
        
        for config in obsolete_configs:
            file_path = config.get('file_path', '')
            config_type = config.get('config_type', '')
            description = config.get('description', '')
            
            if not file_path or not os.path.exists(file_path):
                continue
            
            try:
                # Backup do arquivo
                self.backup_file(file_path)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Correções específicas por tipo de configuração
                if "json" in config_type.lower():
                    content = self.fix_json_config(content, config)
                elif "yaml" in config_type.lower():
                    content = self.fix_yaml_config(content, config)
                elif "ini" in config_type.lower():
                    content = self.fix_ini_config(content, config)
                elif "env" in config_type.lower():
                    content = self.fix_env_config(content, config)
                else:
                    content = self.fix_generic_config(content, config)
                
                # Salva mudanças se houve alteração
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    fixes.append({
                        "file": file_path,
                        "config_type": config_type,
                        "description": description,
                        "fix_applied": "Obsolete configuration updated"
                    })
                    
                    self.correction_report["config_files_updated"].append(file_path)
                    
            except Exception as e:
                print(f"Erro ao corrigir configuração obsoleta em {file_path}: {e}")
        
        self.correction_report["obsolete_configs_fixed"] = fixes
        return fixes
    
    def fix_json_config(self, content, config):
        """Corrige configuração JSON"""
        try:
            # Tenta fazer parse do JSON
            data = json.loads(content)
            
            # Remove campos obsoletos
            obsolete_fields = config.get('obsolete_fields', [])
            for field in obsolete_fields:
                if field in data:
                    del data[field]
            
            # Atualiza valores obsoletos
            obsolete_values = config.get('obsolete_values', {})
            for key, value in obsolete_values.items():
                if key in data and data[key] == value['old']:
                    data[key] = value['new']
            
            # Adiciona campos padrão se não existirem
            default_fields = config.get('default_fields', {})
            for key, value in default_fields.items():
                if key not in data:
                    data[key] = value
            
            return json.dumps(data, indent=2, ensure_ascii=False)
            
        except json.JSONDecodeError:
            # Se não for JSON válido, trata como texto
            return self.fix_generic_config(content, config)
    
    def fix_yaml_config(self, content, config):
        """Corrige configuração YAML"""
        # Remove linhas obsoletas
        obsolete_lines = config.get('obsolete_lines', [])
        for line in obsolete_lines:
            content = content.replace(line, '')
        
        # Substitui valores obsoletos
        obsolete_values = config.get('obsolete_values', {})
        for old_value, new_value in obsolete_values.items():
            content = content.replace(old_value, new_value)
        
        # Adiciona configurações padrão
        default_config = config.get('default_config', '')
        if default_config and default_config not in content:
            content += '\n' + default_config
        
        return content
    
    def fix_ini_config(self, content, config):
        """Corrige configuração INI"""
        # Remove seções obsoletas
        obsolete_sections = config.get('obsolete_sections', [])
        for section in obsolete_sections:
            section_pattern = rf'\[{re.escape(section)}\].*?(?=\[|$)'
            content = re.sub(section_pattern, '', content, flags=re.DOTALL)
        
        # Remove chaves obsoletas
        obsolete_keys = config.get('obsolete_keys', [])
        for key in obsolete_keys:
            key_pattern = rf'^{re.escape(key)}\s*=.*$'
            content = re.sub(key_pattern, '', content, flags=re.MULTILINE)
        
        # Substitui valores obsoletos
        obsolete_values = config.get('obsolete_values', {})
        for old_value, new_value in obsolete_values.items():
            content = content.replace(old_value, new_value)
        
        return content
    
    def fix_env_config(self, content, config):
        """Corrige configuração de variáveis de ambiente"""
        # Remove variáveis obsoletas
        obsolete_vars = config.get('obsolete_vars', [])
        for var in obsolete_vars:
            var_pattern = rf'^{re.escape(var)}\s*=.*$'
            content = re.sub(var_pattern, '', content, flags=re.MULTILINE)
        
        # Substitui valores obsoletos
        obsolete_values = config.get('obsolete_values', {})
        for old_value, new_value in obsolete_values.items():
            content = content.replace(old_value, new_value)
        
        # Adiciona variáveis padrão
        default_vars = config.get('default_vars', [])
        for var in default_vars:
            if var not in content:
                content += '\n' + var
        
        return content
    
    def fix_generic_config(self, content, config):
        """Corrige configuração genérica"""
        # Remove linhas obsoletas
        obsolete_lines = config.get('obsolete_lines', [])
        for line in obsolete_lines:
            content = content.replace(line, '')
        
        # Substitui valores obsoletos
        obsolete_values = config.get('obsolete_values', {})
        for old_value, new_value in obsolete_values.items():
            content = content.replace(old_value, new_value)
        
        # Adiciona configurações padrão
        default_config = config.get('default_config', '')
        if default_config and default_config not in content:
            content += '\n' + default_config
        
        return content
    
    def fix_inconsistent_params(self, inconsistent_params):
        """Corrige parâmetros inconsistentes"""
        fixes = []
        
        for param in inconsistent_params:
            file_path = param.get('file_path', '')
            param_name = param.get('param_name', '')
            description = param.get('description', '')
            
            if not file_path or not os.path.exists(file_path):
                continue
            
            try:
                # Backup do arquivo
                self.backup_file(file_path)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Corrige inconsistências específicas
                if "timeout" in param_name.lower():
                    content = self.fix_timeout_inconsistency(content, param)
                elif "port" in param_name.lower():
                    content = self.fix_port_inconsistency(content, param)
                elif "path" in param_name.lower():
                    content = self.fix_path_inconsistency(content, param)
                elif "url" in param_name.lower():
                    content = self.fix_url_inconsistency(content, param)
                else:
                    content = self.fix_generic_inconsistency(content, param)
                
                # Salva mudanças se houve alteração
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    fixes.append({
                        "file": file_path,
                        "param_name": param_name,
                        "description": description,
                        "fix_applied": "Inconsistent parameter standardized"
                    })
                    
                    self.correction_report["config_files_updated"].append(file_path)
                    
            except Exception as e:
                print(f"Erro ao corrigir parâmetro inconsistente em {file_path}: {e}")
        
        self.correction_report["inconsistent_params_fixed"] = fixes
        return fixes
    
    def fix_timeout_inconsistency(self, content, param):
        """Corrige inconsistência de timeout"""
        # Padroniza timeouts para valores consistentes
        timeout_patterns = [
            (r'timeout\s*=\s*(\d+)', 'timeout = 30'),
            (r'TIMEOUT\s*=\s*(\d+)', 'TIMEOUT = 30'),
            (r'"timeout":\s*(\d+)', '"timeout": 30'),
            (r"'timeout':\s*(\d+)", "'timeout': 30")
        ]
        
        for pattern, replacement in timeout_patterns:
            content = re.sub(pattern, replacement, content)
        
        return content
    
    def fix_port_inconsistency(self, content, param):
        """Corrige inconsistência de portas"""
        # Padroniza portas para valores consistentes
        port_patterns = [
            (r'port\s*=\s*(\d+)', 'port = 8080'),
            (r'PORT\s*=\s*(\d+)', 'PORT = 8080'),
            (r'"port":\s*(\d+)', '"port": 8080'),
            (r"'port':\s*(\d+)", "'port': 8080")
        ]
        
        for pattern, replacement in port_patterns:
            content = re.sub(pattern, replacement, content)
        
        return content
    
    def fix_path_inconsistency(self, content, param):
        """Corrige inconsistência de caminhos"""
        # Padroniza separadores de caminho
        content = content.replace('\\', '/')  # Unix-style paths
        
        # Corrige caminhos relativos
        content = re.sub(r'\.\./\.\./', '../', content)
        content = re.sub(r'\./\./', './', content)
        
        return content
    
    def fix_url_inconsistency(self, content, param):
        """Corrige inconsistência de URLs"""
        # Padroniza URLs
        content = re.sub(r'http://localhost:(\d+)', 'http://localhost:8080', content)
        content = re.sub(r'https://localhost:(\d+)', 'https://localhost:8443', content)
        
        return content
    
    def fix_generic_inconsistency(self, content, param):
        """Corrige inconsistência genérica"""
        # Remove espaços extras
        content = re.sub(r'\s+', ' ', content)
        
        # Padroniza quebras de linha
        content = content.replace('\r\n', '\n')
        
        # Remove linhas vazias duplicadas
        content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)
        
        return content
    
    def create_config_validation_rules(self):
        """Cria regras de validação de configuração"""
        validation_rules = '''
# Configuration Validation Rules

## JSON Configuration Validation
```python
import json
import jsonschema

def validate_json_config(config_data, schema):
    """Valida configuração JSON contra schema"""
    try:
        jsonschema.validate(config_data, schema)
        return True
    except jsonschema.ValidationError as e:
        print(f"Erro de validação: {e}")
        return False
```

## YAML Configuration Validation
```python
import yaml
from cerberus import Validator

def validate_yaml_config(config_data, schema):
    """Valida configuração YAML contra schema"""
    v = Validator(schema)
    if v.validate(config_data):
        return True
    else:
        print(f"Erro de validação: {v.errors}")
        return False
```

## Environment Variables Validation
```python
import os
from typing import Dict, List

def validate_env_vars(required_vars: List[str]) -> Dict[str, str]:
    """Valida variáveis de ambiente obrigatórias"""
    missing_vars = []
    env_vars = {}
    
    for var in required_vars:
        value = os.getenv(var)
        if value is None:
            missing_vars.append(var)
        else:
            env_vars[var] = value
    
    if missing_vars:
        raise ValueError(f"Variáveis de ambiente obrigatórias não encontradas: {missing_vars}")
    
    return env_vars
```

## Configuration Schema Examples
```json
{
  "type": "object",
  "properties": {
    "timeout": {"type": "integer", "minimum": 1, "maximum": 300},
    "port": {"type": "integer", "minimum": 1024, "maximum": 65535},
    "host": {"type": "string", "format": "hostname"},
    "debug": {"type": "boolean"},
    "log_level": {"type": "string", "enum": ["DEBUG", "INFO", "WARNING", "ERROR"]}
  },
  "required": ["timeout", "port", "host"]
}
```
'''
        
        validation_file = self.project_root / "wiki" / "docs" / "config_validation_rules.md"
        with open(validation_file, 'w', encoding='utf-8') as f:
            f.write(validation_rules)
        
        self.correction_report["validation_rules_added"].append(str(validation_file))
        return str(validation_file)
    
    def create_config_guidelines(self):
        """Cria diretrizes de configuração"""
        guidelines = '''# Diretrizes de Configuração - Codex MMORPG

## 1. Padrões de Configuração
- **JSON**: Para configurações complexas e hierárquicas
- **YAML**: Para configurações legíveis e comentadas
- **INI**: Para configurações simples de seções
- **ENV**: Para variáveis de ambiente e segredos
- **TOML**: Para configurações com tipos de dados

## 2. Nomenclatura
- Use nomes descritivos e em inglês
- Use snake_case para chaves e variáveis
- Use UPPER_CASE para variáveis de ambiente
- Mantenha consistência entre arquivos

## 3. Validação
- Implemente validação de schema para JSON/YAML
- Valide tipos de dados e ranges
- Verifique variáveis obrigatórias
- Use valores padrão seguros

## 4. Segurança
- Nunca commite senhas ou chaves secretas
- Use variáveis de ambiente para dados sensíveis
- Valide entrada de configuração
- Implemente rotação de credenciais

## 5. Organização
- Separe configurações por ambiente (dev, test, prod)
- Use herança de configuração
- Mantenha configurações centralizadas
- Documente todas as opções

## 6. Versionamento
- Versionar schemas de configuração
- Manter compatibilidade com versões anteriores
- Documentar mudanças de configuração
- Testar configurações em CI/CD

## 7. Monitoramento
- Logar mudanças de configuração
- Monitorar valores críticos
- Alertar para configurações inválidas
- Implementar health checks

## 8. Backup e Recuperação
- Fazer backup de configurações críticas
- Implementar rollback de configurações
- Testar recuperação de configurações
- Manter histórico de mudanças

## 9. Padrões Específicos

### Timeouts
- Padrão: 30 segundos
- Máximo: 300 segundos
- Mínimo: 1 segundo

### Portas
- Padrão: 8080 (HTTP), 8443 (HTTPS)
- Range: 1024-65535
- Evitar portas reservadas

### Caminhos
- Usar separadores Unix (/)
- Caminhos relativos quando possível
- Validar existência de arquivos

### URLs
- Usar HTTPS em produção
- Validar formato de URL
- Implementar fallbacks
'''
        
        guidelines_file = self.project_root / "wiki" / "docs" / "config_guidelines.md"
        with open(guidelines_file, 'w', encoding='utf-8') as f:
            f.write(guidelines)
        
        self.correction_report["config_files_updated"].append(str(guidelines_file))
        return str(guidelines_file)
    
    def create_config_manager(self):
        """Cria gerenciador de configuração"""
        config_manager = '''#!/usr/bin/env python3
"""
Configuration Manager - Gerencia configurações do sistema
"""
import os
import json
import yaml
from pathlib import Path
from typing import Dict, Any, Optional
from dataclasses import dataclass

@dataclass
class ConfigValidation:
    """Resultado da validação de configuração"""
    is_valid: bool
    errors: list
    warnings: list

class ConfigurationManager:
    """Gerenciador centralizado de configurações"""
    
    def __init__(self, config_dir: str = "config"):
        self.config_dir = Path(config_dir)
        self.config_cache = {}
        self.validation_rules = {}
    
    def load_config(self, config_name: str, config_type: str = "json") -> Dict[str, Any]:
        """Carrega configuração do arquivo"""
        config_file = self.config_dir / f"{config_name}.{config_type}"
        
        if not config_file.exists():
            raise FileNotFoundError(f"Arquivo de configuração não encontrado: {config_file}")
        
        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                if config_type == "json":
                    config = json.load(f)
                elif config_type == "yaml":
                    config = yaml.safe_load(f)
                else:
                    raise ValueError(f"Tipo de configuração não suportado: {config_type}")
            
            # Valida configuração
            validation = self.validate_config(config, config_name)
            if not validation.is_valid:
                print(f"Avisos na configuração {config_name}: {validation.warnings}")
            
            self.config_cache[config_name] = config
            return config
            
        except Exception as e:
            raise RuntimeError(f"Erro ao carregar configuração {config_name}: {e}")
    
    def save_config(self, config_name: str, config_data: Dict[str, Any], 
                   config_type: str = "json") -> None:
        """Salva configuração em arquivo"""
        config_file = self.config_dir / f"{config_name}.{config_type}"
        
        # Cria backup
        if config_file.exists():
            backup_file = config_file.with_suffix(f".{config_type}.backup")
            config_file.rename(backup_file)
        
        try:
            with open(config_file, 'w', encoding='utf-8') as f:
                if config_type == "json":
                    json.dump(config_data, f, indent=2, ensure_ascii=False)
                elif config_type == "yaml":
                    yaml.dump(config_data, f, default_flow_style=False)
                else:
                    raise ValueError(f"Tipo de configuração não suportado: {config_type}")
            
            self.config_cache[config_name] = config_data
            
        except Exception as e:
            raise RuntimeError(f"Erro ao salvar configuração {config_name}: {e}")
    
    def get_config(self, config_name: str, key: Optional[str] = None) -> Any:
        """Obtém valor de configuração"""
        if config_name not in self.config_cache:
            self.load_config(config_name)
        
        config = self.config_cache[config_name]
        
        if key is None:
            return config
        
        keys = key.split('.')
        value = config
        
        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                raise KeyError(f"Chave não encontrada: {key}")
        
        return value
    
    def set_config(self, config_name: str, key: str, value: Any) -> None:
        """Define valor de configuração"""
        if config_name not in self.config_cache:
            self.load_config(config_name)
        
        config = self.config_cache[config_name]
        keys = key.split('.')
        
        # Navega até o nível pai
        current = config
        for k in keys[:-1]:
            if k not in current:
                current[k] = {}
            current = current[k]
        
        # Define o valor
        current[keys[-1]] = value
    
    def validate_config(self, config: Dict[str, Any], config_name: str) -> ConfigValidation:
        """Valida configuração contra regras"""
        errors = []
        warnings = []
        
        # Regras básicas de validação
        if "timeout" in config:
            timeout = config["timeout"]
            if not isinstance(timeout, int) or timeout < 1 or timeout > 300:
                errors.append(f"Timeout deve ser inteiro entre 1 e 300, encontrado: {timeout}")
        
        if "port" in config:
            port = config["port"]
            if not isinstance(port, int) or port < 1024 or port > 65535:
                errors.append(f"Porta deve ser inteiro entre 1024 e 65535, encontrado: {port}")
        
        if "debug" in config and not isinstance(config["debug"], bool):
            errors.append("Debug deve ser booleano")
        
        # Verifica campos obrigatórios
        required_fields = self.validation_rules.get(config_name, {}).get("required", [])
        for field in required_fields:
            if field not in config:
                errors.append(f"Campo obrigatório não encontrado: {field}")
        
        return ConfigValidation(
            is_valid=len(errors) == 0,
            errors=errors,
            warnings=warnings
        )
    
    def reload_config(self, config_name: str) -> None:
        """Recarrega configuração do arquivo"""
        if config_name in self.config_cache:
            del self.config_cache[config_name]
        self.load_config(config_name)
    
    def list_configs(self) -> list:
        """Lista todas as configurações disponíveis"""
        configs = []
        for config_file in self.config_dir.glob("*.*"):
            if config_file.suffix in [".json", ".yaml", ".yml", ".ini"]:
                configs.append(config_file.stem)
        return configs

# Instância global
config_manager = ConfigurationManager()
'''
        
        manager_file = self.project_root / "wiki" / "bmad" / "config" / "config_manager.py"
        manager_file.parent.mkdir(parents=True, exist_ok=True)
        
        with open(manager_file, 'w', encoding='utf-8') as f:
            f.write(config_manager)
        
        self.correction_report["new_configs_created"].append(str(manager_file))
        return str(manager_file)
    
    def create_correction_report(self):
        """Cria relatório de correção"""
        report_file = self.audit_reports_dir / "config_correction_report.json"
        
        # Calcula estatísticas
        total_obsolete_fixes = len(self.correction_report["obsolete_configs_fixed"])
        total_inconsistent_fixes = len(self.correction_report["inconsistent_params_fixed"])
        total_files_updated = len(set(self.correction_report["config_files_updated"]))
        total_backups = len(self.correction_report["backup_files_created"])
        total_new_configs = len(self.correction_report["new_configs_created"])
        
        self.correction_report["total_fixes"] = total_obsolete_fixes + total_inconsistent_fixes
        
        self.correction_report["statistics"] = {
            "obsolete_configs_fixed": total_obsolete_fixes,
            "inconsistent_params_fixed": total_inconsistent_fixes,
            "config_files_updated": total_files_updated,
            "backup_files_created": total_backups,
            "new_configs_created": total_new_configs,
            "validation_rules_added": len(self.correction_report["validation_rules_added"])
        }
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(self.correction_report, f, indent=2, ensure_ascii=False)
        
        return str(report_file)
    
    def run_config_correction(self):
        """Executa correção de configuração completa"""
        print("⚙️ Iniciando correção de configurações e regras...")
        
        # Carrega relatório de configuração
        config_data = self.load_config_audit()
        if not config_data:
            print("❌ Não foi possível carregar relatório de configuração")
            return False
        
        print(f"📊 Configurações obsoletas identificadas: {len(config_data.get('obsolete_configs', []))}")
        print(f"📊 Parâmetros inconsistentes identificados: {len(config_data.get('inconsistent_params', []))}")
        
        # Corrige configurações obsoletas
        print("🔧 Corrigindo configurações obsoletas...")
        obsolete_fixes = self.fix_obsolete_configs(config_data.get('obsolete_configs', []))
        
        # Corrige parâmetros inconsistentes
        print("🔧 Corrigindo parâmetros inconsistentes...")
        inconsistent_fixes = self.fix_inconsistent_params(config_data.get('inconsistent_params', []))
        
        # Cria regras de validação
        print("📋 Criando regras de validação...")
        validation_file = self.create_config_validation_rules()
        
        # Cria diretrizes
        print("📋 Criando diretrizes de configuração...")
        guidelines_file = self.create_config_guidelines()
        
        # Cria gerenciador de configuração
        print("🔧 Criando gerenciador de configuração...")
        manager_file = self.create_config_manager()
        
        # Cria relatório
        report_file = self.create_correction_report()
        
        # Estatísticas finais
        total_fixes = len(obsolete_fixes) + len(inconsistent_fixes)
        
        print(f"\n✅ Correção de configuração concluída!")
        print(f"📊 Arquivos de configuração atualizados: {len(set(self.correction_report['config_files_updated']))}")
        print(f"🔧 Configurações obsoletas corrigidas: {len(obsolete_fixes)}")
        print(f"🔧 Parâmetros inconsistentes corrigidos: {len(inconsistent_fixes)}")
        print(f"💾 Backups criados: {len(self.correction_report['backup_files_created'])}")
        print(f"🆕 Novos arquivos criados: {len(self.correction_report['new_configs_created'])}")
        print(f"📄 Relatório salvo em: {report_file}")
        print(f"📋 Regras de validação: {validation_file}")
        print(f"📋 Diretrizes: {guidelines_file}")
        print(f"🔧 Gerenciador: {manager_file}")
        
        return True

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        project_root = sys.argv[1]
    else:
        project_root = "."
    
    agent = ConfigCorrectionAgent(project_root)
    result = agent.run_config_correction() 