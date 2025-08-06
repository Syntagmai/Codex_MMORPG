---
tags: [integration, open_codes, protocol, otclient, canary, wiki, canary_otclient]
type: wiki_page
status: active
priority: high
created: 2025-08-05
updated: 2025-08-05
aliases: [Open Codes, Protocolo Open, Códigos Abertos, Protocolo Básico]
---

# 🔓 **Open Codes - Protocolo Básico**

> [!info] **Baseado na Pesquisa Habdel**
> Esta página é baseada na pesquisa detalhada da **[INTEGRATION-003: Análise de Protocolos](../../habdel/INTEGRATION-003.md)** realizada pelo sistema Habdel.

---

## 🎯 **Visão Geral**

Os **Open Codes** são o protocolo básico de comunicação entre OTClient e Canary, fornecendo uma base fundamental para todas as operações de jogo. Este protocolo define os códigos de mensagem padrão, estrutura de dados e fluxos de comunicação essenciais.

### **Características Principais**
- **Protocolo binário** simples e eficiente
- **Códigos de mensagem** padronizados
- **Estrutura de dados** consistente
- **Compatibilidade** entre cliente e servidor
- **Extensibilidade** para funcionalidades avançadas

---

## 📋 **Estrutura do Protocolo Open Codes**

### **🔢 Códigos de Mensagem Base**

#### **Mensagens do Cliente para Servidor (0x01 - 0x7F)**
```lua
-- Códigos de mensagem do cliente
local ClientCodes = {
    -- Autenticação
    LOGIN = 0x01,
    LOGOUT = 0x02,
    
    -- Movimento
    MOVE_NORTH = 0x10,
    MOVE_EAST = 0x11,
    MOVE_SOUTH = 0x12,
    MOVE_WEST = 0x13,
    MOVE_NORTHEAST = 0x14,
    MOVE_NORTHWEST = 0x15,
    MOVE_SOUTHEAST = 0x16,
    MOVE_SOUTHWEST = 0x17,
    
    -- Ações
    ATTACK = 0x20,
    USE_ITEM = 0x21,
    USE_ITEM_WITH = 0x22,
    USE_ITEM_ON_CREATURE = 0x23,
    USE_ITEM_ON_TILE = 0x24,
    
    -- Chat
    SAY = 0x30,
    WHISPER = 0x31,
    YELL = 0x32,
    PRIVATE_MESSAGE = 0x33,
    
    -- Inventário
    OPEN_CONTAINER = 0x40,
    CLOSE_CONTAINER = 0x41,
    MOVE_ITEM = 0x42,
    USE_ITEM_FROM_CONTAINER = 0x43,
    
    -- Comércio
    REQUEST_TRADE = 0x50,
    ACCEPT_TRADE = 0x51,
    REJECT_TRADE = 0x52,
    TRADE_ITEM = 0x53,
    TRADE_ACCEPT = 0x54,
    TRADE_CANCEL = 0x55,
    
    -- Outros
    PING = 0x60,
    PONG = 0x61,
    REQUEST_INFO = 0x62
}
```

#### **Mensagens do Servidor para Cliente (0x80 - 0xFF)**
```lua
-- Códigos de mensagem do servidor
local ServerCodes = {
    -- Respostas de autenticação
    LOGIN_RESPONSE = 0x81,
    LOGOUT_RESPONSE = 0x82,
    
    -- Atualizações de jogo
    PLAYER_UPDATE = 0x90,
    CREATURE_UPDATE = 0x91,
    ITEM_UPDATE = 0x92,
    MAP_UPDATE = 0x93,
    
    -- Chat
    CHAT_MESSAGE = 0xA0,
    PRIVATE_MESSAGE = 0xA1,
    SYSTEM_MESSAGE = 0xA2,
    
    -- Inventário
    CONTAINER_OPEN = 0xB0,
    CONTAINER_CLOSE = 0xB1,
    CONTAINER_UPDATE = 0xB2,
    
    -- Comércio
    TRADE_REQUEST = 0xC0,
    TRADE_RESPONSE = 0xC1,
    TRADE_UPDATE = 0xC2,
    TRADE_COMPLETE = 0xC3,
    
    -- Outros
    PING_RESPONSE = 0xD0,
    INFO_RESPONSE = 0xD1,
    ERROR_MESSAGE = 0xE0
}
```

---

## 🏗️ **Implementação do Protocolo**

### **📡 Sistema de Mensagens - OTClient**
```lua
-- Sistema de mensagens Open Codes no OTClient
local OpenCodeSystem = {}

function OpenCodeSystem:init()
    self.clientCodes = ClientCodes
    self.serverCodes = ServerCodes
    self.messageHandlers = {}
    self.sequenceNumber = 0
end

function OpenCodeSystem:createMessage(code, data)
    local message = {
        header = 0xAA55AA55, -- Magic number
        length = 0,
        code = code,
        sequence = self:getNextSequence(),
        data = data or {},
        checksum = 0
    }
    
    -- Serializar dados
    local serializedData = self:serializeData(message.data)
    message.length = #serializedData
    
    -- Calcular checksum
    message.checksum = self:calculateChecksum(serializedData)
    
    return message
end

function OpenCodeSystem:sendMessage(code, data)
    local message = self:createMessage(code, data)
    
    -- Enviar para servidor
    if g_network then
        g_network:sendMessage(message)
    end
    
    return message.sequence
end

function OpenCodeSystem:handleIncomingMessage(rawData)
    -- Parsear mensagem
    local message = self:parseMessage(rawData)
    
    -- Verificar checksum
    if not self:verifyChecksum(message) then
        print("Checksum verification failed")
        return
    end
    
    -- Processar mensagem
    self:processMessage(message)
end

function OpenCodeSystem:processMessage(message)
    local handler = self.messageHandlers[message.code]
    if handler then
        handler(message.data)
    else
        print("Unknown message code: 0x" .. string.format("%02X", message.code))
    end
end

function OpenCodeSystem:registerHandler(code, handler)
    self.messageHandlers[code] = handler
end

function OpenCodeSystem:getNextSequence()
    self.sequenceNumber = self.sequenceNumber + 1
    if self.sequenceNumber > 65535 then
        self.sequenceNumber = 1
    end
    return self.sequenceNumber
end

-- Exemplo de handlers
OpenCodeSystem:registerHandler(OpenCodeSystem.serverCodes.LOGIN_RESPONSE, function(data)
    if data.success then
        print("Login successful")
        g_game:setPlayer(data.playerData)
        g_ui:showGameInterface()
    else
        print("Login failed: " .. data.error)
        g_ui:showLoginError(data.error)
    end
end)

OpenCodeSystem:registerHandler(OpenCodeSystem.serverCodes.PLAYER_UPDATE, function(data)
    g_game:updatePlayer(data)
end)

OpenCodeSystem:registerHandler(OpenCodeSystem.serverCodes.MAP_UPDATE, function(data)
    g_map:updateMap(data)
end)

OpenCodeSystem:registerHandler(OpenCodeSystem.serverCodes.CHAT_MESSAGE, function(data)
    g_chat:addMessage(data)
end)
```

### **📡 Sistema de Mensagens - Canary**
```cpp
// Sistema de mensagens Open Codes no Canary
class OpenCodeSystem {
private:
    std::map<uint8_t, std::function<void(const NetworkMessage&)>> messageHandlers;
    uint16_t sequenceNumber;
    
public:
    OpenCodeSystem() : sequenceNumber(0) {
        registerDefaultHandlers();
    }
    
    void handleIncomingMessage(const NetworkMessage& message) {
        // Parsear cabeçalho
        uint32_t header = message.getU32();
        if (header != 0xAA55AA55) {
            std::cerr << "Invalid message header" << std::endl;
            return;
        }
        
        uint16_t length = message.getU16();
        uint8_t code = message.getU8();
        uint16_t sequence = message.getU16();
        
        // Verificar checksum
        uint16_t receivedChecksum = message.getU16();
        uint16_t calculatedChecksum = calculateChecksum(message);
        
        if (receivedChecksum != calculatedChecksum) {
            std::cerr << "Checksum verification failed" << std::endl;
            return;
        }
        
        // Processar mensagem
        processMessage(code, message);
    }
    
    void processMessage(uint8_t code, const NetworkMessage& message) {
        auto handler = messageHandlers.find(code);
        if (handler != messageHandlers.end()) {
            handler->second(message);
        } else {
            std::cerr << "Unknown message code: 0x" << std::hex << (int)code << std::endl;
        }
    }
    
    void registerHandler(uint8_t code, std::function<void(const NetworkMessage&)> handler) {
        messageHandlers[code] = handler;
    }
    
    void sendMessage(uint8_t code, const NetworkMessage& data, Connection* connection) {
        // Criar mensagem
        NetworkMessage message;
        message.addU32(0xAA55AA55); // Header
        message.addU16(0); // Length placeholder
        message.addU8(code);
        message.addU16(getNextSequence());
        message.addMessage(data);
        
        // Atualizar comprimento
        uint16_t length = message.getSize() - 8; // Excluir header e length
        message.setU16(4, length);
        
        // Calcular e adicionar checksum
        uint16_t checksum = calculateChecksum(message);
        message.addU16(checksum);
        
        // Enviar
        connection->sendMessage(message);
    }
    
private:
    void registerDefaultHandlers() {
        // Handler para login
        registerHandler(0x01, [this](const NetworkMessage& message) {
            handleClientLogin(message);
        });
        
        // Handler para movimento
        registerHandler(0x10, [this](const NetworkMessage& message) {
            handleClientMove(message, 0); // North
        });
        registerHandler(0x11, [this](const NetworkMessage& message) {
            handleClientMove(message, 1); // East
        });
        registerHandler(0x12, [this](const NetworkMessage& message) {
            handleClientMove(message, 2); // South
        });
        registerHandler(0x13, [this](const NetworkMessage& message) {
            handleClientMove(message, 3); // West
        });
        
        // Handler para ataque
        registerHandler(0x20, [this](const NetworkMessage& message) {
            handleClientAttack(message);
        });
        
        // Handler para uso de item
        registerHandler(0x21, [this](const NetworkMessage& message) {
            handleClientUseItem(message);
        });
        
        // Handler para chat
        registerHandler(0x30, [this](const NetworkMessage& message) {
            handleClientSay(message);
        });
    }
    
    void handleClientLogin(const NetworkMessage& message) {
        std::string account = message.getString();
        std::string password = message.getString();
        uint16_t clientVersion = message.getU16();
        
        // Autenticar usuário
        auto player = g_accounts->authenticate(account, password);
        if (player) {
            // Enviar resposta de sucesso
            NetworkMessage response;
            response.addU8(1); // Success
            response.addU32(player->getId());
            response.addString(player->getName());
            response.addU32(player->getLevel());
            response.addU32(player->getHealth());
            response.addU32(player->getMaxHealth());
            
            sendMessage(0x81, response, message.getConnection());
        } else {
            // Enviar resposta de erro
            NetworkMessage response;
            response.addU8(0); // Failure
            response.addString("Invalid credentials");
            
            sendMessage(0x81, response, message.getConnection());
        }
    }
    
    void handleClientMove(const NetworkMessage& message, uint8_t direction) {
        uint32_t playerId = message.getU32();
        
        auto player = g_players->getPlayer(playerId);
        if (player) {
            // Processar movimento
            Position newPos = player->getPosition();
            switch (direction) {
                case 0: newPos.y--; break; // North
                case 1: newPos.x++; break; // East
                case 2: newPos.y++; break; // South
                case 3: newPos.x--; break; // West
            }
            
            if (g_map->canMoveTo(player, newPos)) {
                player->setPosition(newPos);
                
                // Notificar outros jogadores
                notifyPlayerMove(player, newPos);
            }
        }
    }
    
    void handleClientAttack(const NetworkMessage& message) {
        uint32_t playerId = message.getU32();
        uint32_t targetId = message.getU32();
        
        auto player = g_players->getPlayer(playerId);
        auto target = g_creatures->getCreature(targetId);
        
        if (player && target) {
            // Processar ataque
            g_combat->processAttack(player, target);
        }
    }
    
    void handleClientUseItem(const NetworkMessage& message) {
        uint32_t playerId = message.getU32();
        uint32_t itemId = message.getU32();
        Position position = message.getPosition();
        
        auto player = g_players->getPlayer(playerId);
        auto item = g_items->getItem(itemId);
        
        if (player && item) {
            // Processar uso do item
            g_items->useItem(player, item, position);
        }
    }
    
    void handleClientSay(const NetworkMessage& message) {
        uint32_t playerId = message.getU32();
        std::string text = message.getString();
        
        auto player = g_players->getPlayer(playerId);
        if (player) {
            // Processar chat
            g_chat->processMessage(player, text, 0); // 0 = Say
        }
    }
    
    uint16_t getNextSequence() {
        sequenceNumber++;
        if (sequenceNumber > 65535) {
            sequenceNumber = 1;
        }
        return sequenceNumber;
    }
    
    uint16_t calculateChecksum(const NetworkMessage& message) {
        uint16_t checksum = 0;
        for (size_t i = 0; i < message.getSize(); i++) {
            checksum += message.getByte(i);
        }
        return checksum;
    }
};
```

---

## 🛠️ **Exemplos Práticos**

### **Exemplo 1: Sistema de Login**
```lua
-- Exemplo: Sistema de login com Open Codes
local LoginSystem = {}

function LoginSystem:init()
    self.openCodeSystem = OpenCodeSystem:new()
    self.openCodeSystem:init()
end

function LoginSystem:login(account, password)
    -- Criar dados de login
    local loginData = {
        account = account,
        password = password,
        clientVersion = g_app.getVersion(),
        timestamp = os.time()
    }
    
    -- Enviar mensagem de login
    local sequence = self.openCodeSystem:sendMessage(
        self.openCodeSystem.clientCodes.LOGIN,
        loginData
    )
    
    -- Mostrar loading
    g_ui:showLoading("Connecting to server...")
    
    return sequence
end

function LoginSystem:handleLoginResponse(data)
    if data.success then
        -- Login bem-sucedido
        g_game:setPlayer(data.playerData)
        g_ui:hideLoading()
        g_ui:showGameInterface()
        
        -- Configurar eventos de jogo
        self:setupGameEvents()
    else
        -- Login falhou
        g_ui:hideLoading()
        g_ui:showError("Login failed: " .. data.error)
    end
end

function LoginSystem:setupGameEvents()
    -- Registrar handlers para eventos de jogo
    self.openCodeSystem:registerHandler(
        self.openCodeSystem.serverCodes.PLAYER_UPDATE,
        function(data)
            g_game:updatePlayer(data)
        end
    )
    
    self.openCodeSystem:registerHandler(
        self.openCodeSystem.serverCodes.MAP_UPDATE,
        function(data)
            g_map:updateMap(data)
        end
    )
    
    self.openCodeSystem:registerHandler(
        self.openCodeSystem.serverCodes.CHAT_MESSAGE,
        function(data)
            g_chat:addMessage(data)
        end
    )
end
```

### **Exemplo 2: Sistema de Movimento**
```lua
-- Exemplo: Sistema de movimento com Open Codes
local MovementSystem = {}

function MovementSystem:init()
    self.openCodeSystem = OpenCodeSystem:new()
    self.openCodeSystem:init()
end

function MovementSystem:move(direction)
    local directionCodes = {
        north = self.openCodeSystem.clientCodes.MOVE_NORTH,
        east = self.openCodeSystem.clientCodes.MOVE_EAST,
        south = self.openCodeSystem.clientCodes.MOVE_SOUTH,
        west = self.openCodeSystem.clientCodes.MOVE_WEST,
        northeast = self.openCodeSystem.clientCodes.MOVE_NORTHEAST,
        northwest = self.openCodeSystem.clientCodes.MOVE_NORTHWEST,
        southeast = self.openCodeSystem.clientCodes.MOVE_SOUTHEAST,
        southwest = self.openCodeSystem.clientCodes.MOVE_SOUTHWEST
    }
    
    local code = directionCodes[direction]
    if code then
        local moveData = {
            playerId = g_game:getPlayerId(),
            direction = direction,
            timestamp = os.time()
        }
        
        self.openCodeSystem:sendMessage(code, moveData)
    end
end

function MovementSystem:handleMovementResponse(data)
    if data.success then
        -- Movimento bem-sucedido
        g_game:updatePlayerPosition(data.newPosition)
        g_map:updatePlayerPosition(data.newPosition)
    else
        -- Movimento falhou
        print("Movement failed: " .. data.error)
    end
end
```

### **Exemplo 3: Sistema de Chat**
```lua
-- Exemplo: Sistema de chat com Open Codes
local ChatSystem = {}

function ChatSystem:init()
    self.openCodeSystem = OpenCodeSystem:new()
    self.openCodeSystem:init()
end

function ChatSystem:sendMessage(text, type)
    type = type or "say"
    
    local chatTypes = {
        say = self.openCodeSystem.clientCodes.SAY,
        whisper = self.openCodeSystem.clientCodes.WHISPER,
        yell = self.openCodeSystem.clientCodes.YELL,
        private = self.openCodeSystem.clientCodes.PRIVATE_MESSAGE
    }
    
    local code = chatTypes[type]
    if code then
        local chatData = {
            text = text,
            type = type,
            timestamp = os.time()
        }
        
        self.openCodeSystem:sendMessage(code, chatData)
    end
end

function ChatSystem:handleChatMessage(data)
    local message = {
        sender = data.sender,
        text = data.text,
        type = data.type,
        timestamp = data.timestamp
    }
    
    -- Adicionar à interface de chat
    g_ui:addChatMessage(message)
    
    -- Processar comandos especiais
    if data.type == "private" then
        self:handlePrivateMessage(message)
    end
end

function ChatSystem:handlePrivateMessage(message)
    -- Mostrar notificação para mensagem privada
    g_ui:showNotification("Private message from " .. message.sender)
    
    -- Abrir janela de chat privado se não estiver aberta
    if not g_ui:isPrivateChatOpen(message.sender) then
        g_ui:openPrivateChat(message.sender)
    end
end
```

---

## 🔗 **Dependências e Integração**

### **Dependências Internas**
- **[[integracao_protocolo_comunicacao|Protocolo de Comunicação]]** - Sistema de comunicação
- **[[integracao_extended_open_codes|Extended Open Codes]]** - Protocolo avançado
- **[[integracao_sincronizacao_dados|Sincronização de Dados]]** - Sincronização

### **Dependências Externas**
- **TCP/IP** - Protocolo de transporte
- **Lua 5.1+** - Linguagem de scripting
- **C++** - Linguagem de implementação

### **Integração com Outros Sistemas**
```lua
-- Exemplo: Integração com sistema de rede
local NetworkSystem = require("modules/network_system")
local OpenCodeSystem = require("modules/open_code_system")

-- Configurar Open Codes
OpenCodeSystem:setNetworkSystem(NetworkSystem)
OpenCodeSystem:registerDefaultHandlers()

-- Iniciar sistema
OpenCodeSystem:start()
```

---

## 📚 **Referência de API**

### **Funções Principais**

#### **Message Management**
- `OpenCodeSystem:sendMessage(code, data)` - Envia mensagem
- `OpenCodeSystem:handleIncomingMessage(data)` - Processa mensagem recebida
- `OpenCodeSystem:registerHandler(code, handler)` - Registra handler

#### **Protocol Codes**
- `ClientCodes` - Códigos de mensagem do cliente
- `ServerCodes` - Códigos de mensagem do servidor

---

## 🎯 **Melhores Práticas**

### **1. Códigos de Mensagem**
```lua
-- ✅ Bom: Usar códigos padronizados
OpenCodeSystem:sendMessage(OpenCodeSystem.clientCodes.LOGIN, data)

-- ❌ Ruim: Usar códigos arbitrários
OpenCodeSystem:sendMessage(0x99, data) -- Código não padronizado
```

### **2. Tratamento de Erros**
```lua
-- ✅ Bom: Tratamento robusto de erros
local success, result = pcall(function()
    return OpenCodeSystem:handleMessage(message)
end)

if not success then
    print("Open Code error: " .. result)
end

-- ❌ Ruim: Ignorar erros
OpenCodeSystem:handleMessage(message) -- Sem tratamento
```

### **3. Sequenciamento**
```lua
-- ✅ Bom: Usar sequenciamento
local sequence = OpenCodeSystem:sendMessage(code, data)
print("Message sent with sequence: " .. sequence)

-- ❌ Ruim: Ignorar sequenciamento
OpenCodeSystem:sendMessage(code, data) -- Sem controle de sequência
```

---

## 🔍 **Debugging e Troubleshooting**

### **Debug de Open Codes**
```lua
-- Função para debug de Open Codes
function OpenCodeSystem:debugOpenCodes()
    print("=== Open Codes Debug ===")
    print("Client Codes: " .. #self.clientCodes)
    print("Server Codes: " .. #self.serverCodes)
    print("Message Handlers: " .. #self.messageHandlers)
    print("Sequence Number: " .. self.sequenceNumber)
    
    for code, handler in pairs(self.messageHandlers) do
        print("  Handler 0x" .. string.format("%02X", code) .. ": " .. tostring(handler))
    end
end
```

### **Debug de Mensagens**
```lua
-- Função para debug de mensagens
function OpenCodeSystem:debugMessage(message)
    print("=== Message Debug ===")
    print("Code: 0x" .. string.format("%02X", message.code))
    print("Sequence: " .. message.sequence)
    print("Length: " .. message.length)
    print("Checksum: 0x" .. string.format("%04X", message.checksum))
    
    if message.data then
        print("Data: " .. json.encode(message.data))
    end
end
```

---

## 📖 **Recursos Adicionais**

### **Documentação Relacionada**
- **[[integracao_protocolo_comunicacao|Protocolo de Comunicação]]** - Sistema de comunicação
- **[[integracao_extended_open_codes|Extended Open Codes]]** - Protocolo avançado
- **[[integracao_sincronizacao_dados|Sincronização de Dados]]** - Sincronização

### **Exemplos de Código**
- **[[integracao_exemplos_open_codes|Exemplos de Open Codes]]** - Exemplos práticos
- **[[integracao_implementacao_protocolo|Implementação de Protocolo]]** - Implementações

### **Ferramentas de Desenvolvimento**
- **[[integracao_ferramentas_protocolo|Ferramentas de Protocolo]]** - Ferramentas para desenvolvimento
- **[[integracao_debug_protocolo|Debug de Protocolo]]** - Ferramentas de debug

---

## 🎯 **Próximos Passos**

1. **Configure Open Codes** - Configure o sistema de Open Codes
2. **Implemente Handlers** - Implemente handlers para mensagens
3. **Teste Comunicação** - Teste a comunicação básica
4. **Otimize Performance** - Otimize para melhor performance
5. **Monitore Tráfego** - Monitore e analise o tráfego

---

> [!success] **Conclusão**
> Os Open Codes fornecem uma base sólida e padronizada para comunicação entre OTClient e Canary, com códigos de mensagem bem definidos e estrutura de dados consistente. 