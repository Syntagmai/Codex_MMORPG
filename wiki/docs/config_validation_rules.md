
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
#### Nível Basic
```json

```

#### Nível Intermediate
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

#### Nível Advanced
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

## 🔗 **Links Automáticos**

> [!info] **Links Gerados Automaticamente**
> Estes links foram criados automaticamente pelo sistema de linkagem da categoria **Documentation**

### **📚 Links Obrigatórios**
- [[../README|Hub Central da Wiki]]
- [[../dashboard/task_master|Task Master]]
- [[../dashboard/integrated_task_manager|Dashboard Central]]
- [[../maps/search_index|Índice de Busca]]
- [[../maps/tags_index|Índice de Tags]]

### **🧭 Navegação**
- [[../maps/search_index|Índice de Busca]]
- [[../maps/tags_index|Índice de Tags]]
- [[../maps/category_indices|Índices por Categoria]]
- [[../maps/relationships|Relacionamentos]]

### **📊 Métricas da Categoria**
- **Categoria**: Documentation
- **Total de arquivos**: <!-- Contador automático -->
- **Arquivos linkados**: <!-- Contador automático -->
- **Taxa de linkagem**: <!-- Percentual automático -->

---

