---
tags: [canary, api_reference, epic_2_1, analysis, documentation]
type: canary_documentation
status: in_progress
priority: critical
created: 2025-01-27
responsible_agent: deep_source_analyzer
---

# 📋 Referência de APIs - Projeto Canary

## 🎯 **Visão Geral**

Este documento fornece uma **referência completa das APIs públicas** do projeto Canary, incluindo todas as interfaces, métodos, parâmetros e exemplos de uso.

**Status**: Documentação em Progresso  
**Responsável**: Deep Source Analyzer  
**Epic**: 2.1.2 - Análise do Código C++

---

## 🎮 **Game Engine APIs**

### **🏗️ Game Class**

#### **Construtor e Destrutor**
#### Nível Basic
```cpp
Game::Game();
Game::~Game();
```

#### Nível Intermediate
```cpp
Game::Game();
Game::~Game();
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
Game::Game();
Game::~Game();
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

#### **Inicialização e Configuração**
#### Nível Basic
```cpp
/**
 * Inicializa o sistema de jogo
 * @param config Configuração do jogo
 * @return true se inicialização bem-sucedida
 */
bool Game::initialize(const GameConfig& config);

/**
 * Finaliza o sistema de jogo
 */
void Game::shutdown();

/**
 * Define configuração do jogo
 * @param config Nova configuração
 */
void Game::setConfig(const GameConfig& config);

/**
 * Obtém configuração atual do jogo
 * @return Configuração atual
 */
const GameConfig& Game::getConfig() const;
```

#### Nível Intermediate
```cpp
/**
 * Inicializa o sistema de jogo
 * @param config Configuração do jogo
 * @return true se inicialização bem-sucedida
 */
bool Game::initialize(const GameConfig& config);

/**
 * Finaliza o sistema de jogo
 */
void Game::shutdown();

/**
 * Define configuração do jogo
 * @param config Nova configuração
 */
void Game::setConfig(const GameConfig& config);

/**
 * Obtém configuração atual do jogo
 * @return Configuração atual
 */
const GameConfig& Game::getConfig() const;
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
/**
 * Inicializa o sistema de jogo
 * @param config Configuração do jogo
 * @return true se inicialização bem-sucedida
 */
bool Game::initialize(const GameConfig& config);

/**
 * Finaliza o sistema de jogo
 */
void Game::shutdown();

/**
 * Define configuração do jogo
 * @param config Nova configuração
 */
void Game::setConfig(const GameConfig& config);

/**
 * Obtém configuração atual do jogo
 * @return Configuração atual
 */
const GameConfig& Game::getConfig() const;
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

#### **Gerenciamento de Jogadores**
#### Nível Basic
```cpp
/**
 * Cria um novo jogador
 * @param name Nome do jogador
 * @return Ponteiro para o jogador criado ou nullptr se falhar
 */
Player* Game::createPlayer(const std::string& name);

/**
 * Remove um jogador do jogo
 * @param player Ponteiro para o jogador
 */
void Game::removePlayer(Player* player);

/**
 * Obtém jogador pelo nome
 * @param name Nome do jogador
 * @return Ponteiro para o jogador ou nullptr se não encontrado
 */
Player* Game::getPlayer(const std::string& name);

/**
 * Obtém todos os jogadores online
 * @return Vetor com todos os jogadores
 */
std::vector<Player*> Game::getAllPlayers();
```

#### Nível Intermediate
```cpp
/**
 * Cria um novo jogador
 * @param name Nome do jogador
 * @return Ponteiro para o jogador criado ou nullptr se falhar
 */
Player* Game::createPlayer(const std::string& name);

/**
 * Remove um jogador do jogo
 * @param player Ponteiro para o jogador
 */
void Game::removePlayer(Player* player);

/**
 * Obtém jogador pelo nome
 * @param name Nome do jogador
 * @return Ponteiro para o jogador ou nullptr se não encontrado
 */
Player* Game::getPlayer(const std::string& name);

/**
 * Obtém todos os jogadores online
 * @return Vetor com todos os jogadores
 */
std::vector<Player*> Game::getAllPlayers();
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
/**
 * Cria um novo jogador
 * @param name Nome do jogador
 * @return Ponteiro para o jogador criado ou nullptr se falhar
 */
Player* Game::createPlayer(const std::string& name);

/**
 * Remove um jogador do jogo
 * @param player Ponteiro para o jogador
 */
void Game::removePlayer(Player* player);

/**
 * Obtém jogador pelo nome
 * @param name Nome do jogador
 * @return Ponteiro para o jogador ou nullptr se não encontrado
 */
Player* Game::getPlayer(const std::string& name);

/**
 * Obtém todos os jogadores online
 * @return Vetor com todos os jogadores
 */
std::vector<Player*> Game::getAllPlayers();
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

#### **Loop Principal**
#### Nível Basic
```cpp
/**
 * Atualiza o estado do jogo
 * @param deltaTime Tempo decorrido desde última atualização (ms)
 */
void Game::update(uint32_t deltaTime);

/**
 * Processa eventos pendentes
 */
void Game::processEvents();
```

#### Nível Intermediate
```cpp
/**
 * Atualiza o estado do jogo
 * @param deltaTime Tempo decorrido desde última atualização (ms)
 */
void Game::update(uint32_t deltaTime);

/**
 * Processa eventos pendentes
 */
void Game::processEvents();
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
/**
 * Atualiza o estado do jogo
 * @param deltaTime Tempo decorrido desde última atualização (ms)
 */
void Game::update(uint32_t deltaTime);

/**
 * Processa eventos pendentes
 */
void Game::processEvents();
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

### **⚔️ CombatSystem Class**

#### **Gerenciamento de Combate**
#### Nível Basic
```cpp
/**
 * Executa um ataque
 * @param attacker Criatura atacante
 * @param target Criatura alvo
 * @return true se ataque foi executado
 */
bool CombatSystem::attack(Creature* attacker, Creature* target);

/**
 * Processa eventos de combate pendentes
 */
void CombatSystem::processCombatEvents();

/**
 * Registra um novo tipo de arma
 * @param type Tipo de arma a ser registrado
 */
void CombatSystem::registerWeaponType(const WeaponType& type);
```

#### Nível Intermediate
```cpp
/**
 * Executa um ataque
 * @param attacker Criatura atacante
 * @param target Criatura alvo
 * @return true se ataque foi executado
 */
bool CombatSystem::attack(Creature* attacker, Creature* target);

/**
 * Processa eventos de combate pendentes
 */
void CombatSystem::processCombatEvents();

/**
 * Registra um novo tipo de arma
 * @param type Tipo de arma a ser registrado
 */
void CombatSystem::registerWeaponType(const WeaponType& type);
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
/**
 * Executa um ataque
 * @param attacker Criatura atacante
 * @param target Criatura alvo
 * @return true se ataque foi executado
 */
bool CombatSystem::attack(Creature* attacker, Creature* target);

/**
 * Processa eventos de combate pendentes
 */
void CombatSystem::processCombatEvents();

/**
 * Registra um novo tipo de arma
 * @param type Tipo de arma a ser registrado
 */
void CombatSystem::registerWeaponType(const WeaponType& type);
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

#### **Cálculos de Dano**
#### Nível Basic
```cpp
/**
 * Calcula dano de uma arma
 * @param weapon Arma utilizada
 * @param attacker Criatura atacante
 * @return Valor do dano calculado
 */
uint32_t CombatSystem::calculateDamage(const Weapon& weapon, const Creature& attacker);

/**
 * Calcula defesa de uma armadura
 * @param armor Armadura utilizada
 * @param defender Criatura defendendo
 * @return Valor da defesa calculada
 */
uint32_t CombatSystem::calculateDefense(const Armor& armor, const Creature& defender);
```

#### Nível Intermediate
```cpp
/**
 * Calcula dano de uma arma
 * @param weapon Arma utilizada
 * @param attacker Criatura atacante
 * @return Valor do dano calculado
 */
uint32_t CombatSystem::calculateDamage(const Weapon& weapon, const Creature& attacker);

/**
 * Calcula defesa de uma armadura
 * @param armor Armadura utilizada
 * @param defender Criatura defendendo
 * @return Valor da defesa calculada
 */
uint32_t CombatSystem::calculateDefense(const Armor& armor, const Creature& defender);
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
/**
 * Calcula dano de uma arma
 * @param weapon Arma utilizada
 * @param attacker Criatura atacante
 * @return Valor do dano calculado
 */
uint32_t CombatSystem::calculateDamage(const Weapon& weapon, const Creature& attacker);

/**
 * Calcula defesa de uma armadura
 * @param armor Armadura utilizada
 * @param defender Criatura defendendo
 * @return Valor da defesa calculada
 */
uint32_t CombatSystem::calculateDefense(const Armor& armor, const Creature& defender);
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

#### **Sistema de Armas**
#### Nível Basic
```cpp
/**
 * Cria uma nova arma
 * @param type Tipo da arma
 * @return Ponteiro para a arma criada
 */
Weapon* CombatSystem::createWeapon(const WeaponType& type);
```

#### Nível Intermediate
```cpp
/**
 * Cria uma nova arma
 * @param type Tipo da arma
 * @return Ponteiro para a arma criada
 */
Weapon* CombatSystem::createWeapon(const WeaponType& type);
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
/**
 * Cria uma nova arma
 * @param type Tipo da arma
 * @return Ponteiro para a arma criada
 */
Weapon* CombatSystem::createWeapon(const WeaponType& type);
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

### **🎒 InventorySystem Class**

#### **Gerenciamento de Itens**
#### Nível Basic
```cpp
/**
 * Cria um novo item
 * @param type Tipo do item
 * @return Ponteiro para o item criado
 */
Item* InventorySystem::createItem(const ItemType& type);

/**
 * Destrói um item
 * @param item Item a ser destruído
 */
void InventorySystem::destroyItem(Item* item);

/**
 * Obtém item pelo ID
 * @param id ID do item
 * @return Ponteiro para o item ou nullptr se não encontrado
 */
Item* InventorySystem::getItem(uint32_t id);
```

#### Nível Intermediate
```cpp
/**
 * Cria um novo item
 * @param type Tipo do item
 * @return Ponteiro para o item criado
 */
Item* InventorySystem::createItem(const ItemType& type);

/**
 * Destrói um item
 * @param item Item a ser destruído
 */
void InventorySystem::destroyItem(Item* item);

/**
 * Obtém item pelo ID
 * @param id ID do item
 * @return Ponteiro para o item ou nullptr se não encontrado
 */
Item* InventorySystem::getItem(uint32_t id);
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
/**
 * Cria um novo item
 * @param type Tipo do item
 * @return Ponteiro para o item criado
 */
Item* InventorySystem::createItem(const ItemType& type);

/**
 * Destrói um item
 * @param item Item a ser destruído
 */
void InventorySystem::destroyItem(Item* item);

/**
 * Obtém item pelo ID
 * @param id ID do item
 * @return Ponteiro para o item ou nullptr se não encontrado
 */
Item* InventorySystem::getItem(uint32_t id);
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

#### **Operações de Inventário**
#### Nível Basic
```cpp
/**
 * Adiciona item ao inventário do jogador
 * @param player Jogador
 * @param item Item a ser adicionado
 * @param slot Slot do inventário
 * @return true se operação bem-sucedida
 */
bool InventorySystem::addItem(Player* player, Item* item, uint32_t slot);

/**
 * Remove item do inventário do jogador
 * @param player Jogador
 * @param slot Slot do inventário
 * @return true se operação bem-sucedida
 */
bool InventorySystem::removeItem(Player* player, uint32_t slot);

/**
 * Move item entre slots do inventário
 * @param player Jogador
 * @param fromSlot Slot de origem
 * @param toSlot Slot de destino
 * @return true se operação bem-sucedida
 */
bool InventorySystem::moveItem(Player* player, uint32_t fromSlot, uint32_t toSlot);
```

#### Nível Intermediate
```cpp
/**
 * Adiciona item ao inventário do jogador
 * @param player Jogador
 * @param item Item a ser adicionado
 * @param slot Slot do inventário
 * @return true se operação bem-sucedida
 */
bool InventorySystem::addItem(Player* player, Item* item, uint32_t slot);

/**
 * Remove item do inventário do jogador
 * @param player Jogador
 * @param slot Slot do inventário
 * @return true se operação bem-sucedida
 */
bool InventorySystem::removeItem(Player* player, uint32_t slot);

/**
 * Move item entre slots do inventário
 * @param player Jogador
 * @param fromSlot Slot de origem
 * @param toSlot Slot de destino
 * @return true se operação bem-sucedida
 */
bool InventorySystem::moveItem(Player* player, uint32_t fromSlot, uint32_t toSlot);
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
/**
 * Adiciona item ao inventário do jogador
 * @param player Jogador
 * @param item Item a ser adicionado
 * @param slot Slot do inventário
 * @return true se operação bem-sucedida
 */
bool InventorySystem::addItem(Player* player, Item* item, uint32_t slot);

/**
 * Remove item do inventário do jogador
 * @param player Jogador
 * @param slot Slot do inventário
 * @return true se operação bem-sucedida
 */
bool InventorySystem::removeItem(Player* player, uint32_t slot);

/**
 * Move item entre slots do inventário
 * @param player Jogador
 * @param fromSlot Slot de origem
 * @param toSlot Slot de destino
 * @return true se operação bem-sucedida
 */
bool InventorySystem::moveItem(Player* player, uint32_t fromSlot, uint32_t toSlot);
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

#### **Verificações**
#### Nível Basic
```cpp
/**
 * Verifica se jogador pode carregar item
 * @param player Jogador
 * @param item Item a ser verificado
 * @return true se pode carregar
 */
bool InventorySystem::canCarry(Player* player, Item* item);

/**
 * Obtém próximo slot livre do jogador
 * @param player Jogador
 * @return Índice do slot livre ou -1 se não houver
 */
uint32_t InventorySystem::getFreeSlot(Player* player);
```

#### Nível Intermediate
```cpp
/**
 * Verifica se jogador pode carregar item
 * @param player Jogador
 * @param item Item a ser verificado
 * @return true se pode carregar
 */
bool InventorySystem::canCarry(Player* player, Item* item);

/**
 * Obtém próximo slot livre do jogador
 * @param player Jogador
 * @return Índice do slot livre ou -1 se não houver
 */
uint32_t InventorySystem::getFreeSlot(Player* player);
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
/**
 * Verifica se jogador pode carregar item
 * @param player Jogador
 * @param item Item a ser verificado
 * @return true se pode carregar
 */
bool InventorySystem::canCarry(Player* player, Item* item);

/**
 * Obtém próximo slot livre do jogador
 * @param player Jogador
 * @return Índice do slot livre ou -1 se não houver
 */
uint32_t InventorySystem::getFreeSlot(Player* player);
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

---

## 🌐 **Network Layer APIs**

### **🌐 NetworkManager Class**

#### **Inicialização e Configuração**
#### Nível Basic
```cpp
/**
 * Inicializa o sistema de rede
 * @param config Configuração de rede
 * @return true se inicialização bem-sucedida
 */
bool NetworkManager::initialize(const NetworkConfig& config);

/**
 * Finaliza o sistema de rede
 */
void NetworkManager::shutdown();

/**
 * Define configuração de rede
 * @param config Nova configuração
 */
void NetworkManager::setConfig(const NetworkConfig& config);

/**
 * Obtém configuração atual de rede
 * @return Configuração atual
 */
const NetworkConfig& NetworkManager::getConfig() const;
```

#### Nível Intermediate
```cpp
/**
 * Inicializa o sistema de rede
 * @param config Configuração de rede
 * @return true se inicialização bem-sucedida
 */
bool NetworkManager::initialize(const NetworkConfig& config);

/**
 * Finaliza o sistema de rede
 */
void NetworkManager::shutdown();

/**
 * Define configuração de rede
 * @param config Nova configuração
 */
void NetworkManager::setConfig(const NetworkConfig& config);

/**
 * Obtém configuração atual de rede
 * @return Configuração atual
 */
const NetworkConfig& NetworkManager::getConfig() const;
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
/**
 * Inicializa o sistema de rede
 * @param config Configuração de rede
 * @return true se inicialização bem-sucedida
 */
bool NetworkManager::initialize(const NetworkConfig& config);

/**
 * Finaliza o sistema de rede
 */
void NetworkManager::shutdown();

/**
 * Define configuração de rede
 * @param config Nova configuração
 */
void NetworkManager::setConfig(const NetworkConfig& config);

/**
 * Obtém configuração atual de rede
 * @return Configuração atual
 */
const NetworkConfig& NetworkManager::getConfig() const;
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

#### **Gerenciamento de Conexões**
#### Nível Basic
```cpp
/**
 * Aceita nova conexão
 * @return Ponteiro para nova conexão ou nullptr se falhar
 */
Connection* NetworkManager::acceptConnection();

/**
 * Fecha uma conexão
 * @param connection Conexão a ser fechada
 */
void NetworkManager::closeConnection(Connection* connection);
```

#### Nível Intermediate
```cpp
/**
 * Aceita nova conexão
 * @return Ponteiro para nova conexão ou nullptr se falhar
 */
Connection* NetworkManager::acceptConnection();

/**
 * Fecha uma conexão
 * @param connection Conexão a ser fechada
 */
void NetworkManager::closeConnection(Connection* connection);
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
/**
 * Aceita nova conexão
 * @return Ponteiro para nova conexão ou nullptr se falhar
 */
Connection* NetworkManager::acceptConnection();

/**
 * Fecha uma conexão
 * @param connection Conexão a ser fechada
 */
void NetworkManager::closeConnection(Connection* connection);
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

#### **Processamento de Dados**
#### Nível Basic
```cpp
/**
 * Processa dados recebidos
 */
void NetworkManager::processIncomingData();

/**
 * Envia dados através de uma conexão
 * @param connection Conexão de destino
 * @param packet Pacote a ser enviado
 */
void NetworkManager::sendData(Connection* connection, const Packet& packet);
```

#### Nível Intermediate
```cpp
/**
 * Processa dados recebidos
 */
void NetworkManager::processIncomingData();

/**
 * Envia dados através de uma conexão
 * @param connection Conexão de destino
 * @param packet Pacote a ser enviado
 */
void NetworkManager::sendData(Connection* connection, const Packet& packet);
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
/**
 * Processa dados recebidos
 */
void NetworkManager::processIncomingData();

/**
 * Envia dados através de uma conexão
 * @param connection Conexão de destino
 * @param packet Pacote a ser enviado
 */
void NetworkManager::sendData(Connection* connection, const Packet& packet);
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

### **📡 ProtocolHandler Class**

#### **Processamento de Pacotes**
#### Nível Basic
```cpp
/**
 * Processa um pacote recebido
 * @param connection Conexão de origem
 * @param packet Pacote a ser processado
 * @return true se processamento bem-sucedido
 */
bool ProtocolHandler::processPacket(Connection* connection, const Packet& packet);

/**
 * Cria um novo pacote
 * @param type Tipo do pacote
 * @param data Dados do pacote
 * @return Pacote criado
 */
Packet ProtocolHandler::createPacket(uint16_t type, const PacketData& data);
```

#### Nível Intermediate
```cpp
/**
 * Processa um pacote recebido
 * @param connection Conexão de origem
 * @param packet Pacote a ser processado
 * @return true se processamento bem-sucedido
 */
bool ProtocolHandler::processPacket(Connection* connection, const Packet& packet);

/**
 * Cria um novo pacote
 * @param type Tipo do pacote
 * @param data Dados do pacote
 * @return Pacote criado
 */
Packet ProtocolHandler::createPacket(uint16_t type, const PacketData& data);
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
/**
 * Processa um pacote recebido
 * @param connection Conexão de origem
 * @param packet Pacote a ser processado
 * @return true se processamento bem-sucedido
 */
bool ProtocolHandler::processPacket(Connection* connection, const Packet& packet);

/**
 * Cria um novo pacote
 * @param type Tipo do pacote
 * @param data Dados do pacote
 * @return Pacote criado
 */
Packet ProtocolHandler::createPacket(uint16_t type, const PacketData& data);
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

#### **Registro de Handlers**
#### Nível Basic
```cpp
/**
 * Registra handler para tipo de pacote
 * @param type Tipo do pacote
 * @param handler Função handler
 */
void ProtocolHandler::registerHandler(uint16_t type, PacketHandler handler);

/**
 * Remove handler para tipo de pacote
 * @param type Tipo do pacote
 */
void ProtocolHandler::unregisterHandler(uint16_t type);
```

#### Nível Intermediate
```cpp
/**
 * Registra handler para tipo de pacote
 * @param type Tipo do pacote
 * @param handler Função handler
 */
void ProtocolHandler::registerHandler(uint16_t type, PacketHandler handler);

/**
 * Remove handler para tipo de pacote
 * @param type Tipo do pacote
 */
void ProtocolHandler::unregisterHandler(uint16_t type);
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
/**
 * Registra handler para tipo de pacote
 * @param type Tipo do pacote
 * @param handler Função handler
 */
void ProtocolHandler::registerHandler(uint16_t type, PacketHandler handler);

/**
 * Remove handler para tipo de pacote
 * @param type Tipo do pacote
 */
void ProtocolHandler::unregisterHandler(uint16_t type);
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

#### **Validação**
#### Nível Basic
```cpp
/**
 * Valida estrutura de um pacote
 * @param packet Pacote a ser validado
 * @return true se pacote válido
 */
bool ProtocolHandler::validatePacket(const Packet& packet);

/**
 * Autentica um pacote
 * @param packet Pacote a ser autenticado
 * @return true se autenticação bem-sucedida
 */
bool ProtocolHandler::authenticatePacket(const Packet& packet);
```

#### Nível Intermediate
```cpp
/**
 * Valida estrutura de um pacote
 * @param packet Pacote a ser validado
 * @return true se pacote válido
 */
bool ProtocolHandler::validatePacket(const Packet& packet);

/**
 * Autentica um pacote
 * @param packet Pacote a ser autenticado
 * @return true se autenticação bem-sucedida
 */
bool ProtocolHandler::authenticatePacket(const Packet& packet);
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
/**
 * Valida estrutura de um pacote
 * @param packet Pacote a ser validado
 * @return true se pacote válido
 */
bool ProtocolHandler::validatePacket(const Packet& packet);

/**
 * Autentica um pacote
 * @param packet Pacote a ser autenticado
 * @return true se autenticação bem-sucedida
 */
bool ProtocolHandler::authenticatePacket(const Packet& packet);
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

---

## 💾 **Database System APIs**

### **🗄️ DatabaseManager Class**

#### **Inicialização e Configuração**
#### Nível Basic
```cpp
/**
 * Inicializa o sistema de banco de dados
 * @param config Configuração do banco
 * @return true se inicialização bem-sucedida
 */
bool DatabaseManager::initialize(const DatabaseConfig& config);

/**
 * Finaliza o sistema de banco de dados
 */
void DatabaseManager::shutdown();
```

#### Nível Intermediate
```cpp
/**
 * Inicializa o sistema de banco de dados
 * @param config Configuração do banco
 * @return true se inicialização bem-sucedida
 */
bool DatabaseManager::initialize(const DatabaseConfig& config);

/**
 * Finaliza o sistema de banco de dados
 */
void DatabaseManager::shutdown();
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
/**
 * Inicializa o sistema de banco de dados
 * @param config Configuração do banco
 * @return true se inicialização bem-sucedida
 */
bool DatabaseManager::initialize(const DatabaseConfig& config);

/**
 * Finaliza o sistema de banco de dados
 */
void DatabaseManager::shutdown();
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

#### **Operações de Banco**
#### Nível Basic
```cpp
/**
 * Executa uma query genérica
 * @param query Query SQL
 * @return true se execução bem-sucedida
 */
bool DatabaseManager::executeQuery(const std::string& query);

/**
 * Executa uma query SELECT
 * @param query Query SELECT
 * @return Resultado da query
 */
QueryResult DatabaseManager::executeSelect(const std::string& query);

/**
 * Executa uma query INSERT
 * @param query Query INSERT
 * @return ID do registro inserido
 */
uint32_t DatabaseManager::executeInsert(const std::string& query);

/**
 * Executa uma query UPDATE
 * @param query Query UPDATE
 * @return true se execução bem-sucedida
 */
bool DatabaseManager::executeUpdate(const std::string& query);
```

#### Nível Intermediate
```cpp
/**
 * Executa uma query genérica
 * @param query Query SQL
 * @return true se execução bem-sucedida
 */
bool DatabaseManager::executeQuery(const std::string& query);

/**
 * Executa uma query SELECT
 * @param query Query SELECT
 * @return Resultado da query
 */
QueryResult DatabaseManager::executeSelect(const std::string& query);

/**
 * Executa uma query INSERT
 * @param query Query INSERT
 * @return ID do registro inserido
 */
uint32_t DatabaseManager::executeInsert(const std::string& query);

/**
 * Executa uma query UPDATE
 * @param query Query UPDATE
 * @return true se execução bem-sucedida
 */
bool DatabaseManager::executeUpdate(const std::string& query);
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
/**
 * Executa uma query genérica
 * @param query Query SQL
 * @return true se execução bem-sucedida
 */
bool DatabaseManager::executeQuery(const std::string& query);

/**
 * Executa uma query SELECT
 * @param query Query SELECT
 * @return Resultado da query
 */
QueryResult DatabaseManager::executeSelect(const std::string& query);

/**
 * Executa uma query INSERT
 * @param query Query INSERT
 * @return ID do registro inserido
 */
uint32_t DatabaseManager::executeInsert(const std::string& query);

/**
 * Executa uma query UPDATE
 * @param query Query UPDATE
 * @return true se execução bem-sucedida
 */
bool DatabaseManager::executeUpdate(const std::string& query);
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

#### **Transações**
#### Nível Basic
```cpp
/**
 * Inicia uma transação
 * @return true se início bem-sucedido
 */
bool DatabaseManager::beginTransaction();

/**
 * Confirma uma transação
 * @return true se confirmação bem-sucedida
 */
bool DatabaseManager::commitTransaction();

/**
 * Reverte uma transação
 * @return true se reversão bem-sucedida
 */
bool DatabaseManager::rollbackTransaction();
```

#### Nível Intermediate
```cpp
/**
 * Inicia uma transação
 * @return true se início bem-sucedido
 */
bool DatabaseManager::beginTransaction();

/**
 * Confirma uma transação
 * @return true se confirmação bem-sucedida
 */
bool DatabaseManager::commitTransaction();

/**
 * Reverte uma transação
 * @return true se reversão bem-sucedida
 */
bool DatabaseManager::rollbackTransaction();
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
/**
 * Inicia uma transação
 * @return true se início bem-sucedido
 */
bool DatabaseManager::beginTransaction();

/**
 * Confirma uma transação
 * @return true se confirmação bem-sucedida
 */
bool DatabaseManager::commitTransaction();

/**
 * Reverte uma transação
 * @return true se reversão bem-sucedida
 */
bool DatabaseManager::rollbackTransaction();
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

#### **Cache**
#### Nível Basic
```cpp
/**
 * Define valor no cache
 * @param key Chave do cache
 * @param value Valor a ser armazenado
 */
void DatabaseManager::setCache(const std::string& key, const std::string& value);

/**
 * Obtém valor do cache
 * @param key Chave do cache
 * @return Valor armazenado ou string vazia se não encontrado
 */
std::string DatabaseManager::getCache(const std::string& key);

/**
 * Limpa todo o cache
 */
void DatabaseManager::clearCache();
```

#### Nível Intermediate
```cpp
/**
 * Define valor no cache
 * @param key Chave do cache
 * @param value Valor a ser armazenado
 */
void DatabaseManager::setCache(const std::string& key, const std::string& value);

/**
 * Obtém valor do cache
 * @param key Chave do cache
 * @return Valor armazenado ou string vazia se não encontrado
 */
std::string DatabaseManager::getCache(const std::string& key);

/**
 * Limpa todo o cache
 */
void DatabaseManager::clearCache();
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
/**
 * Define valor no cache
 * @param key Chave do cache
 * @param value Valor a ser armazenado
 */
void DatabaseManager::setCache(const std::string& key, const std::string& value);

/**
 * Obtém valor do cache
 * @param key Chave do cache
 * @return Valor armazenado ou string vazia se não encontrado
 */
std::string DatabaseManager::getCache(const std::string& key);

/**
 * Limpa todo o cache
 */
void DatabaseManager::clearCache();
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

---

## 🎮 **Game Object APIs**

### **👤 Player Class**

#### **Propriedades Básicas**
#### Nível Basic
```cpp
/**
 * Obtém nome do jogador
 * @return Nome do jogador
 */
std::string Player::getName() const;

/**
 * Define nome do jogador
 * @param name Novo nome
 */
void Player::setName(const std::string& name);

/**
 * Obtém posição do jogador
 * @return Posição atual
 */
Position Player::getPosition() const;

/**
 * Define posição do jogador
 * @param pos Nova posição
 */
void Player::setPosition(const Position& pos);

/**
 * Obtém saúde do jogador
 * @return Valor da saúde
 */
uint32_t Player::getHealth() const;

/**
 * Define saúde do jogador
 * @param health Novo valor de saúde
 */
void Player::setHealth(uint32_t health);

/**
 * Obtém mana do jogador
 * @return Valor da mana
 */
uint32_t Player::getMana() const;

/**
 * Define mana do jogador
 * @param mana Novo valor de mana
 */
void Player::setMana(uint32_t mana);
```

#### Nível Intermediate
```cpp
/**
 * Obtém nome do jogador
 * @return Nome do jogador
 */
std::string Player::getName() const;

/**
 * Define nome do jogador
 * @param name Novo nome
 */
void Player::setName(const std::string& name);

/**
 * Obtém posição do jogador
 * @return Posição atual
 */
Position Player::getPosition() const;

/**
 * Define posição do jogador
 * @param pos Nova posição
 */
void Player::setPosition(const Position& pos);

/**
 * Obtém saúde do jogador
 * @return Valor da saúde
 */
uint32_t Player::getHealth() const;

/**
 * Define saúde do jogador
 * @param health Novo valor de saúde
 */
void Player::setHealth(uint32_t health);

/**
 * Obtém mana do jogador
 * @return Valor da mana
 */
uint32_t Player::getMana() const;

/**
 * Define mana do jogador
 * @param mana Novo valor de mana
 */
void Player::setMana(uint32_t mana);
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
/**
 * Obtém nome do jogador
 * @return Nome do jogador
 */
std::string Player::getName() const;

/**
 * Define nome do jogador
 * @param name Novo nome
 */
void Player::setName(const std::string& name);

/**
 * Obtém posição do jogador
 * @return Posição atual
 */
Position Player::getPosition() const;

/**
 * Define posição do jogador
 * @param pos Nova posição
 */
void Player::setPosition(const Position& pos);

/**
 * Obtém saúde do jogador
 * @return Valor da saúde
 */
uint32_t Player::getHealth() const;

/**
 * Define saúde do jogador
 * @param health Novo valor de saúde
 */
void Player::setHealth(uint32_t health);

/**
 * Obtém mana do jogador
 * @return Valor da mana
 */
uint32_t Player::getMana() const;

/**
 * Define mana do jogador
 * @param mana Novo valor de mana
 */
void Player::setMana(uint32_t mana);
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

#### **Inventário**
#### Nível Basic
```cpp
/**
 * Obtém item em slot específico
 * @param slot Índice do slot
 * @return Item no slot ou nullptr se vazio
 */
Item* Player::getItem(uint32_t slot) const;

/**
 * Define item em slot específico
 * @param slot Índice do slot
 * @param item Item a ser colocado
 */
void Player::setItem(uint32_t slot, Item* item);

/**
 * Obtém todos os itens do inventário
 * @return Vetor com todos os itens
 */
std::vector<Item*> Player::getInventory() const;

/**
 * Verifica se slot está vazio
 * @param slot Índice do slot
 * @return true se slot vazio
 */
bool Player::isSlotEmpty(uint32_t slot) const;
```

#### Nível Intermediate
```cpp
/**
 * Obtém item em slot específico
 * @param slot Índice do slot
 * @return Item no slot ou nullptr se vazio
 */
Item* Player::getItem(uint32_t slot) const;

/**
 * Define item em slot específico
 * @param slot Índice do slot
 * @param item Item a ser colocado
 */
void Player::setItem(uint32_t slot, Item* item);

/**
 * Obtém todos os itens do inventário
 * @return Vetor com todos os itens
 */
std::vector<Item*> Player::getInventory() const;

/**
 * Verifica se slot está vazio
 * @param slot Índice do slot
 * @return true se slot vazio
 */
bool Player::isSlotEmpty(uint32_t slot) const;
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
/**
 * Obtém item em slot específico
 * @param slot Índice do slot
 * @return Item no slot ou nullptr se vazio
 */
Item* Player::getItem(uint32_t slot) const;

/**
 * Define item em slot específico
 * @param slot Índice do slot
 * @param item Item a ser colocado
 */
void Player::setItem(uint32_t slot, Item* item);

/**
 * Obtém todos os itens do inventário
 * @return Vetor com todos os itens
 */
std::vector<Item*> Player::getInventory() const;

/**
 * Verifica se slot está vazio
 * @param slot Índice do slot
 * @return true se slot vazio
 */
bool Player::isSlotEmpty(uint32_t slot) const;
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

#### **Experiência e Nível**
#### Nível Basic
```cpp
/**
 * Obtém nível do jogador
 * @return Nível atual
 */
uint32_t Player::getLevel() const;

/**
 * Define nível do jogador
 * @param level Novo nível
 */
void Player::setLevel(uint32_t level);

/**
 * Obtém experiência do jogador
 * @return Experiência atual
 */
uint64_t Player::getExperience() const;

/**
 * Adiciona experiência ao jogador
 * @param exp Experiência a ser adicionada
 */
void Player::addExperience(uint64_t exp);

/**
 * Obtém experiência necessária para próximo nível
 * @return Experiência necessária
 */
uint64_t Player::getExperienceForNextLevel() const;
```

#### Nível Intermediate
```cpp
/**
 * Obtém nível do jogador
 * @return Nível atual
 */
uint32_t Player::getLevel() const;

/**
 * Define nível do jogador
 * @param level Novo nível
 */
void Player::setLevel(uint32_t level);

/**
 * Obtém experiência do jogador
 * @return Experiência atual
 */
uint64_t Player::getExperience() const;

/**
 * Adiciona experiência ao jogador
 * @param exp Experiência a ser adicionada
 */
void Player::addExperience(uint64_t exp);

/**
 * Obtém experiência necessária para próximo nível
 * @return Experiência necessária
 */
uint64_t Player::getExperienceForNextLevel() const;
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
/**
 * Obtém nível do jogador
 * @return Nível atual
 */
uint32_t Player::getLevel() const;

/**
 * Define nível do jogador
 * @param level Novo nível
 */
void Player::setLevel(uint32_t level);

/**
 * Obtém experiência do jogador
 * @return Experiência atual
 */
uint64_t Player::getExperience() const;

/**
 * Adiciona experiência ao jogador
 * @param exp Experiência a ser adicionada
 */
void Player::addExperience(uint64_t exp);

/**
 * Obtém experiência necessária para próximo nível
 * @return Experiência necessária
 */
uint64_t Player::getExperienceForNextLevel() const;
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

### **🐉 Creature Class**

#### **Propriedades Básicas**
#### Nível Basic
```cpp
/**
 * Obtém ID da criatura
 * @return ID único
 */
uint32_t Creature::getId() const;

/**
 * Obtém nome da criatura
 * @return Nome da criatura
 */
std::string Creature::getName() const;

/**
 * Define nome da criatura
 * @param name Novo nome
 */
void Creature::setName(const std::string& name);

/**
 * Obtém posição da criatura
 * @return Posição atual
 */
Position Creature::getPosition() const;

/**
 * Define posição da criatura
 * @param pos Nova posição
 */
void Creature::setPosition(const Position& pos);

/**
 * Obtém saúde da criatura
 * @return Valor da saúde
 */
uint32_t Creature::getHealth() const;

/**
 * Define saúde da criatura
 * @param health Novo valor de saúde
 */
void Creature::setHealth(uint32_t health);

/**
 * Obtém saúde máxima da criatura
 * @return Valor máximo de saúde
 */
uint32_t Creature::getMaxHealth() const;

/**
 * Define saúde máxima da criatura
 * @param maxHealth Novo valor máximo
 */
void Creature::setMaxHealth(uint32_t maxHealth);
```

#### Nível Intermediate
```cpp
/**
 * Obtém ID da criatura
 * @return ID único
 */
uint32_t Creature::getId() const;

/**
 * Obtém nome da criatura
 * @return Nome da criatura
 */
std::string Creature::getName() const;

/**
 * Define nome da criatura
 * @param name Novo nome
 */
void Creature::setName(const std::string& name);

/**
 * Obtém posição da criatura
 * @return Posição atual
 */
Position Creature::getPosition() const;

/**
 * Define posição da criatura
 * @param pos Nova posição
 */
void Creature::setPosition(const Position& pos);

/**
 * Obtém saúde da criatura
 * @return Valor da saúde
 */
uint32_t Creature::getHealth() const;

/**
 * Define saúde da criatura
 * @param health Novo valor de saúde
 */
void Creature::setHealth(uint32_t health);

/**
 * Obtém saúde máxima da criatura
 * @return Valor máximo de saúde
 */
uint32_t Creature::getMaxHealth() const;

/**
 * Define saúde máxima da criatura
 * @param maxHealth Novo valor máximo
 */
void Creature::setMaxHealth(uint32_t maxHealth);
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
/**
 * Obtém ID da criatura
 * @return ID único
 */
uint32_t Creature::getId() const;

/**
 * Obtém nome da criatura
 * @return Nome da criatura
 */
std::string Creature::getName() const;

/**
 * Define nome da criatura
 * @param name Novo nome
 */
void Creature::setName(const std::string& name);

/**
 * Obtém posição da criatura
 * @return Posição atual
 */
Position Creature::getPosition() const;

/**
 * Define posição da criatura
 * @param pos Nova posição
 */
void Creature::setPosition(const Position& pos);

/**
 * Obtém saúde da criatura
 * @return Valor da saúde
 */
uint32_t Creature::getHealth() const;

/**
 * Define saúde da criatura
 * @param health Novo valor de saúde
 */
void Creature::setHealth(uint32_t health);

/**
 * Obtém saúde máxima da criatura
 * @return Valor máximo de saúde
 */
uint32_t Creature::getMaxHealth() const;

/**
 * Define saúde máxima da criatura
 * @param maxHealth Novo valor máximo
 */
void Creature::setMaxHealth(uint32_t maxHealth);
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

#### **Movimento**
#### Nível Basic
```cpp
/**
 * Move criatura para posição
 * @param pos Posição de destino
 * @return true se movimento bem-sucedido
 */
bool Creature::moveTo(const Position& pos);

/**
 * Obtém direção da criatura
 * @return Direção atual
 */
Direction Creature::getDirection() const;

/**
 * Define direção da criatura
 * @param dir Nova direção
 */
void Creature::setDirection(Direction dir);

/**
 * Obtém velocidade da criatura
 * @return Velocidade atual
 */
uint32_t Creature::getSpeed() const;

/**
 * Define velocidade da criatura
 * @param speed Nova velocidade
 */
void Creature::setSpeed(uint32_t speed);
```

#### Nível Intermediate
```cpp
/**
 * Move criatura para posição
 * @param pos Posição de destino
 * @return true se movimento bem-sucedido
 */
bool Creature::moveTo(const Position& pos);

/**
 * Obtém direção da criatura
 * @return Direção atual
 */
Direction Creature::getDirection() const;

/**
 * Define direção da criatura
 * @param dir Nova direção
 */
void Creature::setDirection(Direction dir);

/**
 * Obtém velocidade da criatura
 * @return Velocidade atual
 */
uint32_t Creature::getSpeed() const;

/**
 * Define velocidade da criatura
 * @param speed Nova velocidade
 */
void Creature::setSpeed(uint32_t speed);
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
/**
 * Move criatura para posição
 * @param pos Posição de destino
 * @return true se movimento bem-sucedido
 */
bool Creature::moveTo(const Position& pos);

/**
 * Obtém direção da criatura
 * @return Direção atual
 */
Direction Creature::getDirection() const;

/**
 * Define direção da criatura
 * @param dir Nova direção
 */
void Creature::setDirection(Direction dir);

/**
 * Obtém velocidade da criatura
 * @return Velocidade atual
 */
uint32_t Creature::getSpeed() const;

/**
 * Define velocidade da criatura
 * @param speed Nova velocidade
 */
void Creature::setSpeed(uint32_t speed);
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

#### **Combate**
#### Nível Basic
```cpp
/**
 * Obtém alvo atual da criatura
 * @return Alvo atual ou nullptr se nenhum
 */
Creature* Creature::getTarget() const;

/**
 * Define alvo da criatura
 * @param target Novo alvo
 */
void Creature::setTarget(Creature* target);

/**
 * Ataca uma criatura
 * @param target Criatura alvo
 * @return true se ataque executado
 */
bool Creature::attack(Creature* target);

/**
 * Recebe dano
 * @param damage Quantidade de dano
 * @param attacker Criatura atacante
 */
void Creature::takeDamage(uint32_t damage, Creature* attacker = nullptr);

/**
 * Verifica se criatura está morta
 * @return true se morta
 */
bool Creature::isDead() const;
```

#### Nível Intermediate
```cpp
/**
 * Obtém alvo atual da criatura
 * @return Alvo atual ou nullptr se nenhum
 */
Creature* Creature::getTarget() const;

/**
 * Define alvo da criatura
 * @param target Novo alvo
 */
void Creature::setTarget(Creature* target);

/**
 * Ataca uma criatura
 * @param target Criatura alvo
 * @return true se ataque executado
 */
bool Creature::attack(Creature* target);

/**
 * Recebe dano
 * @param damage Quantidade de dano
 * @param attacker Criatura atacante
 */
void Creature::takeDamage(uint32_t damage, Creature* attacker = nullptr);

/**
 * Verifica se criatura está morta
 * @return true se morta
 */
bool Creature::isDead() const;
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
/**
 * Obtém alvo atual da criatura
 * @return Alvo atual ou nullptr se nenhum
 */
Creature* Creature::getTarget() const;

/**
 * Define alvo da criatura
 * @param target Novo alvo
 */
void Creature::setTarget(Creature* target);

/**
 * Ataca uma criatura
 * @param target Criatura alvo
 * @return true se ataque executado
 */
bool Creature::attack(Creature* target);

/**
 * Recebe dano
 * @param damage Quantidade de dano
 * @param attacker Criatura atacante
 */
void Creature::takeDamage(uint32_t damage, Creature* attacker = nullptr);

/**
 * Verifica se criatura está morta
 * @return true se morta
 */
bool Creature::isDead() const;
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

### **🎒 Item Class**

#### **Propriedades Básicas**
#### Nível Basic
```cpp
/**
 * Obtém ID do item
 * @return ID único
 */
uint32_t Item::getId() const;

/**
 * Obtém tipo do item
 * @return Tipo do item
 */
ItemType Item::getType() const;

/**
 * Define tipo do item
 * @param type Novo tipo
 */
void Item::setType(const ItemType& type);

/**
 * Obtém posição do item
 * @return Posição atual
 */
Position Item::getPosition() const;

/**
 * Define posição do item
 * @param pos Nova posição
 */
void Item::setPosition(const Position& pos);

/**
 * Obtém quantidade do item
 * @return Quantidade atual
 */
uint32_t Item::getCount() const;

/**
 * Define quantidade do item
 * @param count Nova quantidade
 */
void Item::setCount(uint32_t count);
```

#### Nível Intermediate
```cpp
/**
 * Obtém ID do item
 * @return ID único
 */
uint32_t Item::getId() const;

/**
 * Obtém tipo do item
 * @return Tipo do item
 */
ItemType Item::getType() const;

/**
 * Define tipo do item
 * @param type Novo tipo
 */
void Item::setType(const ItemType& type);

/**
 * Obtém posição do item
 * @return Posição atual
 */
Position Item::getPosition() const;

/**
 * Define posição do item
 * @param pos Nova posição
 */
void Item::setPosition(const Position& pos);

/**
 * Obtém quantidade do item
 * @return Quantidade atual
 */
uint32_t Item::getCount() const;

/**
 * Define quantidade do item
 * @param count Nova quantidade
 */
void Item::setCount(uint32_t count);
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
/**
 * Obtém ID do item
 * @return ID único
 */
uint32_t Item::getId() const;

/**
 * Obtém tipo do item
 * @return Tipo do item
 */
ItemType Item::getType() const;

/**
 * Define tipo do item
 * @param type Novo tipo
 */
void Item::setType(const ItemType& type);

/**
 * Obtém posição do item
 * @return Posição atual
 */
Position Item::getPosition() const;

/**
 * Define posição do item
 * @param pos Nova posição
 */
void Item::setPosition(const Position& pos);

/**
 * Obtém quantidade do item
 * @return Quantidade atual
 */
uint32_t Item::getCount() const;

/**
 * Define quantidade do item
 * @param count Nova quantidade
 */
void Item::setCount(uint32_t count);
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

#### **Atributos**
#### Nível Basic
```cpp
/**
 * Obtém atributo do item
 * @param attr Nome do atributo
 * @return Valor do atributo ou string vazia se não encontrado
 */
std::string Item::getAttribute(const std::string& attr) const;

/**
 * Define atributo do item
 * @param attr Nome do atributo
 * @param value Valor do atributo
 */
void Item::setAttribute(const std::string& attr, const std::string& value);

/**
 * Remove atributo do item
 * @param attr Nome do atributo
 */
void Item::removeAttribute(const std::string& attr);

/**
 * Verifica se item possui atributo
 * @param attr Nome do atributo
 * @return true se possui atributo
 */
bool Item::hasAttribute(const std::string& attr) const;

/**
 * Obtém todos os atributos do item
 * @return Mapa com todos os atributos
 */
std::map<std::string, std::string> Item::getAllAttributes() const;
```

#### Nível Intermediate
```cpp
/**
 * Obtém atributo do item
 * @param attr Nome do atributo
 * @return Valor do atributo ou string vazia se não encontrado
 */
std::string Item::getAttribute(const std::string& attr) const;

/**
 * Define atributo do item
 * @param attr Nome do atributo
 * @param value Valor do atributo
 */
void Item::setAttribute(const std::string& attr, const std::string& value);

/**
 * Remove atributo do item
 * @param attr Nome do atributo
 */
void Item::removeAttribute(const std::string& attr);

/**
 * Verifica se item possui atributo
 * @param attr Nome do atributo
 * @return true se possui atributo
 */
bool Item::hasAttribute(const std::string& attr) const;

/**
 * Obtém todos os atributos do item
 * @return Mapa com todos os atributos
 */
std::map<std::string, std::string> Item::getAllAttributes() const;
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
/**
 * Obtém atributo do item
 * @param attr Nome do atributo
 * @return Valor do atributo ou string vazia se não encontrado
 */
std::string Item::getAttribute(const std::string& attr) const;

/**
 * Define atributo do item
 * @param attr Nome do atributo
 * @param value Valor do atributo
 */
void Item::setAttribute(const std::string& attr, const std::string& value);

/**
 * Remove atributo do item
 * @param attr Nome do atributo
 */
void Item::removeAttribute(const std::string& attr);

/**
 * Verifica se item possui atributo
 * @param attr Nome do atributo
 * @return true se possui atributo
 */
bool Item::hasAttribute(const std::string& attr) const;

/**
 * Obtém todos os atributos do item
 * @return Mapa com todos os atributos
 */
std::map<std::string, std::string> Item::getAllAttributes() const;
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

#### **Manipulação**
#### Nível Basic
```cpp
/**
 * Move item para nova posição
 * @param newPos Nova posição
 * @return true se movimento bem-sucedido
 */
bool Item::moveTo(const Position& newPos);

/**
 * Divide item em duas partes
 * @param count Quantidade a ser separada
 * @return Novo item com quantidade separada ou nullptr se falhar
 */
Item* Item::split(uint32_t count);

/**
 * Une item com outro item
 * @param other Item a ser unido
 * @return true se união bem-sucedida
 */
bool Item::merge(Item* other);

/**
 * Verifica se item pode ser empilhado
 * @return true se pode empilhar
 */
bool Item::isStackable() const;

/**
 * Verifica se item pode ser movido
 * @return true se pode mover
 */
bool Item::isMovable() const;
```

#### Nível Intermediate
```cpp
/**
 * Move item para nova posição
 * @param newPos Nova posição
 * @return true se movimento bem-sucedido
 */
bool Item::moveTo(const Position& newPos);

/**
 * Divide item em duas partes
 * @param count Quantidade a ser separada
 * @return Novo item com quantidade separada ou nullptr se falhar
 */
Item* Item::split(uint32_t count);

/**
 * Une item com outro item
 * @param other Item a ser unido
 * @return true se união bem-sucedida
 */
bool Item::merge(Item* other);

/**
 * Verifica se item pode ser empilhado
 * @return true se pode empilhar
 */
bool Item::isStackable() const;

/**
 * Verifica se item pode ser movido
 * @return true se pode mover
 */
bool Item::isMovable() const;
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
/**
 * Move item para nova posição
 * @param newPos Nova posição
 * @return true se movimento bem-sucedido
 */
bool Item::moveTo(const Position& newPos);

/**
 * Divide item em duas partes
 * @param count Quantidade a ser separada
 * @return Novo item com quantidade separada ou nullptr se falhar
 */
Item* Item::split(uint32_t count);

/**
 * Une item com outro item
 * @param other Item a ser unido
 * @return true se união bem-sucedida
 */
bool Item::merge(Item* other);

/**
 * Verifica se item pode ser empilhado
 * @return true se pode empilhar
 */
bool Item::isStackable() const;

/**
 * Verifica se item pode ser movido
 * @return true se pode mover
 */
bool Item::isMovable() const;
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

---

## 📜 **Scripting APIs**

### **🐍 Lua Integration**

#### **LuaManager Class**
#### Nível Basic
```cpp
/**
 * Inicializa o interpretador Lua
 * @return true se inicialização bem-sucedida
 */
bool LuaManager::initialize();

/**
 * Finaliza o interpretador Lua
 */
void LuaManager::shutdown();

/**
 * Executa script Lua
 * @param script Código Lua
 * @return true se execução bem-sucedida
 */
bool LuaManager::executeScript(const std::string& script);

/**
 * Executa arquivo Lua
 * @param filename Nome do arquivo
 * @return true se execução bem-sucedida
 */
bool LuaManager::executeFile(const std::string& filename);

/**
 * Registra função C++ no Lua
 * @param name Nome da função
 * @param func Ponteiro para função
 */
void LuaManager::registerFunction(const std::string& name, lua_CFunction func);
```

#### Nível Intermediate
```cpp
/**
 * Inicializa o interpretador Lua
 * @return true se inicialização bem-sucedida
 */
bool LuaManager::initialize();

/**
 * Finaliza o interpretador Lua
 */
void LuaManager::shutdown();

/**
 * Executa script Lua
 * @param script Código Lua
 * @return true se execução bem-sucedida
 */
bool LuaManager::executeScript(const std::string& script);

/**
 * Executa arquivo Lua
 * @param filename Nome do arquivo
 * @return true se execução bem-sucedida
 */
bool LuaManager::executeFile(const std::string& filename);

/**
 * Registra função C++ no Lua
 * @param name Nome da função
 * @param func Ponteiro para função
 */
void LuaManager::registerFunction(const std::string& name, lua_CFunction func);
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
/**
 * Inicializa o interpretador Lua
 * @return true se inicialização bem-sucedida
 */
bool LuaManager::initialize();

/**
 * Finaliza o interpretador Lua
 */
void LuaManager::shutdown();

/**
 * Executa script Lua
 * @param script Código Lua
 * @return true se execução bem-sucedida
 */
bool LuaManager::executeScript(const std::string& script);

/**
 * Executa arquivo Lua
 * @param filename Nome do arquivo
 * @return true se execução bem-sucedida
 */
bool LuaManager::executeFile(const std::string& filename);

/**
 * Registra função C++ no Lua
 * @param name Nome da função
 * @param func Ponteiro para função
 */
void LuaManager::registerFunction(const std::string& name, lua_CFunction func);
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

#### **Event System**
#### Nível Basic
```cpp
/**
 * Registra handler para evento
 * @param eventName Nome do evento
 * @param handler Função handler
 */
void EventSystem::registerHandler(const std::string& eventName, EventHandler handler);

/**
 * Remove handler de evento
 * @param eventName Nome do evento
 * @param handler Função handler
 */
void EventSystem::unregisterHandler(const std::string& eventName, EventHandler handler);

/**
 * Dispara um evento
 * @param eventName Nome do evento
 * @param data Dados do evento
 */
void EventSystem::triggerEvent(const std::string& eventName, const EventData& data);

/**
 * Obtém lista de eventos registrados
 * @return Lista de nomes de eventos
 */
std::vector<std::string> EventSystem::getRegisteredEvents() const;
```

#### Nível Intermediate
```cpp
/**
 * Registra handler para evento
 * @param eventName Nome do evento
 * @param handler Função handler
 */
void EventSystem::registerHandler(const std::string& eventName, EventHandler handler);

/**
 * Remove handler de evento
 * @param eventName Nome do evento
 * @param handler Função handler
 */
void EventSystem::unregisterHandler(const std::string& eventName, EventHandler handler);

/**
 * Dispara um evento
 * @param eventName Nome do evento
 * @param data Dados do evento
 */
void EventSystem::triggerEvent(const std::string& eventName, const EventData& data);

/**
 * Obtém lista de eventos registrados
 * @return Lista de nomes de eventos
 */
std::vector<std::string> EventSystem::getRegisteredEvents() const;
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
/**
 * Registra handler para evento
 * @param eventName Nome do evento
 * @param handler Função handler
 */
void EventSystem::registerHandler(const std::string& eventName, EventHandler handler);

/**
 * Remove handler de evento
 * @param eventName Nome do evento
 * @param handler Função handler
 */
void EventSystem::unregisterHandler(const std::string& eventName, EventHandler handler);

/**
 * Dispara um evento
 * @param eventName Nome do evento
 * @param data Dados do evento
 */
void EventSystem::triggerEvent(const std::string& eventName, const EventData& data);

/**
 * Obtém lista de eventos registrados
 * @return Lista de nomes de eventos
 */
std::vector<std::string> EventSystem::getRegisteredEvents() const;
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

---

## 🔧 **Utility APIs**

### **📊 Position Class**
#### Nível Basic
```cpp
/**
 * Construtor padrão
 */
Position::Position();

/**
 * Construtor com coordenadas
 * @param x Coordenada X
 * @param y Coordenada Y
 * @param z Coordenada Z
 */
Position::Position(uint16_t x, uint16_t y, uint8_t z);

/**
 * Obtém coordenada X
 * @return Valor X
 */
uint16_t Position::getX() const;

/**
 * Define coordenada X
 * @param x Novo valor X
 */
void Position::setX(uint16_t x);

/**
 * Obtém coordenada Y
 * @return Valor Y
 */
uint16_t Position::getY() const;

/**
 * Define coordenada Y
 * @param y Novo valor Y
 */
void Position::setY(uint16_t y);

/**
 * Obtém coordenada Z
 * @return Valor Z
 */
uint8_t Position::getZ() const;

/**
 * Define coordenada Z
 * @param z Novo valor Z
 */
void Position::setZ(uint8_t z);

/**
 * Calcula distância até outra posição
 * @param other Outra posição
 * @return Distância calculada
 */
double Position::distanceTo(const Position& other) const;

/**
 * Verifica se posição é válida
 * @return true se posição válida
 */
bool Position::isValid() const;
```

#### Nível Intermediate
```cpp
/**
 * Construtor padrão
 */
Position::Position();

/**
 * Construtor com coordenadas
 * @param x Coordenada X
 * @param y Coordenada Y
 * @param z Coordenada Z
 */
Position::Position(uint16_t x, uint16_t y, uint8_t z);

/**
 * Obtém coordenada X
 * @return Valor X
 */
uint16_t Position::getX() const;

/**
 * Define coordenada X
 * @param x Novo valor X
 */
void Position::setX(uint16_t x);

/**
 * Obtém coordenada Y
 * @return Valor Y
 */
uint16_t Position::getY() const;

/**
 * Define coordenada Y
 * @param y Novo valor Y
 */
void Position::setY(uint16_t y);

/**
 * Obtém coordenada Z
 * @return Valor Z
 */
uint8_t Position::getZ() const;

/**
 * Define coordenada Z
 * @param z Novo valor Z
 */
void Position::setZ(uint8_t z);

/**
 * Calcula distância até outra posição
 * @param other Outra posição
 * @return Distância calculada
 */
double Position::distanceTo(const Position& other) const;

/**
 * Verifica se posição é válida
 * @return true se posição válida
 */
bool Position::isValid() const;
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
/**
 * Construtor padrão
 */
Position::Position();

/**
 * Construtor com coordenadas
 * @param x Coordenada X
 * @param y Coordenada Y
 * @param z Coordenada Z
 */
Position::Position(uint16_t x, uint16_t y, uint8_t z);

/**
 * Obtém coordenada X
 * @return Valor X
 */
uint16_t Position::getX() const;

/**
 * Define coordenada X
 * @param x Novo valor X
 */
void Position::setX(uint16_t x);

/**
 * Obtém coordenada Y
 * @return Valor Y
 */
uint16_t Position::getY() const;

/**
 * Define coordenada Y
 * @param y Novo valor Y
 */
void Position::setY(uint16_t y);

/**
 * Obtém coordenada Z
 * @return Valor Z
 */
uint8_t Position::getZ() const;

/**
 * Define coordenada Z
 * @param z Novo valor Z
 */
void Position::setZ(uint8_t z);

/**
 * Calcula distância até outra posição
 * @param other Outra posição
 * @return Distância calculada
 */
double Position::distanceTo(const Position& other) const;

/**
 * Verifica se posição é válida
 * @return true se posição válida
 */
bool Position::isValid() const;
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

### **📋 GameConfig Class**
#### Nível Basic
```cpp
/**
 * Obtém valor de configuração
 * @param key Chave da configuração
 * @return Valor da configuração
 */
std::string GameConfig::getValue(const std::string& key) const;

/**
 * Define valor de configuração
 * @param key Chave da configuração
 * @param value Valor da configuração
 */
void GameConfig::setValue(const std::string& key, const std::string& value);

/**
 * Carrega configuração de arquivo
 * @param filename Nome do arquivo
 * @return true se carregamento bem-sucedido
 */
bool GameConfig::loadFromFile(const std::string& filename);

/**
 * Salva configuração em arquivo
 * @param filename Nome do arquivo
 * @return true se salvamento bem-sucedido
 */
bool GameConfig::saveToFile(const std::string& filename) const;
```

#### Nível Intermediate
```cpp
/**
 * Obtém valor de configuração
 * @param key Chave da configuração
 * @return Valor da configuração
 */
std::string GameConfig::getValue(const std::string& key) const;

/**
 * Define valor de configuração
 * @param key Chave da configuração
 * @param value Valor da configuração
 */
void GameConfig::setValue(const std::string& key, const std::string& value);

/**
 * Carrega configuração de arquivo
 * @param filename Nome do arquivo
 * @return true se carregamento bem-sucedido
 */
bool GameConfig::loadFromFile(const std::string& filename);

/**
 * Salva configuração em arquivo
 * @param filename Nome do arquivo
 * @return true se salvamento bem-sucedido
 */
bool GameConfig::saveToFile(const std::string& filename) const;
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
/**
 * Obtém valor de configuração
 * @param key Chave da configuração
 * @return Valor da configuração
 */
std::string GameConfig::getValue(const std::string& key) const;

/**
 * Define valor de configuração
 * @param key Chave da configuração
 * @param value Valor da configuração
 */
void GameConfig::setValue(const std::string& key, const std::string& value);

/**
 * Carrega configuração de arquivo
 * @param filename Nome do arquivo
 * @return true se carregamento bem-sucedido
 */
bool GameConfig::loadFromFile(const std::string& filename);

/**
 * Salva configuração em arquivo
 * @param filename Nome do arquivo
 * @return true se salvamento bem-sucedido
 */
bool GameConfig::saveToFile(const std::string& filename) const;
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

---

## 📝 **Exemplos de Uso**

### **🎮 Exemplo: Criação de Jogador**
#### Nível Basic
```cpp
// Criar novo jogador
auto game = GameManager::getInstance()->getGame();
auto player = game->createPlayer("PlayerName");

if (player) {
    // Configurar propriedades iniciais
    player->setPosition(Position(100, 100, 7));
    player->setHealth(150);
    player->setMana(50);
    player->setLevel(1);
    
    // Adicionar item inicial
    auto inventory = game->getInventorySystem();
    auto sword = inventory->createItem(ItemType::SWORD);
    inventory->addItem(player, sword, 0);
    
    std::cout << "Jogador criado com sucesso!" << std::endl;
}
```

#### Nível Intermediate
```cpp
// Criar novo jogador
auto game = GameManager::getInstance()->getGame();
auto player = game->createPlayer("PlayerName");

if (player) {
    // Configurar propriedades iniciais
    player->setPosition(Position(100, 100, 7));
    player->setHealth(150);
    player->setMana(50);
    player->setLevel(1);
    
    // Adicionar item inicial
    auto inventory = game->getInventorySystem();
    auto sword = inventory->createItem(ItemType::SWORD);
    inventory->addItem(player, sword, 0);
    
    std::cout << "Jogador criado com sucesso!" << std::endl;
}
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
// Criar novo jogador
auto game = GameManager::getInstance()->getGame();
auto player = game->createPlayer("PlayerName");

if (player) {
    // Configurar propriedades iniciais
    player->setPosition(Position(100, 100, 7));
    player->setHealth(150);
    player->setMana(50);
    player->setLevel(1);
    
    // Adicionar item inicial
    auto inventory = game->getInventorySystem();
    auto sword = inventory->createItem(ItemType::SWORD);
    inventory->addItem(player, sword, 0);
    
    std::cout << "Jogador criado com sucesso!" << std::endl;
}
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

### **⚔️ Exemplo: Sistema de Combate**
#### Nível Basic
```cpp
// Criar combate entre jogador e monstro
auto combat = game->getCombatSystem();
auto player = game->getPlayer("PlayerName");
auto monster = game->createCreature(CreatureType::RAT, Position(101, 100, 7));

if (player && monster) {
    // Configurar alvos
    player->setTarget(monster);
    monster->setTarget(player);
    
    // Executar ataque
    if (combat->attack(player, monster)) {
        uint32_t damage = combat->calculateDamage(WeaponType::SWORD, *player);
        monster->takeDamage(damage, player);
        
        std::cout << "Ataque executado! Dano: " << damage << std::endl;
    }
}
```

#### Nível Intermediate
```cpp
// Criar combate entre jogador e monstro
auto combat = game->getCombatSystem();
auto player = game->getPlayer("PlayerName");
auto monster = game->createCreature(CreatureType::RAT, Position(101, 100, 7));

if (player && monster) {
    // Configurar alvos
    player->setTarget(monster);
    monster->setTarget(player);
    
    // Executar ataque
    if (combat->attack(player, monster)) {
        uint32_t damage = combat->calculateDamage(WeaponType::SWORD, *player);
        monster->takeDamage(damage, player);
        
        std::cout << "Ataque executado! Dano: " << damage << std::endl;
    }
}
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
// Criar combate entre jogador e monstro
auto combat = game->getCombatSystem();
auto player = game->getPlayer("PlayerName");
auto monster = game->createCreature(CreatureType::RAT, Position(101, 100, 7));

if (player && monster) {
    // Configurar alvos
    player->setTarget(monster);
    monster->setTarget(player);
    
    // Executar ataque
    if (combat->attack(player, monster)) {
        uint32_t damage = combat->calculateDamage(WeaponType::SWORD, *player);
        monster->takeDamage(damage, player);
        
        std::cout << "Ataque executado! Dano: " << damage << std::endl;
    }
}
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

### **🌐 Exemplo: Comunicação de Rede**
#### Nível Basic
```cpp
// Processar pacote de login
auto network = GameManager::getInstance()->getNetwork();
auto protocol = network->getProtocolHandler();

// Criar pacote de login
auto loginData = PacketData();
loginData.setString("username", "PlayerName");
loginData.setString("password", "Password123");

auto loginPacket = protocol->createPacket(PacketType::LOGIN, loginData);

// Enviar pacote
auto connection = network->acceptConnection();
if (connection) {
    network->sendData(connection, loginPacket);
    std::cout << "Pacote de login enviado!" << std::endl;
}
```

#### Nível Intermediate
```cpp
// Processar pacote de login
auto network = GameManager::getInstance()->getNetwork();
auto protocol = network->getProtocolHandler();

// Criar pacote de login
auto loginData = PacketData();
loginData.setString("username", "PlayerName");
loginData.setString("password", "Password123");

auto loginPacket = protocol->createPacket(PacketType::LOGIN, loginData);

// Enviar pacote
auto connection = network->acceptConnection();
if (connection) {
    network->sendData(connection, loginPacket);
    std::cout << "Pacote de login enviado!" << std::endl;
}
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```cpp
// Processar pacote de login
auto network = GameManager::getInstance()->getNetwork();
auto protocol = network->getProtocolHandler();

// Criar pacote de login
auto loginData = PacketData();
loginData.setString("username", "PlayerName");
loginData.setString("password", "Password123");

auto loginPacket = protocol->createPacket(PacketType::LOGIN, loginData);

// Enviar pacote
auto connection = network->acceptConnection();
if (connection) {
    network->sendData(connection, loginPacket);
    std::cout << "Pacote de login enviado!" << std::endl;
}
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

### **💾 Exemplo: Operações de Banco**
#### Nível Basic
```cpp
if (database->beginTransaction()) {
        if (database->executeUpdate(query)) {
                if (inventory[i]) {
            std::cout << "Dados salvos com sucesso!" << std::endl;
        std::cerr << "Erro ao salvar dados!" << std::endl;
```

#### Nível Intermediate
```cpp
// Salvar dados do jogador
auto database = GameManager::getInstance()->getDatabase();

// Iniciar transação
if (database->beginTransaction()) {
    try {
        // Salvar informações básicas
        std::string query = "UPDATE players SET level = " + 
                           std::to_string(player->getLevel()) + 
                           ", experience = " + 
                           std::to_string(player->getExperience()) + 
                           " WHERE name = '" + player->getName() + "'";
        
        if (database->executeUpdate(query)) {
            // Salvar inventário
            auto inventory = player->getInventory();
            for (size_t i = 0; i < inventory.size(); ++i) {
                if (inventory[i]) {
                    query = "INSERT INTO player_items (player_name, slot, item_id) VALUES ('" +
                           player->getName() + "', " + std::to_string(i) + ", " +
                           std::to_string(inventory[i]->getId()) + ")";
                    database->executeInsert(query);
                }
            }
            
            database->commitTransaction();
            std::cout << "Dados salvos com sucesso!" << std::endl;
        }
    } catch (...) {
        database->rollbackTransaction();
        std::cerr << "Erro ao salvar dados!" << std::endl;
    }
}
```

#### Nível Advanced
```cpp
// Salvar dados do jogador
auto database = GameManager::getInstance()->getDatabase();

// Iniciar transação
if (database->beginTransaction()) {
    try {
        // Salvar informações básicas
        std::string query = "UPDATE players SET level = " + 
                           std::to_string(player->getLevel()) + 
                           ", experience = " + 
                           std::to_string(player->getExperience()) + 
                           " WHERE name = '" + player->getName() + "'";
        
        if (database->executeUpdate(query)) {
            // Salvar inventário
            auto inventory = player->getInventory();
            for (size_t i = 0; i < inventory.size(); ++i) {
                if (inventory[i]) {
                    query = "INSERT INTO player_items (player_name, slot, item_id) VALUES ('" +
                           player->getName() + "', " + std::to_string(i) + ", " +
                           std::to_string(inventory[i]->getId()) + ")";
                    database->executeInsert(query);
                }
            }
            
            database->commitTransaction();
            std::cout << "Dados salvos com sucesso!" << std::endl;
        }
    } catch (...) {
        database->rollbackTransaction();
        std::cerr << "Erro ao salvar dados!" << std::endl;
    }
}
-- Adicionar metatable para funcionalidade avançada
local mt = {
    __index = function(t, k)
        return rawget(t, k) or 'Valor não encontrado'
    end
    __call = function(t, ...)
        print('Objeto chamado com:', ...)
    end
}
setmetatable(meuObjeto, mt)
```

---

## 🔄 **Status da Documentação**

### **✅ Concluído**
- [x] APIs do Game Engine documentadas
- [x] APIs de Network Layer documentadas
- [x] APIs de Database System documentadas
- [x] APIs de Game Objects documentadas
- [x] Exemplos de uso criados

### **🔄 Em Progresso**
- [ ] Documentação de APIs de Scripting
- [ ] Documentação de APIs de Utilitários
- [ ] Exemplos avançados de uso

### **⏳ Pendente**
- [ ] Documentação de APIs internas
- [ ] Guias de integração
- [ ] Troubleshooting de APIs

---

**Documento Criado**: 2025-01-27  
**Responsável**: Deep Source Analyzer  
**Status**: 🔄 **Documentação em Progresso**  
**Próximo**: 🎨 **Design Patterns** 