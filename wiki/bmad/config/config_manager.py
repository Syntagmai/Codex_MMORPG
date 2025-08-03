#!/usr/bin/env python3
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
