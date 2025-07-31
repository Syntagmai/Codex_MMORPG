# Auto Update Maps Rules

## 📋 Regras de Atualização Automática de Mapas

Este arquivo define as regras para **atualização automática obrigatória** de todos os mapas JSON do projeto, garantindo que os índices estejam sempre sincronizados com o estado atual dos arquivos.

---

## 🎯 Regras Principais

### 1. **Atualização Automática Obrigatória**
**SEMPRE execute scripts de atualização de mapas antes de qualquer tarefa.** Todos os mapas JSON devem estar atualizados antes de iniciar qualquer operação.

### 2. **Ordem de Atualização Padronizada**
**Execute os scripts na ordem estabelecida:**
1. **Primeiro**: `update_source_index.py` - Índice do código-fonte
2. **Segundo**: `update_habdel_index.py` - Índice da documentação original
3. **Terceiro**: `update_modules_index.py` - Índice dos módulos
4. **Quarto**: `update_styles_index.py` - Índice dos estilos
5. **Quinto**: `update_resources_index.py` - Índice dos recursos
6. **Sexto**: `update_tools_index.py` - Índice das ferramentas
7. **Sétimo**: `wiki/update_json_maps.py` - Índices da wiki

### 3. **Trigger de Atualização**
**SEMPRE atualize mapas quando:**
- ✅ Qualquer tarefa for solicitada
- ✅ Arquivos forem modificados manualmente
- ✅ Novos arquivos forem criados
- ✅ Estrutura de pastas for alterada
- ✅ Dependências forem atualizadas

### 4. **Validação Obrigatória**
**SEMPRE valide a integridade dos mapas após atualização:**
- ✅ Verificar se todos os arquivos estão indexados
- ✅ Confirmar se metadados estão corretos
- ✅ Validar relacionamentos entre componentes
- ✅ Testar consultas de busca

### 5. **Fallback de Segurança**
**Se algum script falhar:**
- ✅ Continuar com os mapas existentes
- ✅ Reportar erro específico
- ✅ Tentar atualização parcial
- ✅ Manter sistema funcional

---

## 🔄 Processo de Atualização

### 📋 **Fluxo de Atualização Automática**

Para qualquer tarefa solicitada:

1. **Detectar** necessidade de atualização
2. **Executar** scripts na ordem estabelecida
3. **Validar** integridade dos mapas
4. **Reportar** status de atualização
5. **Prosseguir** com a tarefa solicitada

### 🎯 **Scripts de Atualização**

#### **1. Índice do Código-Fonte**
```bash
python update_source_index.py
```
- **Propósito**: Indexar código-fonte OTClient
- **Arquivo**: `otclient_source_index.json`
- **Frequência**: Sempre antes de consultas técnicas

#### **2. Índice da Documentação Original**
```bash
python update_habdel_index.py
```
- **Propósito**: Indexar documentação original e planejamento
- **Arquivo**: `habdel_index.json`
- **Frequência**: Sempre antes de consultas de documentação

#### **3. Índice dos Módulos**
```bash
python update_modules_index.py
```
- **Propósito**: Indexar módulos Lua e APIs
- **Arquivo**: `modules_index.json`
- **Frequência**: Sempre antes de consultas de módulos

#### **4. Índice dos Estilos**
```bash
python update_styles_index.py
```
- **Propósito**: Indexar estilos OTUI
- **Arquivo**: `styles_index.json`
- **Frequência**: Sempre antes de consultas de UI

#### **5. Índice dos Recursos**
```bash
python update_resources_index.py
```
- **Propósito**: Indexar recursos (imagens, sons, fontes)
- **Arquivo**: `resources_index.json`
- **Frequência**: Sempre antes de consultas de recursos

#### **6. Índice das Ferramentas**
```bash
python update_tools_index.py
```
- **Propósito**: Indexar ferramentas de desenvolvimento
- **Arquivo**: `tools_index.json`
- **Frequência**: Sempre antes de consultas de ferramentas

#### **7. Índices da Wiki**
```bash
python wiki/update_json_maps.py
```
- **Propósito**: Atualizar índices da wiki
- **Arquivos**: `tags_index.json`, `wiki_map.json`, `relationships.json`
- **Frequência**: Sempre antes de consultas da wiki

---

## ⚡ Otimização de Performance

### 🎯 **Estratégias de Atualização**

#### **1. Atualização Inteligente**
- **Detectar mudanças** antes de reindexar
- **Atualizar apenas** arquivos modificados
- **Manter cache** de metadados estáveis
- **Paralelizar** atualizações quando possível

#### **2. Atualização Incremental**
```python
def smart_update():
    """Atualização inteligente baseada em mudanças"""
    # Verificar timestamps dos arquivos
    # Identificar arquivos modificados
    # Atualizar apenas seções relevantes
    # Manter integridade dos relacionamentos
```

#### **3. Cache de Metadados**
- **Manter metadados** em memória durante sessão
- **Invalidar cache** apenas quando necessário
- **Reutilizar** informações estáveis
- **Otimizar** consultas frequentes

### 📊 **Métricas de Performance**

| Operação | Tempo Máximo | Otimização |
|----------|--------------|------------|
| **Atualização completa** | < 30s | Paralelização |
| **Atualização incremental** | < 5s | Detecção de mudanças |
| **Validação de integridade** | < 2s | Cache inteligente |
| **Consulta após atualização** | < 100ms | Índices otimizados |

---

## ⚠️ Regras de Exceção

### 1. **Emergências**
Em situações de emergência, pule atualização e use mapas existentes.

### 2. **Falhas de Script**
Se um script falhar, continue com os outros e reporte o erro.

### 3. **Recursos Limitados**
Em ambientes com recursos limitados, priorize mapas essenciais.

### 4. **Primeira Execução**
Na primeira execução, execute todos os scripts mesmo que demore.

---

## 📚 Exemplos de Uso

### 🔄 **Atualização Automática**
```python
def auto_update_all_maps():
    """Atualiza todos os mapas automaticamente"""
    scripts = [
        "update_source_index.py",
        "update_habdel_index.py", 
        "update_modules_index.py",
        "update_styles_index.py",
        "update_resources_index.py",
        "update_tools_index.py",
        "wiki/update_json_maps.py"
    ]
    
    for script in scripts:
        try:
            subprocess.run(["python", script], check=True)
            print(f"✅ {script} atualizado com sucesso")
        except subprocess.CalledProcessError as e:
            print(f"⚠️ {script} falhou: {e}")
            continue
```

### 🎯 **Validação de Integridade**
```python
def validate_maps_integrity():
    """Valida integridade de todos os mapas"""
    maps = [
        "otclient_source_index.json",
        "habdel_index.json",
        "modules_index.json", 
        "styles_index.json",
        "resources_index.json",
        "tools_index.json",
        "wiki/tags_index.json"
    ]
    
    for map_file in maps:
        try:
            with open(map_file, 'r') as f:
                data = json.load(f)
            print(f"✅ {map_file} válido")
        except Exception as e:
            print(f"❌ {map_file} inválido: {e}")
```

### 📊 **Relatório de Status**
```python
def generate_update_report():
    """Gera relatório de status dos mapas"""
    report = {
        "timestamp": datetime.now().isoformat(),
        "maps_updated": [],
        "maps_failed": [],
        "total_files_indexed": 0,
        "performance_metrics": {}
    }
    
    # Gerar relatório detalhado
    return report
```

---

## ✅ Tarefa Obrigatória da IA

**SEMPRE que qualquer tarefa for solicitada:**

1. **Detectar** necessidade de atualização de mapas
2. **Executar** scripts na ordem estabelecida
3. **Validar** integridade de todos os mapas
4. **Reportar** status de atualização
5. **Prosseguir** com a tarefa solicitada
6. **Manter** mapas sempre atualizados

---

## 📎 Integração com Sistema Existente

### 🔗 **Com system-rules.md**
- **Aplicar** regras de sistema antes de atualizar
- **Validar** consistência entre regras
- **Manter** hierarquia estabelecida

### 🔗 **Com otclient-source-index-rules.md**
- **Priorizar** atualização do código-fonte
- **Manter** sincronização com implementação real
- **Validar** categorização de sistemas

### 🔗 **Com wiki-json-navigation-rules.md**
- **Atualizar** índices da wiki automaticamente
- **Manter** relacionamentos entre documentos
- **Validar** estrutura de navegação

---

## 🚀 Benefícios Esperados

### ⚡ **Performance**
- **Mapas sempre atualizados** automaticamente
- **Consultas ultra-rápidas** via índices otimizados
- **Redução de 90%** no tempo de busca

### 🎯 **Precisão**
- **Informação sempre sincronizada** com arquivos
- **Relacionamentos** sempre corretos
- **Metadados** sempre precisos

### 💰 **Eficiência**
- **Menor uso de tokens** em consultas
- **Navegação direcionada** e precisa
- **Redução de processamento** desnecessário

### 🔄 **Automação**
- **Atualização transparente** para o usuário
- **Manutenção automática** de índices
- **Sistema auto-gerenciado** de mapas 