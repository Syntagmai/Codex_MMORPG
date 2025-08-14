# 🪄 Índice de Funcionalidade: Magias

Este índice reúne toda a documentação sobre o **sistema de magias**, cobrindo desde a criação de novas spells no servidor Canary até seus efeitos visuais no OTClient.

---

## 📚 Conceitos Fundamentais
- **[Sistema de Magias (Canary)](<../canary_sistema_magias.md>)**: Guia detalhado sobre a infraestrutura de magias, vocações e fórmulas de dano/cura.
- **[Sistema de Partículas (Canary)](<../canary_sistema_particulas.md>)**: Como criar os efeitos visuais (partículas) associados às magias.
- **[Sistema de Animações (Canary)](<../canary_sistema_animacoes.md>)**: Para entender como os efeitos de magias são animados.
- **[Sistema de Som (Canary)](<../canary_sistema_som.md>)**: Para adicionar efeitos sonoros às magias.

## 🛠️ Como Criar e Modificar
- **[Como Criar Magias](<./como_criar.md#canary-servidor>)**: Link direto para a seção de criação de novas magias.
- **[Como Adicionar Efeitos Visuais](<./como_adicionar.md#canary-servidor>)**: Guia para adicionar partículas e animações.

## 📜 Exemplos de Código e Scripts
- **`canary/data/scripts/spells/`**: Diretório com todos os scripts de magias do servidor.
- **`canary/src/lua/functions/creatures/combat/`**: Funções C++ que dão suporte ao sistema de combate e magias.

## 🔗 Tópicos Relacionados
- **[Sistema de Combate](<../canary_sistema_combate.md>)**: As magias são um componente central do sistema de combate.
- **[Sistema de Scripting Lua](<../canary_sistema_scripting.md>)**: A base para a criação da lógica das magias.
- **[Protocolo de Comunicação](<../integracao_protocolo_comunicacao.md>)**: Para entender como os efeitos das magias são comunicados ao cliente.
