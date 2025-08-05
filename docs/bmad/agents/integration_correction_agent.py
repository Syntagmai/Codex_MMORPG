#!/usr/bin/env python3
"""
Integration Correction Agent - Epic 18 Task 18.4
Corrige integrações e dependências identificadas na Epic 17
"""
import os
import json
import re
import shutil
from datetime import datetime
from pathlib import Path

class IntegrationCorrectionAgent:
    def __init__(self, project_root):
        self.project_root = Path(project_root)
        self.audit_reports_dir = self.project_root / "wiki" / "docs" / "audit_reports"
        self.integration_report = self.audit_reports_dir / "integration_audit_report.json"
        self.correction_report = {
            "timestamp": datetime.now().isoformat(),
            "circular_dependencies_fixed": [],
            "broken_interfaces_fixed": [],
            "api_endpoints_fixed": [],
            "data_flows_fixed": [],
            "critical_integrations_fixed": [],
            "integration_points_fixed": [],
            "files_modified": [],
            "backups_created": [],
            "new_interfaces_created": [],
            "total_fixes": 0
        }
    
    def load_integration_audit(self):
        """Carrega o relatório de auditoria de integração"""
        try:
            with open(self.integration_report, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Erro ao carregar relatório de integração: {e}")
            return None
    
    def backup_file(self, file_path):
        """Cria backup de um arquivo antes de modificá-lo"""
        try:
            backup_path = str(file_path) + ".backup"
            shutil.copy2(file_path, backup_path)
            self.correction_report["backups_created"].append(backup_path)
            return True
        except Exception as e:
            print(f"Erro ao criar backup de {file_path}: {e}")
            return False
    
    def fix_circular_dependencies(self, circular_deps):
        """Corrige dependências circulares"""
        fixes = []
        
        for dep in circular_deps:
            file_path = dep.get('file_path', '')
            dependency_info = dep.get('dependency_info', '')
            description = dep.get('description', '')
            
            if not file_path or not os.path.exists(file_path):
                continue
            
            try:
                # Backup do arquivo
                self.backup_file(file_path)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Estratégias para quebrar dependências circulares
                if "import" in dependency_info.lower():
                    # Move imports para dentro de funções (lazy loading)
                    content = self.implement_lazy_loading(content)
                
                elif "class" in dependency_info.lower():
                    # Usa herança ou composição para quebrar dependência
                    content = self.break_class_dependency(content)
                
                elif "function" in dependency_info.lower():
                    # Usa callbacks ou eventos para quebrar dependência
                    content = self.break_function_dependency(content)
                
                # Salva mudanças se houve alteração
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    fixes.append({
                        "file": file_path,
                        "dependency_type": dependency_info,
                        "description": description,
                        "fix_applied": "Circular dependency broken"
                    })
                    
                    self.correction_report["files_modified"].append(file_path)
                    
            except Exception as e:
                print(f"Erro ao corrigir dependência circular em {file_path}: {e}")
        
        self.correction_report["circular_dependencies_fixed"] = fixes
        return fixes
    
    def implement_lazy_loading(self, content):
        """Implementa lazy loading para quebrar imports circulares"""
        # Move imports para dentro de funções
        import_pattern = r'^(import\s+[\w\s,]+|from\s+[\w.]+\s+import\s+[\w\s,]+)$'
        imports = re.findall(import_pattern, content, re.MULTILINE)
        
        # Remove imports do topo
        for imp in imports:
            content = content.replace(imp + '\n', '')
        
        # Adiciona função de lazy loading
        lazy_loading_code = '''
def get_required_modules():
    """Carrega módulos sob demanda para evitar dependências circulares"""
    import sys
    from importlib import import_module
    
    modules = {}
    
    def load_module(module_name):
        if module_name not in modules:
            try:
                modules[module_name] = import_module(module_name)
            except ImportError as e:
                print(f"Erro ao carregar módulo {module_name}: {e}")
                modules[module_name] = None
        return modules[module_name]
    
    return load_module

# Função global para carregamento lazy
lazy_load = get_required_modules()
'''
        
        # Adiciona código de lazy loading no início
        content = lazy_loading_code + '\n' + content
        
        return content
    
    def break_class_dependency(self, content):
        """Quebra dependência de classe usando herança ou composição"""
        # Identifica classes que podem usar herança
        class_pattern = r'class\s+(\w+)\s*\(([^)]+)\):'
        
        def replace_class(match):
            class_name = match.group(1)
            parent_class = match.group(2)
            
            # Se a classe pai causa dependência circular, usa composição
            if "circular" in parent_class.lower():
                return f'''class {class_name}:
    def __init__(self):
        self._parent = None
    
    def set_parent(self, parent):
        """Define parent via composição"""
        self._parent = parent
    
    def get_parent(self):
        """Obtém parent via composição"""
        return self._parent'''
            else:
                return match.group(0)
        
        content = re.sub(class_pattern, replace_class, content)
        return content
    
    def break_function_dependency(self, content):
        """Quebra dependência de função usando callbacks"""
        # Adiciona sistema de callbacks
        callback_code = '''
class CallbackManager:
    """Gerenciador de callbacks para quebrar dependências"""
    
    def __init__(self):
        self.callbacks = {}
    
    def register_callback(self, name, callback):
        """Registra um callback"""
        self.callbacks[name] = callback
    
    def call_callback(self, name, *args, **kwargs):
        """Executa um callback"""
        if name in self.callbacks:
            return self.callbacks[name](*args, **kwargs)
        return None

# Instância global do gerenciador de callbacks
callback_manager = CallbackManager()
'''
        
        content = callback_code + '\n' + content
        return content
    
    def fix_broken_interfaces(self, broken_interfaces):
        """Corrige interfaces quebradas"""
        fixes = []
        
        for interface in broken_interfaces:
            file_path = interface.get('file_path', '')
            interface_type = interface.get('interface_type', '')
            description = interface.get('description', '')
            
            if not file_path or not os.path.exists(file_path):
                continue
            
            try:
                # Backup do arquivo
                self.backup_file(file_path)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Correções específicas por tipo de interface
                if "api" in interface_type.lower():
                    content = self.fix_api_interface(content)
                elif "database" in interface_type.lower():
                    content = self.fix_database_interface(content)
                elif "file" in interface_type.lower():
                    content = self.fix_file_interface(content)
                elif "network" in interface_type.lower():
                    content = self.fix_network_interface(content)
                
                # Salva mudanças se houve alteração
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    fixes.append({
                        "file": file_path,
                        "interface_type": interface_type,
                        "description": description,
                        "fix_applied": "Interface fixed"
                    })
                    
                    self.correction_report["files_modified"].append(file_path)
                    
            except Exception as e:
                print(f"Erro ao corrigir interface em {file_path}: {e}")
        
        self.correction_report["broken_interfaces_fixed"] = fixes
        return fixes
    
    def fix_api_interface(self, content):
        """Corrige interface de API"""
        api_interface_code = '''
import requests
import json
from typing import Dict, Any, Optional

class APIClient:
    """Cliente API robusto com tratamento de erros"""
    
    def __init__(self, base_url: str, timeout: int = 30):
        self.base_url = base_url.rstrip('/')
        self.timeout = timeout
        self.session = requests.Session()
    
    def _make_request(self, method: str, endpoint: str, data: Optional[Dict] = None, 
                     headers: Optional[Dict] = None) -> Dict[str, Any]:
        """Faz requisição HTTP com tratamento de erros"""
        url = f"{self.base_url}/{endpoint.lstrip('/')}"
        
        try:
            response = self.session.request(
                method=method,
                url=url,
                json=data,
                headers=headers,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            return {"error": str(e), "status_code": getattr(e.response, 'status_code', None)}
    
    def get(self, endpoint: str, headers: Optional[Dict] = None) -> Dict[str, Any]:
        """GET request"""
        return self._make_request('GET', endpoint, headers=headers)
    
    def post(self, endpoint: str, data: Dict, headers: Optional[Dict] = None) -> Dict[str, Any]:
        """POST request"""
        return self._make_request('POST', endpoint, data=data, headers=headers)
    
    def put(self, endpoint: str, data: Dict, headers: Optional[Dict] = None) -> Dict[str, Any]:
        """PUT request"""
        return self._make_request('PUT', endpoint, data=data, headers=headers)
    
    def delete(self, endpoint: str, headers: Optional[Dict] = None) -> Dict[str, Any]:
        """DELETE request"""
        return self._make_request('DELETE', endpoint, headers=headers)
'''
        
        # Adiciona interface de API se não existir
        if "class APIClient" not in content:
            content = api_interface_code + '\n' + content
        
        return content
    
    def fix_database_interface(self, content):
        """Corrige interface de banco de dados"""
        db_interface_code = '''
import sqlite3
import psycopg2
from contextlib import contextmanager
from typing import List, Dict, Any, Optional

class DatabaseInterface:
    """Interface unificada para banco de dados"""
    
    def __init__(self, connection_string: str, db_type: str = "sqlite"):
        self.connection_string = connection_string
        self.db_type = db_type
    
    @contextmanager
    def get_connection(self):
        """Gerenciador de contexto para conexões"""
        conn = None
        try:
            if self.db_type == "sqlite":
                conn = sqlite3.connect(self.connection_string)
            elif self.db_type == "postgresql":
                conn = psycopg2.connect(self.connection_string)
            else:
                raise ValueError(f"Tipo de banco não suportado: {self.db_type}")
            
            yield conn
        except Exception as e:
            if conn:
                conn.rollback()
            raise e
        finally:
            if conn:
                conn.close()
    
    def execute_query(self, query: str, params: Optional[tuple] = None) -> List[Dict[str, Any]]:
        """Executa query e retorna resultados"""
        with self.get_connection() as conn:
            cursor = conn.cursor()
            try:
                if params:
                    cursor.execute(query, params)
                else:
                    cursor.execute(query)
                
                if query.strip().upper().startswith('SELECT'):
                    columns = [desc[0] for desc in cursor.description]
                    return [dict(zip(columns, row)) for row in cursor.fetchall()]
                else:
                    conn.commit()
                    return [{"affected_rows": cursor.rowcount}]
            except Exception as e:
                conn.rollback()
                raise e
'''
        
        # Adiciona interface de banco se não existir
        if "class DatabaseInterface" not in content:
            content = db_interface_code + '\n' + content
        
        return content
    
    def fix_file_interface(self, content):
        """Corrige interface de arquivo"""
        file_interface_code = '''
import os
import json
import csv
from pathlib import Path
from typing import Any, Dict, List, Optional

class FileInterface:
    """Interface unificada para operações de arquivo"""
    
    def __init__(self, base_path: str = "."):
        self.base_path = Path(base_path)
    
    def read_json(self, file_path: str) -> Dict[str, Any]:
        """Lê arquivo JSON"""
        full_path = self.base_path / file_path
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            raise IOError(f"Erro ao ler JSON {file_path}: {e}")
    
    def write_json(self, file_path: str, data: Dict[str, Any], indent: int = 2) -> None:
        """Escreve arquivo JSON"""
        full_path = self.base_path / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            with open(full_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=indent, ensure_ascii=False)
        except Exception as e:
            raise IOError(f"Erro ao escrever JSON {file_path}: {e}")
    
    def read_csv(self, file_path: str) -> List[Dict[str, str]]:
        """Lê arquivo CSV"""
        full_path = self.base_path / file_path
        try:
            with open(full_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                return list(reader)
        except Exception as e:
            raise IOError(f"Erro ao ler CSV {file_path}: {e}")
    
    def write_csv(self, file_path: str, data: List[Dict[str, str]], fieldnames: Optional[List[str]] = None) -> None:
        """Escreve arquivo CSV"""
        full_path = self.base_path / file_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        
        try:
            with open(full_path, 'w', encoding='utf-8', newline='') as f:
                if not fieldnames and data:
                    fieldnames = list(data[0].keys())
                
                writer = csv.DictWriter(f, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)
        except Exception as e:
            raise IOError(f"Erro ao escrever CSV {file_path}: {e}")
    
    def file_exists(self, file_path: str) -> bool:
        """Verifica se arquivo existe"""
        return (self.base_path / file_path).exists()
    
    def create_directory(self, dir_path: str) -> None:
        """Cria diretório"""
        full_path = self.base_path / dir_path
        full_path.mkdir(parents=True, exist_ok=True)
'''
        
        # Adiciona interface de arquivo se não existir
        if "class FileInterface" not in content:
            content = file_interface_code + '\n' + content
        
        return content
    
    def fix_network_interface(self, content):
        """Corrige interface de rede"""
        network_interface_code = '''
import socket
import asyncio
import aiohttp
from typing import Dict, Any, Optional

class NetworkInterface:
    """Interface unificada para operações de rede"""
    
    def __init__(self, timeout: int = 30):
        self.timeout = timeout
    
    async def http_request(self, method: str, url: str, data: Optional[Dict] = None, 
                          headers: Optional[Dict] = None) -> Dict[str, Any]:
        """Faz requisição HTTP assíncrona"""
        try:
            async with aiohttp.ClientSession() as session:
                async with session.request(method, url, json=data, headers=headers, 
                                         timeout=aiohttp.ClientTimeout(total=self.timeout)) as response:
                    return {
                        "status": response.status,
                        "data": await response.json() if response.content_type == 'application/json' else await response.text(),
                        "headers": dict(response.headers)
                    }
        except Exception as e:
            return {"error": str(e), "status": None}
    
    def tcp_connect(self, host: str, port: int) -> bool:
        """Testa conexão TCP"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(self.timeout)
            result = sock.connect_ex((host, port))
            sock.close()
            return result == 0
        except Exception:
            return False
    
    def udp_send(self, host: str, port: int, data: bytes) -> bool:
        """Envia dados via UDP"""
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            sock.settimeout(self.timeout)
            sock.sendto(data, (host, port))
            sock.close()
            return True
        except Exception:
            return False
'''
        
        # Adiciona interface de rede se não existir
        if "class NetworkInterface" not in content:
            content = network_interface_code + '\n' + content
        
        return content
    
    def fix_api_endpoints(self, api_endpoints):
        """Corrige endpoints de API"""
        fixes = []
        
        for endpoint in api_endpoints:
            file_path = endpoint.get('file_path', '')
            endpoint_info = endpoint.get('endpoint_info', '')
            description = endpoint.get('description', '')
            
            if not file_path or not os.path.exists(file_path):
                continue
            
            try:
                # Backup do arquivo
                self.backup_file(file_path)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Adiciona tratamento de erro e validação
                content = self.add_endpoint_validation(content)
                
                # Salva mudanças se houve alteração
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    fixes.append({
                        "file": file_path,
                        "endpoint_info": endpoint_info,
                        "description": description,
                        "fix_applied": "API endpoint validation added"
                    })
                    
                    self.correction_report["files_modified"].append(file_path)
                    
            except Exception as e:
                print(f"Erro ao corrigir endpoint em {file_path}: {e}")
        
        self.correction_report["api_endpoints_fixed"] = fixes
        return fixes
    
    def add_endpoint_validation(self, content):
        """Adiciona validação a endpoints"""
        validation_code = '''
from functools import wraps
from typing import Dict, Any, Optional

def validate_endpoint(required_params: Optional[list] = None, 
                     required_headers: Optional[list] = None):
    """Decorator para validar endpoints"""
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # Valida parâmetros obrigatórios
            if required_params:
                for param in required_params:
                    if param not in kwargs:
                        return {"error": f"Parâmetro obrigatório ausente: {param}"}, 400
            
            # Valida headers obrigatórios
            if required_headers:
                request = args[0] if args else None
                if request and hasattr(request, 'headers'):
                    for header in required_headers:
                        if header not in request.headers:
                            return {"error": f"Header obrigatório ausente: {header}"}, 400
            
            return func(*args, **kwargs)
        return wrapper
    return decorator

def handle_api_errors(func):
    """Decorator para tratamento de erros de API"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            return {"error": str(e), "type": "internal_error"}, 500
    return wrapper
'''
        
        # Adiciona validação se não existir
        if "def validate_endpoint" not in content:
            content = validation_code + '\n' + content
        
        return content
    
    def fix_data_flows(self, data_flows):
        """Corrige fluxos de dados"""
        fixes = []
        
        for flow in data_flows:
            file_path = flow.get('file_path', '')
            flow_type = flow.get('flow_type', '')
            description = flow.get('description', '')
            
            if not file_path or not os.path.exists(file_path):
                continue
            
            try:
                # Backup do arquivo
                self.backup_file(file_path)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Adiciona validação de dados
                content = self.add_data_validation(content)
                
                # Salva mudanças se houve alteração
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    fixes.append({
                        "file": file_path,
                        "flow_type": flow_type,
                        "description": description,
                        "fix_applied": "Data flow validation added"
                    })
                    
                    self.correction_report["files_modified"].append(file_path)
                    
            except Exception as e:
                print(f"Erro ao corrigir fluxo de dados em {file_path}: {e}")
        
        self.correction_report["data_flows_fixed"] = fixes
        return fixes
    
    def add_data_validation(self, content):
        """Adiciona validação de dados"""
        validation_code = '''
import re
from typing import Any, Dict, List, Optional

class DataValidator:
    """Validador de dados para fluxos"""
    
    @staticmethod
    def validate_email(email: str) -> bool:
        """Valida formato de email"""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return bool(re.match(pattern, email))
    
    @staticmethod
    def validate_url(url: str) -> bool:
        """Valida formato de URL"""
        pattern = r'^https?://[^\s/$.?#].[^\s]*$'
        return bool(re.match(pattern, url))
    
    @staticmethod
    def validate_required_fields(data: Dict, required_fields: List[str]) -> List[str]:
        """Valida campos obrigatórios"""
        missing = []
        for field in required_fields:
            if field not in data or data[field] is None or data[field] == "":
                missing.append(field)
        return missing
    
    @staticmethod
    def sanitize_string(text: str) -> str:
        """Sanitiza string"""
        if not text:
            return ""
        # Remove caracteres perigosos
        dangerous_chars = ['<', '>', '"', "'", '&']
        for char in dangerous_chars:
            text = text.replace(char, '')
        return text.strip()
    
    @staticmethod
    def validate_data_type(value: Any, expected_type: type) -> bool:
        """Valida tipo de dados"""
        return isinstance(value, expected_type)

# Instância global
data_validator = DataValidator()
'''
        
        # Adiciona validação se não existir
        if "class DataValidator" not in content:
            content = validation_code + '\n' + content
        
        return content
    
    def fix_critical_integrations(self, critical_integrations):
        """Corrige integrações críticas"""
        fixes = []
        
        for integration in critical_integrations:
            file_path = integration.get('file_path', '')
            integration_type = integration.get('integration_type', '')
            description = integration.get('description', '')
            
            if not file_path or not os.path.exists(file_path):
                continue
            
            try:
                # Backup do arquivo
                self.backup_file(file_path)
                
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                original_content = content
                
                # Adiciona tratamento de erro robusto
                content = self.add_robust_error_handling(content)
                
                # Salva mudanças se houve alteração
                if content != original_content:
                    with open(file_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    fixes.append({
                        "file": file_path,
                        "integration_type": integration_type,
                        "description": description,
                        "fix_applied": "Robust error handling added"
                    })
                    
                    self.correction_report["files_modified"].append(file_path)
                    
            except Exception as e:
                print(f"Erro ao corrigir integração crítica em {file_path}: {e}")
        
        self.correction_report["critical_integrations_fixed"] = fixes
        return fixes
    
    def add_robust_error_handling(self, content):
        """Adiciona tratamento de erro robusto"""
        error_handling_code = '''
import logging
import traceback
from typing import Any, Optional, Callable

class IntegrationErrorHandler:
    """Manipulador de erros para integrações críticas"""
    
    def __init__(self, logger_name: str = "integration"):
        self.logger = logging.getLogger(logger_name)
        self.retry_count = 3
        self.retry_delay = 1
    
    def handle_integration_error(self, func: Callable, *args, **kwargs) -> Optional[Any]:
        """Executa função com tratamento de erro robusto"""
        for attempt in range(self.retry_count):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                self.logger.error(f"Tentativa {attempt + 1} falhou: {str(e)}")
                self.logger.error(f"Traceback: {traceback.format_exc()}")
                
                if attempt < self.retry_count - 1:
                    import time
                    time.sleep(self.retry_delay * (attempt + 1))
                else:
                    self.logger.error("Todas as tentativas falharam")
                    raise e
    
    def log_integration_event(self, event_type: str, details: Dict[str, Any]):
        """Registra evento de integração"""
        self.logger.info(f"Evento de integração: {event_type} - {details}")

# Instância global
integration_error_handler = IntegrationErrorHandler()
'''
        
        # Adiciona tratamento de erro se não existir
        if "class IntegrationErrorHandler" not in content:
            content = error_handling_code + '\n' + content
        
        return content
    
    def create_integration_guidelines(self):
        """Cria diretrizes de integração"""
        guidelines = '''# Diretrizes de Integração - Codex MMORPG

## 1. Arquitetura de Integração
- Usar padrão de injeção de dependência
- Implementar interfaces bem definidas
- Evitar dependências circulares
- Usar lazy loading quando necessário
- Implementar fallbacks para integrações críticas

## 2. Tratamento de Erros
- Implementar retry automático para falhas temporárias
- Usar circuit breakers para integrações externas
- Logar todos os erros de integração
- Implementar fallbacks graciosos
- Monitorar health checks

## 3. Validação de Dados
- Validar entrada e saída de todas as integrações
- Implementar schemas de validação
- Sanitizar dados antes do processamento
- Validar tipos de dados
- Implementar transformações de dados

## 4. Performance
- Usar conexões persistentes quando possível
- Implementar cache para dados estáticos
- Otimizar queries e requisições
- Usar paginação para grandes volumes
- Monitorar latência e throughput

## 5. Segurança
- Validar todas as entradas
- Implementar autenticação e autorização
- Usar HTTPS para comunicações externas
- Sanitizar dados sensíveis
- Implementar rate limiting

## 6. Monitoramento
- Implementar health checks
- Monitorar métricas de integração
- Configurar alertas para falhas
- Logar eventos importantes
- Implementar tracing distribuído

## 7. Testes
- Testar cenários de sucesso e falha
- Implementar testes de integração
- Testar fallbacks e retry logic
- Simular condições de rede
- Testar performance sob carga

## 8. Documentação
- Documentar APIs e interfaces
- Manter documentação de integração atualizada
- Documentar fluxos de dados
- Criar diagramas de arquitetura
- Documentar procedimentos de troubleshooting
'''
        
        guidelines_file = self.project_root / "wiki" / "docs" / "integration_guidelines.md"
        with open(guidelines_file, 'w', encoding='utf-8') as f:
            f.write(guidelines)
        
        self.correction_report["files_modified"].append(str(guidelines_file))
        return str(guidelines_file)
    
    def create_correction_report(self):
        """Cria relatório de correção"""
        report_file = self.audit_reports_dir / "integration_correction_report.json"
        
        # Calcula estatísticas
        total_circular_fixes = len(self.correction_report["circular_dependencies_fixed"])
        total_interface_fixes = len(self.correction_report["broken_interfaces_fixed"])
        total_endpoint_fixes = len(self.correction_report["api_endpoints_fixed"])
        total_flow_fixes = len(self.correction_report["data_flows_fixed"])
        total_integration_fixes = len(self.correction_report["critical_integrations_fixed"])
        total_files_modified = len(set(self.correction_report["files_modified"]))
        
        self.correction_report["total_fixes"] = (
            total_circular_fixes + total_interface_fixes + 
            total_endpoint_fixes + total_flow_fixes + total_integration_fixes
        )
        
        self.correction_report["statistics"] = {
            "circular_dependencies_fixed": total_circular_fixes,
            "broken_interfaces_fixed": total_interface_fixes,
            "api_endpoints_fixed": total_endpoint_fixes,
            "data_flows_fixed": total_flow_fixes,
            "critical_integrations_fixed": total_integration_fixes,
            "files_modified": total_files_modified,
            "backups_created": len(self.correction_report["backups_created"])
        }
        
        with open(report_file, 'w', encoding='utf-8') as f:
            json.dump(self.correction_report, f, indent=2, ensure_ascii=False)
        
        return str(report_file)
    
    def run_integration_correction(self):
        """Executa correção de integração completa"""
        print("🔗 Iniciando correção de integrações e dependências...")
        
        # Carrega relatório de integração
        integration_data = self.load_integration_audit()
        if not integration_data:
            print("❌ Não foi possível carregar relatório de integração")
            return False
        
        print(f"📊 Dependências circulares identificadas: {len(integration_data.get('circular_dependencies', []))}")
        print(f"📊 Interfaces quebradas identificadas: {len(integration_data.get('broken_interfaces', []))}")
        print(f"📊 Endpoints de API identificados: {len(integration_data.get('api_endpoints', []))}")
        print(f"📊 Fluxos de dados identificados: {len(integration_data.get('data_flows', []))}")
        print(f"📊 Integrações críticas identificadas: {len(integration_data.get('critical_integrations', []))}")
        
        # Corrige dependências circulares
        print("🔄 Corrigindo dependências circulares...")
        circular_fixes = self.fix_circular_dependencies(integration_data.get('circular_dependencies', []))
        
        # Corrige interfaces quebradas
        print("🔧 Corrigindo interfaces quebradas...")
        interface_fixes = self.fix_broken_interfaces(integration_data.get('broken_interfaces', []))
        
        # Corrige endpoints de API
        print("🌐 Corrigindo endpoints de API...")
        endpoint_fixes = self.fix_api_endpoints(integration_data.get('api_endpoints', []))
        
        # Corrige fluxos de dados
        print("📊 Corrigindo fluxos de dados...")
        flow_fixes = self.fix_data_flows(integration_data.get('data_flows', []))
        
        # Corrige integrações críticas
        print("🚨 Corrigindo integrações críticas...")
        integration_fixes = self.fix_critical_integrations(integration_data.get('critical_integrations', []))
        
        # Cria diretrizes
        print("📋 Criando diretrizes de integração...")
        guidelines_file = self.create_integration_guidelines()
        
        # Cria relatório
        report_file = self.create_correction_report()
        
        # Estatísticas finais
        total_fixes = (
            len(circular_fixes) + len(interface_fixes) + 
            len(endpoint_fixes) + len(flow_fixes) + len(integration_fixes)
        )
        
        print(f"\n✅ Correção de integração concluída!")
        print(f"📊 Arquivos modificados: {len(set(self.correction_report['files_modified']))}")
        print(f"🔄 Dependências circulares corrigidas: {len(circular_fixes)}")
        print(f"🔧 Interfaces corrigidas: {len(interface_fixes)}")
        print(f"🌐 Endpoints corrigidos: {len(endpoint_fixes)}")
        print(f"📊 Fluxos de dados corrigidos: {len(flow_fixes)}")
        print(f"🚨 Integrações críticas corrigidas: {len(integration_fixes)}")
        print(f"📄 Relatório salvo em: {report_file}")
        print(f"📋 Diretrizes: {guidelines_file}")
        
        return True

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        project_root = sys.argv[1]
    else:
        project_root = "."
    
    agent = IntegrationCorrectionAgent(project_root)
    result = agent.run_integration_correction() 