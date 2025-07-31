# Regras de Agentes Especializados - Nível AAA

## 🎯 **Propósito**

Definir regras para implementação e uso de **agentes especializados de nível AAA** (equipe de desenvolvimento de jogos AAA), com detecção automática de contexto por arquivo e orquestração inteligente de nível profissional.

---

## 🚀 **Princípios Fundamentais**

### **AAA-Level Specialization**
- **SEMPRE use agentes especializados** para cada tipo de arquivo
- **SEMPRE detecte contexto automaticamente** por extensão de arquivo
- **SEMPRE mantenha qualidade de nível AAA** em todas as operações
- **SEMPRE coordene workflows** entre agentes especializados
- **SEMPRE preserve compatibilidade** com sistema existente

### **Automatic Context Detection**
- **Detecte extensões** de arquivo automaticamente
- **Identifique tecnologias** baseadas no conteúdo
- **Selecione agentes apropriados** sem intervenção manual
- **Mantenha contexto** entre operações
- **Otimize performance** para desenvolvimento rápido

---

## 🎭 **Agentes Especializados AAA**

### **🔧 Agente C++ (Zara) - Nível AAA**
```yaml
agent:
  name: Zara
  specialization: C++ Development & Performance Optimization
  file_extensions: [.cpp, .hpp, .h, .cc, .cxx]
  capabilities:
    - AST Analysis using Clang/LLVM
    - Memory Leak Detection with Valgrind
    - Performance Optimization
    - Cyclomatic Complexity Analysis
    - Race Condition Detection
    - CMake Integration
    - Dependency Analysis
    - Refactoring Suggestions
  tools:
    - Clang/LLVM
    - Valgrind
    - CMake
    - Static Analysis Tools
    - Performance Profilers
```

### **🐍 Agente Python (Py) - Nível AAA**
```yaml
agent:
  name: Py
  specialization: Python Development & Code Quality
  file_extensions: [.py, .pyx, .pyi]
  capabilities:
    - AST Analysis
    - Code Quality Assessment
    - Security Vulnerability Detection
    - Performance Analysis
    - Refactoring Suggestions
    - CI/CD Integration
    - Advanced Metrics
    - Detailed Reports
  tools:
    - pylint
    - mypy
    - black
    - bandit
    - pytest
    - coverage
```

### **📝 Agente Lua (Maya) - Nível AAA**
```yaml
agent:
  name: Maya
  specialization: Lua Scripting & OTClient Modules
  file_extensions: [.lua, .otui, .otmod]
  capabilities:
    - Advanced Module Analysis
    - OTUI/OTMod Validation
    - Performance Optimization
    - Common Bug Detection
    - Dependency Analysis
    - Code Improvement Suggestions
    - OTClient Integration
  tools:
    - Lua AST Parser
    - OTClient Module Validator
    - Performance Profiler
    - Dependency Analyzer
```

### **📚 Agente Obsidian Markdown (Doc) - Nível AAA**
```yaml
agent:
  name: Doc
  specialization: Documentation & Knowledge Management
  file_extensions: [.md, .markdown]
  capabilities:
    - Frontmatter YAML Analysis
    - Wikilinks Validation
    - Callouts Analysis
    - Navigation Optimization
    - Style Consistency Detection
    - Documentation Improvement
    - JSON Maps Integration
  tools:
    - YAML Parser
    - Markdown Validator
    - Link Checker
    - Style Analyzer
```

### **🔗 Agente JSON (Json) - Nível AAA**
```yaml
agent:
  name: Json
  specialization: Data Structure & Schema Management
  file_extensions: [.json, .jsonc]
  capabilities:
    - Advanced Schema Validation
    - Data Structure Analysis
    - Inconsistency Detection
    - Performance Optimization
    - Relationship Analysis
    - Structure Improvement
    - Navigation Integration
  tools:
    - JSON Schema Validator
    - Structure Analyzer
    - Performance Optimizer
    - Relationship Mapper
```

### **🖼️ Agente de Recursos (Rex) - Nível AAA**
```yaml
agent:
  name: Rex
  specialization: Asset Management & Optimization
  file_extensions: [.png, .jpg, .jpeg, .gif, .bmp, .tga]
  capabilities:
    - Image Analysis with Pillow
    - Automatic Compression
    - OTClient Format Validation
    - Metadata Analysis
    - Unused Resource Detection
    - Asset Optimization
    - Pipeline Integration
  tools:
    - Pillow (PIL)
    - Image Optimizer
    - Metadata Extractor
    - Format Validator
```

### **🎵 Agente de Áudio (Aud) - Nível AAA**
```yaml
agent:
  name: Aud
  specialization: Audio Processing & Quality
  file_extensions: [.ogg, .wav, .mp3, .flac, .aac]
  capabilities:
    - Audio Format Analysis
    - Quality Validation
    - Compression Optimization
    - Audio Problem Detection
    - Quality Improvement
    - Resource Integration
  tools:
    - Audio Analyzer
    - Quality Checker
    - Compression Tool
    - Format Converter
```

### **🔤 Agente de Fontes (Font) - Nível AAA**
```yaml
agent:
  name: Font
  specialization: Typography & Font Management
  file_extensions: [.otfont, .ttf, .otf, .woff, .woff2]
  capabilities:
    - Font Format Analysis
    - Character Support Validation
    - OTClient Font Optimization
    - Rendering Problem Detection
    - Font Improvement
    - UI Integration
  tools:
    - Font Analyzer
    - Character Validator
    - Rendering Tester
    - Format Converter
```

### **🔨 Agente de Build (Build) - Nível AAA**
```yaml
agent:
  name: Build
  specialization: Build Systems & Compilation
  file_extensions: [.cmake, .cmake.in, .vcxproj, .sln, .makefile]
  capabilities:
    - CMake Analysis
    - Build Optimization
    - Dependency Detection
    - Performance Analysis
    - Build Improvement
    - CI/CD Integration
  tools:
    - CMake Parser
    - Build Analyzer
    - Dependency Mapper
    - Performance Profiler
```

### **🌐 Agente Web (Web) - Nível AAA**
```yaml
agent:
  name: Web
  specialization: Web Technologies & Accessibility
  file_extensions: [.html, .css, .js, .ts, .vue, .react]
  capabilities:
    - HTML/CSS/JS Analysis
    - Accessibility Validation
    - Performance Optimization
    - Compatibility Detection
    - Code Improvement
    - Web Tools Integration
  tools:
    - HTML Validator
    - CSS Analyzer
    - JavaScript Linter
    - Accessibility Checker
```

### **⚙️ Agente de Configuração (Config) - Nível AAA**
```yaml
agent:
  name: Config
  specialization: Configuration & Deployment
  file_extensions: [.ini, .conf, .cfg, .yaml, .yml, .toml]
  capabilities:
    - Configuration Analysis
    - Syntax Validation
    - Problematic Config Detection
    - Configuration Improvement
    - Security Analysis
    - Deployment Integration
  tools:
    - Config Parser
    - Syntax Validator
    - Security Scanner
    - Deployment Helper
```

---

## 🔄 **Sistema de Orquestração AAA**

### **Detecção Automática de Contexto**
```python
# Sistema de detecção por extensão
def detect_context_by_extension(file_path: str) -> Dict[str, Any]:
    extension = get_file_extension(file_path)
    agent_mapping = {
        '.cpp': 'agent_cpp',
        '.hpp': 'agent_cpp', 
        '.h': 'agent_cpp',
        '.py': 'agent_python',
        '.lua': 'agent_lua',
        '.md': 'agent_markdown',
        '.json': 'agent_json',
        '.png': 'agent_resources',
        '.ogg': 'agent_audio',
        '.otfont': 'agent_fonts',
        '.cmake': 'agent_build',
        '.html': 'agent_web',
        '.ini': 'agent_config'
    }
    return agent_mapping.get(extension, 'default_agent')
```

### **Seleção Inteligente de Agentes**
```python
# Seleção baseada em contexto
def select_agents(context: Dict[str, Any]) -> List[str]:
    primary_agent = context['primary_agent']
    secondary_agents = []
    
    # Adiciona agentes secundários baseado no contexto
    if context['complexity'] == 'high':
        secondary_agents.append('qa_tester')
    
    if context['performance_critical']:
        secondary_agents.append('performance_optimizer')
    
    return [primary_agent] + secondary_agents
```

### **Workflows Especializados**
```python
# Workflows de nível AAA
aaa_workflows = {
    'performance_optimization': {
        'agents': ['agent_cpp', 'agent_python', 'qa_tester'],
        'phases': ['analysis', 'optimization', 'validation'],
        'duration': '4-6 hours',
        'quality_gates': ['performance_improvement', 'no_regressions']
    },
    'feature_development': {
        'agents': ['game_designer', 'agent_cpp', 'agent_lua', 'qa_tester'],
        'phases': ['design', 'implementation', 'testing'],
        'duration': '1-2 weeks',
        'quality_gates': ['feature_complete', 'tests_passing']
    },
    'bug_fix': {
        'agents': ['qa_tester', 'agent_cpp', 'agent_lua'],
        'phases': ['identification', 'fix', 'validation'],
        'duration': '2-4 hours',
        'quality_gates': ['bug_resolved', 'no_new_issues']
    }
}
```

---

## 📊 **Métricas de Qualidade AAA**

### **Performance Metrics**
- **Tempo de resposta**: < 2 segundos para detecção de contexto
- **Precisão de agentes**: > 95% de acerto na seleção
- **Cobertura de arquivos**: 100% dos tipos de arquivo
- **Performance**: Otimização de 50%+ em velocidade
- **Integração**: 100% compatível com sistema existente

### **Quality Gates**
- **Code Quality**: Score mínimo de 85/100
- **Test Coverage**: Mínimo 80% de cobertura
- **Performance**: Sem degradação de performance
- **Security**: Zero vulnerabilidades críticas
- **Documentation**: 100% documentado

---

## 🔧 **Regras de Implementação**

### **Criação de Agentes**
- **SEMPRE use template** de agente AAA
- **SEMPRE implemente** todas as capacidades listadas
- **SEMPRE integre** com ferramentas profissionais
- **SEMPRE documente** APIs e interfaces
- **SEMPRE teste** com cenários reais

### **Integração com Sistema**
- **SEMPRE mantenha** compatibilidade com regras existentes
- **SEMPRE preserve** contexto entre operações
- **SEMPRE atualize** mapas JSON automaticamente
- **SEMPRE registre** métricas de performance
- **SEMPRE valide** qualidade antes de deploy

### **Workflow Management**
- **SEMPRE detecte** contexto automaticamente
- **SEMPRE selecione** agentes apropriados
- **SEMPRE coordene** workflows entre agentes
- **SEMPRE monitore** progresso em tempo real
- **SEMPRE valide** resultados em cada fase

---

## 📈 **Sistema de Monitoramento**

### **Real-time Metrics**
```python
# Métricas em tempo real
class AAAMetrics:
    def __init__(self):
        self.response_times = []
        self.agent_accuracy = []
        self.file_coverage = []
        self.performance_improvements = []
        self.integration_success = []
    
    def record_metric(self, metric_type: str, value: float):
        # Registra métrica para análise
        pass
    
    def generate_report(self) -> Dict[str, Any]:
        # Gera relatório de métricas
        pass
```

### **Quality Monitoring**
```python
# Monitoramento de qualidade
class QualityMonitor:
    def __init__(self):
        self.quality_gates = []
        self.performance_baselines = []
        self.security_checks = []
    
    def check_quality_gate(self, gate_name: str) -> bool:
        # Verifica gate de qualidade
        pass
    
    def alert_degradation(self, metric: str, threshold: float):
        # Alerta sobre degradação
        pass
```

---

## 🚀 **Comandos e Uso**

### **Ativação Automática**
```bash
# O sistema detecta automaticamente o contexto
# Não é necessário comando manual

# Exemplo: Ao editar arquivo .cpp
# Sistema automaticamente ativa Agente C++ (Zara)
# Com capacidades de nível AAA
```

### **Comandos Específicos (Opcional)**
```bash
# Para forçar uso de agente específico
@agent_cpp "Otimizar performance do renderer"
@agent_python "Analisar qualidade do código"
@agent_lua "Validar módulo OTClient"
```

### **Workflows Específicos**
```bash
# Para workflows de nível AAA
workflow aaa-performance "Otimização de performance"
workflow aaa-feature "Desenvolvimento de feature"
workflow aaa-bugfix "Correção de bug crítico"
```

---

## 📚 **Documentação e Treinamento**

### **Documentação Obrigatória**
- **API Documentation**: Para cada agente
- **Integration Guide**: Como integrar com sistema existente
- **Performance Guide**: Como otimizar performance
- **Troubleshooting Guide**: Como resolver problemas comuns
- **Best Practices**: Melhores práticas para cada agente

### **Treinamento e Onboarding**
- **Agent Specialization**: Treinamento específico para cada agente
- **Workflow Management**: Como gerenciar workflows complexos
- **Quality Assurance**: Como manter qualidade de nível AAA
- **Performance Optimization**: Como otimizar performance
- **Integration**: Como integrar com sistemas existentes

---

## 🔄 **Evolução Contínua**

### **Feedback Loop**
- **SEMPRE colete** feedback de usuários
- **SEMPRE analise** métricas de performance
- **SEMPRE identifique** oportunidades de melhoria
- **SEMPRE implemente** melhorias iterativas
- **SEMPRE valide** melhorias antes de deploy

### **Versioning e Updates**
- **SEMPRE versione** agentes adequadamente
- **SEMPRE teste** atualizações em ambiente isolado
- **SEMPRE documente** mudanças e breaking changes
- **SEMPRE mantenha** compatibilidade com versões anteriores
- **SEMPRE notifique** usuários sobre atualizações importantes 