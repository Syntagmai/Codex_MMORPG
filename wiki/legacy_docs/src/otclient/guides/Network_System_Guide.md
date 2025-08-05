
# Sistema de Rede

Sistema de comunicação de rede assíncrono com suporte a múltiplos protocolos, criptografia e reconexão automática.

## 📋 Índice

1. [Visão Geral](#visão-geral)
2. [API C++](#api-c)
3. [API Lua](#api-lua)
4. [Arquitetura de Conexão](#arquitetura-de-conexão)
5. [Sistema de Protocolo](#sistema-de-protocolo)
6. [Segurança e Criptografia](#segurança-e-criptografia)
7. [Exemplos Práticos](#exemplos-práticos)
8. [Melhores Práticas](#melhores-práticas)

## 🎯 Visão Geral

O sistema de rede do OTClient oferece comunicação assíncrona robusta com:

- **Conexões TCP assíncronas**: Baseadas em ASIO
- **Múltiplos protocolos**: Game, HTTP, WebSocket
- **Criptografia XTEA**: Segurança de dados
- **Reconexão automática**: Recuperação de falhas
- **Compressão**: Redução de tráfego de rede
- **Timeouts configuráveis**: Controle de latência

### 🔧 Fluxo de Comunicação

```
Cliente → Resolver DNS → Conectar → Handshake → Troca de Dados → Desconectar
```

## 🔧 API C++

### Connection Class
```cpp
class Connection : public LuaObject {
    -- Classe: Connection
public:
    // Configurações de timeout
    enum {
        READ_TIMEOUT = 30,      // 30 segundos para leitura
        WRITE_TIMEOUT = 30,     // 30 segundos para escrita
        SEND_BUFFER_SIZE = 65536,  // Buffer de envio (64KB)
        RECV_BUFFER_SIZE = 65536   // Buffer de recepção (64KB)
    };

    // Construtor/Destrutor
    Connection();
    ~Connection() override;

    // Métodos estáticos
    static void poll();          // Processa eventos de rede
    static void terminate();     // Termina todas as conexões

    // Gerenciamento de conexão
    void connect(std::string_view host, uint16_t port, 
                const std::function<void()>& connectCallback);
    void close();

    // Operações de I/O
    void write(const uint8_t* buffer, size_t size);
    void read(uint16_t bytes, const RecvCallback& callback);
    void read_until(std::string_view delimiter, const RecvCallback& callback);
    void read_some(const RecvCallback& callback);

    // Estado da conexão
    bool isConnecting() const;
    bool isConnected() const;
    int getIp();
    std::error_code getError() const;
    ticks_t getElapsedTicksSinceLastRead() const;

    // Callbacks
    void setErrorCallback(const ErrorCallback& errorCallback);

private:
    // Implementação interna
    asio::ip::tcp::resolver m_resolver;
    asio::ip::tcp::socket m_socket;
    asio::streambuf m_inputStream;
    std::shared_ptr<asio::streambuf> m_outputStream;
    
    // Timers
    asio::basic_waitable_timer<std::chrono::high_resolution_clock> m_readTimer;
    asio::basic_waitable_timer<std::chrono::high_resolution_clock> m_writeTimer;
    
    // Estado
    bool m_connected;
    bool m_connecting;
    std::error_code m_error;
    stdext::timer m_activityTimer;
};
```

### Protocol Class
```cpp
class Protocol : public LuaObject {
    -- Classe: Protocol
public:
    Protocol();
    ~Protocol() override;

    // Conexão
    void connect(std::string_view host, uint16_t port);
    void disconnect();

    // Estado
    bool isConnected();
    bool isConnecting();
    ticks_t getElapsedTicksSinceLastRead() const;

    // Criptografia XTEA
    void generateXteaKey();
    void setXteaKey(uint32_t a, uint32_t b, uint32_t c, uint32_t d);
    std::vector<uint32_t> getXteaKey();
    void enableXteaEncryption();

    // Recursos adicionais
    void enableChecksum();          // Verificação de integridade
    void enabledSequencedPackets(); // Numeração sequencial

    // I/O de mensagens
    virtual void send(const OutputMessagePtr& outputMessage);
    virtual void recv();

    // Gravação/Reprodução
    void setRecorder(PacketRecorderPtr recorder);
    void playRecord(PacketPlayerPtr player);

protected:
    // Callbacks virtuais
    virtual void onConnect();
    virtual void onRecv(const InputMessagePtr& inputMessage);
    virtual void onError(const std::error_code& err);
    virtual void onSend();

    // Criptografia
    std::array<uint32_t, 4> m_xteaKey;
    uint32_t m_packetNumber;
    bool m_xteaEncryptionEnabled;
    bool m_checksumEnabled;
    bool m_sequencedPackets;

private:
    ConnectionPtr m_connection;
    PacketRecorderPtr m_recorder;
    PacketPlayerPtr m_player;
};
```

### Message Classes
```cpp
// Mensagem de entrada
class InputMessage {
    -- Classe: InputMessage
public:
    // Leitura de dados
    uint8_t getU8();
    uint16_t getU16();
    uint32_t getU32();
    uint64_t getU64();
    std::string getString();
    Position getPosition();

    // Controle de posição
    void skipBytes(uint16_t bytes);
    void setMessageSize(uint16_t size);
    uint16_t getUnreadSize();
    
    // Criptografia
    bool decryptRsa(int size);
    void decryptXtea(const uint32_t* key);
};

// Mensagem de saída
class OutputMessage {
    -- Classe: OutputMessage
public:
    // Escrita de dados
    void addU8(uint8_t value);
    void addU16(uint16_t value);
    void addU32(uint32_t value);
    void addU64(uint64_t value);
    void addString(const std::string& value);
    void addPosition(const Position& pos);

    // Controle
    void writeChecksum();
    void writeMessageSize();
    
    // Criptografia
    void encryptRsa(int size);
    void encryptXtea(const uint32_t* key);
    
    // Estado
    uint16_t getMessageSize();
    void setMessageSize(uint16_t size);
    uint8_t* getDataBuffer();
};
```

## 🐍 API Lua

### Conexão e Protocolo

#### `Protocol:connect(host, port)`
Conecta ao servidor especificado.

```lua
local protocol = Protocol.create()

-- Conectar ao servidor
    --  Conectar ao servidor (traduzido)
protocol:connect("127.0.0.1", 7171)

-- Verificar estado
    --  Verificar estado (traduzido)
if protocol:isConnecting() then
    -- Verificação condicional
    print("Conectando...")
elseif protocol:isConnected() then
    print("Conectado!")
end
```

#### `Protocol:disconnect()`
Desconecta do servidor.

#### Nível Basic
```lua
protocol:disconnect()
```

#### Nível Intermediate
```lua
protocol:disconnect()
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```lua
protocol:disconnect()
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

#### Estado da Conexão
```lua
-- Verificar estado
    --  Verificar estado (traduzido)
local isConnected = protocol:isConnected()
local isConnecting = protocol:isConnecting()
local lastRead = protocol:getElapsedTicksSinceLastRead()

-- Callback de erro
    --  Callback de erro (traduzido)
protocol.onError = function(protocol, error)
    print("Erro de conexão:", error)
end

-- Callback de conexão
protocol.onConnect = function(protocol)
    print("Conectado com sucesso!")
end
```

### Envio e Recepção de Dados

#### Enviando Mensagens
```lua
-- Criar mensagem
    --  Criar mensagem (traduzido)
local msg = OutputMessage.create()
msg:addU8(0x14)  -- Opcode
msg:addString("Hello Server")
msg:addU32(12345)

-- Enviar
    --  Enviar (traduzido)
protocol:send(msg)
```

#### Recebendo Mensagens
```lua
protocol.onRecv = function(protocol, msg)
    local opcode = msg:getU8()
    
    if opcode == 0x14 then
    -- Verificação condicional
        local text = msg:getString()
        local number = msg:getU32()
        print("Recebido:", text, number)
    end
end
```

### Configuração de Criptografia

#### XTEA Encryption
```lua
-- Gerar chave aleatória
protocol:generateXteaKey()

-- Definir chave específica
protocol:setXteaKey(0x12345678, 0x9ABCDEF0, 0x11111111, 0x22222222)

-- Habilitar criptografia
    --  Habilitar criptografia (traduzido)
protocol:enableXteaEncryption()

-- Obter chave atual
    --  Obter chave atual (traduzido)
local key = protocol:getXteaKey()
print("Chave XTEA:", table.unpack(key))
```

#### Recursos Adicionais
```lua
-- Habilitar checksum
    --  Habilitar checksum (traduzido)
protocol:enableChecksum()

-- Habilitar pacotes sequenciados
    --  Habilitar pacotes sequenciados (traduzido)
protocol:enabledSequencedPackets()
```

## 🏗️ Arquitetura de Conexão

### Modelo Assíncrono
```
┌─────────────────┐    ┌─────────────────┐    ┌─────────────────┐
│   Application   │    │    Protocol     │    │   Connection    │
│                 │    │                 │    │                 │
│ send()          │───▶│ send()          │───▶│ write()         │
│ onRecv()        │◀───│ onRecv()        │◀───│ read()          │
│                 │    │                 │    │                 │
└─────────────────┘    └─────────────────┘    └─────────────────┘
                                                       │
                                                       ▼
                                              ┌─────────────────┐
                                              │   ASIO Socket   │
                                              │                 │
                                              │ async_connect() │
                                              │ async_read()    │
                                              │ async_write()   │
                                              └─────────────────┘
```

### Lifecycle da Conexão
#### Nível Basic
```lua
-- 1. Criação
local protocol = Protocol.create()

-- 2. Configuração
protocol:setXteaKey(...)
protocol:enableChecksum()

-- 3. Conexão
protocol:connect("server.com", 7171)

-- 4. Handshake
protocol.onConnect = function()
    local loginMsg = OutputMessage.create()
    loginMsg:addU8(GameClientOpcodes.GameServerLoginRequest)
    loginMsg:addString(username)
    loginMsg:addString(password)
    protocol:send(loginMsg)
end

-- 5. Comunicação
protocol.onRecv = function(protocol, msg)
    -- Processar mensagens recebidas
end

-- 6. Desconexão
protocol:disconnect()
```

#### Nível Intermediate
```lua
-- 1. Criação
local protocol = Protocol.create()

-- 2. Configuração
protocol:setXteaKey(...)
protocol:enableChecksum()

-- 3. Conexão
protocol:connect("server.com", 7171)

-- 4. Handshake
protocol.onConnect = function()
    local loginMsg = OutputMessage.create()
    loginMsg:addU8(GameClientOpcodes.GameServerLoginRequest)
    loginMsg:addString(username)
    loginMsg:addString(password)
    protocol:send(loginMsg)
end

-- 5. Comunicação
protocol.onRecv = function(protocol, msg)
    -- Processar mensagens recebidas
end

-- 6. Desconexão
protocol:disconnect()
-- Adicionar tratamento de erros
local success, result = pcall(function()
    -- Código original aqui
end)
if not success then
    print('Erro:', result)
end
```

#### Nível Advanced
```lua
-- 1. Criação
local protocol = Protocol.create()

-- 2. Configuração
protocol:setXteaKey(...)
protocol:enableChecksum()

-- 3. Conexão
protocol:connect("server.com", 7171)

-- 4. Handshake
protocol.onConnect = function()
    local loginMsg = OutputMessage.create()
    loginMsg:addU8(GameClientOpcodes.GameServerLoginRequest)
    loginMsg:addString(username)
    loginMsg:addString(password)
    protocol:send(loginMsg)
end

-- 5. Comunicação
protocol.onRecv = function(protocol, msg)
    -- Processar mensagens recebidas
end

-- 6. Desconexão
protocol:disconnect()
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

## 🔐 Sistema de Protocolo

### Opcodes do Jogo
```lua
-- Opcodes do cliente para servidor
    --  Opcodes do cliente para servidor (traduzido)
GameClientOpcodes = {
    GameServerLoginRequest = 1,
    GameServerLogout = 2,
    GameServerPing = 3,
    GameServerWalk = 4,
    GameServerTalk = 5,
    GameServerUseItem = 6,
    GameServerRotateItem = 7,
    GameServerMove = 8,
    -- ... mais opcodes
    --  ... mais opcodes (traduzido)
}

-- Opcodes do servidor para cliente
    --  Opcodes do servidor para cliente (traduzido)
GameServerOpcodes = {
    GameServerInitGame = 10,
    GameServerLoginError = 20,
    GameServerPing = 30,
    GameServerAddCreature = 23,
    GameServerFullMap = 100,
    GameServerTextMessage = 180,
    -- ... mais opcodes
    --  ... mais opcodes (traduzido)
}
```

### Handler de Protocolo Customizado
```lua
local MyProtocol = {}
MyProtocol.__index = MyProtocol

function MyProtocol.create()
    -- Função: MyProtocol
    local protocol = Protocol.create()
    setmetatable(protocol, MyProtocol)
    
    -- Configurar handlers
    --  Configurar handlers (traduzido)
    protocol.onConnect = MyProtocol.onConnect
    protocol.onRecv = MyProtocol.onRecv
    protocol.onError = MyProtocol.onError
    
    return protocol
end

function MyProtocol:onConnect()
    -- Função: MyProtocol
    print("Conectado ao servidor personalizado")
    self:sendHandshake()
end

function MyProtocol:onRecv(msg)
    -- Função: MyProtocol
    local opcode = msg:getU8()
    
    -- Dispatch para handlers específicos
    local handlers = {
        [0x01] = self.handleLogin,
        [0x02] = self.handleChat,
        [0x03] = self.handlePlayerUpdate,
    }
    
    local handler = handlers[opcode]
    if handler then
    -- Verificação condicional
        handler(self, msg)
    else
        print("Opcode desconhecido:", opcode)
    end
end

function MyProtocol:sendHandshake()
    -- Função: MyProtocol
    local msg = OutputMessage.create()
    msg:addU8(0x01)  -- Login opcode
    msg:addString("myusername")
    msg:addString("mypassword")
    msg:addU32(1000)  -- Client version
    self:send(msg)
end
```

## 🔒 Segurança e Criptografia

### Implementação XTEA
```lua
-- Sistema de criptografia XTEA para proteção de dados
local XTEAManager = {}

function XTEAManager.generateKey()
    -- Função: XTEAManager
    local key = {}
    for i = 1, 4 do
    -- Loop de repetição
        key[i] = math.random(0, 0xFFFFFFFF)
    end
    return key
end

function XTEAManager.rotateKey(key)
    -- Função: XTEAManager
    -- Rotação de chave para segurança adicional
    local newKey = {}
    for i = 1, 4 do
    -- Loop de repetição
        newKey[i] = ((key[i] << 1) | (key[i] >> 31)) & 0xFFFFFFFF
    end
    return newKey
end

-- Uso em protocolo
    --  Uso em protocolo (traduzido)
local protocol = Protocol.create()
local xteaKey = XTEAManager.generateKey()

protocol:setXteaKey(table.unpack(xteaKey))
protocol:enableXteaEncryption()
```

### Verificação de Integridade
```lua
-- Habilitar checksum para verificação de integridade
protocol:enableChecksum()

-- Implementação de validação adicional
local function validateMessage(msg)
    local expectedSize = msg:getU16()
    local actualSize = msg:getUnreadSize()
    
    if expectedSize ~= actualSize then
    -- Verificação condicional
        error("Tamanho de mensagem inválido")
    end
    
    -- Verificar magic number
    --  Verificar magic number (traduzido)
    local magic = msg:getU32()
    if magic ~= 0x12345678 then
    -- Verificação condicional
        error("Magic number inválido")
    end
    
    return true
end
```

## 💡 Exemplos Práticos

### 1. Cliente de Chat Simples
#### Inicialização e Configuração
```lua
local ChatClient = {}
ChatClient.__index = ChatClient

function ChatClient.create()
    local self = setmetatable({}, ChatClient)
    self.protocol = Protocol.create()
    self.isLoggedIn = false
    
    -- Configurar callbacks
    self.protocol.onConnect = function() self:onConnect() end
    self.protocol.onRecv = function(protocol, msg) self:onRecv(msg) end
    self.protocol.onError = function(protocol, error) self:onError(error) end
    
    return self
end

function ChatClient:connect(host, port, username, password)
    self.username = username
    self.password = password
    
    print("Conectando a", host .. ":" .. port)
    self.protocol:connect(host, port)
end
```

#### Funcionalidade 1
```lua

function ChatClient:onConnect()
    print("Conectado! Enviando login...")
    
    local msg = OutputMessage.create()
    msg:addU8(1)  -- Login opcode
    msg:addString(self.username)
    msg:addString(self.password)
    
    self.protocol:send(msg)
end

function ChatClient:onRecv(msg)
    local opcode = msg:getU8()
    
    if opcode == 1 then  -- Login response
        local success = msg:getU8()
        if success == 1 then
            self.isLoggedIn = true
            print("Login bem-sucedido!")
        else
            local errorMsg = msg:getString()
            print("Erro de login:", errorMsg)
        end
```

#### Funcionalidade 2
```lua
        
    elseif opcode == 2 then  -- Chat message
        local sender = msg:getString()
        local message = msg:getString()
        print("[" .. sender .. "]:", message)
        
    elseif opcode == 3 then  -- User list
        local count = msg:getU16()
        print("Usuários online (" .. count .. "):")
        for i = 1, count do
            local username = msg:getString()
            print("  -", username)
        end
    end
end

function ChatClient:sendMessage(message)
    if not self.isLoggedIn then
        print("Não está logado!")
        return
    end
```

#### Finalização
```lua
    
    local msg = OutputMessage.create()
    msg:addU8(2)  -- Chat opcode
    msg:addString(message)
    
    self.protocol:send(msg)
end

function ChatClient:onError(error)
    print("Erro de conexão:", error)
    self.isLoggedIn = false
end

-- Uso
local client = ChatClient.create()
client:connect("127.0.0.1", 8080, "usuario", "senha")

-- Simular envio de mensagem (após conectar)
scheduleEvent(function()
    client:sendMessage("Olá pessoal!")
end, 2000)
```

### 2. Sistema de Reconexão Automática
#### Inicialização e Configuração
```lua
local AutoReconnect = {}
AutoReconnect.__index = AutoReconnect

function AutoReconnect.create(protocol, config)
    local self = setmetatable({}, AutoReconnect)
    
    self.protocol = protocol
    self.config = config or {
        maxAttempts = 5,
        baseDelay = 1000,  -- 1 segundo
        maxDelay = 30000,  -- 30 segundos
        backoffMultiplier = 2
    }
    
    self.attempts = 0
    self.isReconnecting = false
    self.lastHost = nil
    self.lastPort = nil
    
    -- Interceptar métodos do protocolo
    self.originalConnect = protocol.connect
    self.originalOnError = protocol.onError
    
    protocol.connect = function(host, port)
        self:connect(host, port)
    end
```

#### Funcionalidade 1
```lua
    
    protocol.onError = function(protocol, error)
        self:onError(error)
    end
    
    return self
end

function AutoReconnect:connect(host, port)
    self.lastHost = host
    self.lastPort = port
    self.attempts = 0
    self.isReconnecting = false
    
    self.originalConnect(self.protocol, host, port)
end

function AutoReconnect:onError(error)
    -- Chamar callback original se existir
    if self.originalOnError then
        self.originalOnError(self.protocol, error)
    end
```

#### Funcionalidade 2
```lua
    
    -- Tentar reconectar se apropriado
    if self:shouldReconnect(error) then
        self:scheduleReconnect()
    end
end

function AutoReconnect:shouldReconnect(error)
    -- Não reconectar se já estamos tentando
    if self.isReconnecting then
        return false
    end
    
    -- Não reconectar se excedeu tentativas
    if self.attempts >= self.config.maxAttempts then
        print("Máximo de tentativas de reconexão excedido")
        return false
    end
    
    -- Não reconectar em certos tipos de erro
    local noReconnectErrors = {
        "Connection refused",
        "Invalid credentials",
        "Banned"
    }
```

#### Funcionalidade 3
```lua
    
    for _, errorType in ipairs(noReconnectErrors) do
        if string.find(error, errorType) then
            return false
        end
    end
    
    return true
end

function AutoReconnect:scheduleReconnect()
    if not self.lastHost or not self.lastPort then
        return
    end
    
    self.isReconnecting = true
    self.attempts = self.attempts + 1
    
    -- Calcular delay com backoff exponencial
    local delay = math.min(
        self.config.baseDelay * (self.config.backoffMultiplier ^ (self.attempts - 1)),
        self.config.maxDelay
    )
    
    print(string.format("Tentativa de reconexão %d/%d em %d segundos...", 
                       self.attempts, self.config.maxAttempts, delay / 1000))
    
    scheduleEvent(function()
        self:attemptReconnect()
    end, delay)
```

#### Finalização
```lua
end

function AutoReconnect:attemptReconnect()
    self.isReconnecting = false
    
    print("Tentando reconectar...")
    self.originalConnect(self.protocol, self.lastHost, self.lastPort)
end

-- Uso
local protocol = Protocol.create()
local autoReconnect = AutoReconnect.create(protocol, {
    maxAttempts = 10,
    baseDelay = 2000,
    maxDelay = 60000
})

protocol:connect("server.com", 7171)
```

### 3. Monitor de Latência e Performance
#### Inicialização e Configuração
```lua
local NetworkMonitor = {}
NetworkMonitor.__index = NetworkMonitor

function NetworkMonitor.create(protocol)
    local self = setmetatable({}, NetworkMonitor)
    
    self.protocol = protocol
    self.stats = {
        packetsReceived = 0,
        packetsSent = 0,
        bytesReceived = 0,
        bytesSent = 0,
        lastPingTime = 0,
        latency = 0,
        avgLatency = 0,
        minLatency = math.huge,
        maxLatency = 0,
        pingHistory = {}
    }
    
    -- Interceptar send/recv
    self.originalSend = protocol.send
    self.originalOnRecv = protocol.onRecv
    
    protocol.send = function(msg)
        self:onSend(msg)
        return self.originalSend(protocol, msg)
    end
```

#### Funcionalidade 1
```lua
    
    protocol.onRecv = function(protocol, msg)
        self:onRecv(msg)
        if self.originalOnRecv then
            return self.originalOnRecv(protocol, msg)
        end
    end
    
    -- Iniciar ping automático
    self:startPingMonitor()
    
    return self
end

function NetworkMonitor:onSend(msg)
    self.stats.packetsSent = self.stats.packetsSent + 1
    self.stats.bytesSent = self.stats.bytesSent + msg:getMessageSize()
    
    -- Detectar ping
    if msg:getMessageSize() > 0 then
        local opcode = msg:getDataBuffer()[0]
        if opcode == 0x1E then  -- Ping opcode
            self.stats.lastPingTime = g_clock.millis()
        end
```

#### Funcionalidade 2
```lua
    end
end

function NetworkMonitor:onRecv(msg)
    self.stats.packetsReceived = self.stats.packetsReceived + 1
    self.stats.bytesReceived = self.stats.bytesReceived + msg:getUnreadSize()
    
    -- Detectar pong
    local opcode = msg:getU8()
    if opcode == 0x1F then  -- Pong opcode
        self:updateLatency()
    end
    
    -- Resetar posição da mensagem
    msg:skipBytes(-1)
end

function NetworkMonitor:updateLatency()
    if self.stats.lastPingTime > 0 then
        local currentTime = g_clock.millis()
        local latency = currentTime - self.stats.lastPingTime
        
        self.stats.latency = latency
        self.stats.minLatency = math.min(self.stats.minLatency, latency)
        self.stats.maxLatency = math.max(self.stats.maxLatency, latency)
        
        -- Adicionar ao histórico
        table.insert(self.stats.pingHistory, latency)
        if #self.stats.pingHistory > 100 then
            table.remove(self.stats.pingHistory, 1)
        end
```

#### Funcionalidade 3
```lua
        
        -- Calcular média
        local sum = 0
        for _, ping in ipairs(self.stats.pingHistory) do
            sum = sum + ping
        end
        self.stats.avgLatency = sum / #self.stats.pingHistory
        
        self.stats.lastPingTime = 0
    end
end

function NetworkMonitor:startPingMonitor()
    local function sendPing()
        if self.protocol:isConnected() then
            local msg = OutputMessage.create()
            msg:addU8(0x1E)  -- Ping opcode
            self.protocol:send(msg)
        end
        
        scheduleEvent(sendPing, 5000)  -- Ping a cada 5 segundos
    end
```

#### Funcionalidade 4
```lua
    
    sendPing()
end

function NetworkMonitor:getStats()
    return {
        packetsReceived = self.stats.packetsReceived,
        packetsSent = self.stats.packetsSent,
        bytesReceived = self.stats.bytesReceived,
        bytesSent = self.stats.bytesSent,
        currentLatency = self.stats.latency,
        averageLatency = math.floor(self.stats.avgLatency),
        minLatency = self.stats.minLatency,
        maxLatency = self.stats.maxLatency,
        connectionQuality = self:getConnectionQuality()
    }
end

function NetworkMonitor:getConnectionQuality()
    if self.stats.avgLatency <= 50 then
        return "Excelente"
    elseif self.stats.avgLatency <= 100 then
        return "Boa"
    elseif self.stats.avgLatency <= 200 then
        return "Regular"
    else
        return "Ruim"
    end
```

#### Funcionalidade 5
```lua
end

-- UI para exibir estatísticas
function NetworkMonitor:createStatsWindow()
    local window = g_ui.createWidget('MainWindow')
    window:setTitle('Monitor de Rede')
    window:setSize({300, 200})
    
    local statsLabel = g_ui.createWidget('UILabel', window)
    statsLabel:setTextAlign(AlignLeft)
    
    local function updateDisplay()
        local stats = self:getStats()
        local text = string.format(
            "Pacotes: %d↑ %d↓\n" ..
            "Bytes: %s↑ %s↓\n" ..
            "Latência: %dms (avg: %dms)\n" ..
            "Range: %d-%dms\n" ..
            "Qualidade: %s",
            stats.packetsSent, stats.packetsReceived,
            formatBytes(stats.bytesSent), formatBytes(stats.bytesReceived),
            stats.currentLatency, stats.averageLatency,
            stats.minLatency, stats.maxLatency,
            stats.connectionQuality
        )
        
        statsLabel:setText(text)
        scheduleEvent(updateDisplay, 1000)
    end
```

#### Finalização
```lua
    
    updateDisplay()
    return window
end

-- Função auxiliar para formatar bytes
function formatBytes(bytes)
    if bytes < 1024 then
        return bytes .. "B"
    elseif bytes < 1048576 then
        return string.format("%.1fKB", bytes / 1024)
    else
        return string.format("%.1fMB", bytes / 1048576)
    end
end

-- Uso
local protocol = Protocol.create()
local monitor = NetworkMonitor.create(protocol)

-- Conectar e mostrar estatísticas
protocol:connect("server.com", 7171)
monitor:createStatsWindow()
```

## ✅ Melhores Práticas

### 1. Gerenciamento de Conexão
- **Timeouts apropriados**: Configure baseado na latência esperada
- **Reconexão inteligente**: Use backoff exponencial
- **Cleanup adequado**: Sempre feche conexões não utilizadas
- **Pool de conexões**: Para múltiplas conexões simultâneas

### 2. Protocolo e Mensagens
- **Validação rigorosa**: Sempre valide dados recebidos
- **Versionamento**: Mantenha compatibilidade entre versões
- **Compressão**: Use para dados grandes
- **Batching**: Agrupe múltiplas pequenas mensagens

### 3. Segurança
- **Criptografia sempre**: Use XTEA para dados sensíveis
- **Validação de integridade**: Implement checksums
- **Rate limiting**: Proteja contra spam/flood
- **Sanitização**: Limpe todas as entradas

### 4. Performance
- **Buffers adequados**: Configure tamanhos baseados no uso
- **Async operations**: Nunca bloqueie a thread principal
- **Monitoring**: Monitore latência e throughput
- **Graceful degradation**: Funcione mesmo com conectividade ruim

### 5. Debugging e Logging
```lua
-- Sistema de logging para rede
    --  Sistema de logging para rede (traduzido)
local NetworkLogger = {
    levels = { DEBUG = 1, INFO = 2, WARN = 3, ERROR = 4 },
    currentLevel = 2
}

function NetworkLogger.log(level, message, data)
    -- Função: NetworkLogger
    if NetworkLogger.levels[level] >= NetworkLogger.currentLevel then
    -- Verificação condicional
        local timestamp = os.date("%H:%M:%S")
        local logMsg = string.format("[%s] %s: %s", timestamp, level, message)
        
        if data then
    -- Verificação condicional
            logMsg = logMsg .. " | Data: " .. tostring(data)
        end
        
        print(logMsg)
        
        -- Salvar em arquivo se necessário
        if level == "ERROR" then
    -- Verificação condicional
            g_logger.error(logMsg)
        end
    end
end

-- Uso
    --  Uso (traduzido)
NetworkLogger.log("INFO", "Conectando ao servidor", "127.0.0.1:7171")
NetworkLogger.log("DEBUG", "Enviando mensagem", "Opcode: 0x14")
NetworkLogger.log("ERROR", "Falha na conexão", error)
```

### 6. Tratamento de Erro Robusto
```lua
function createRobustProtocol()
    -- Função: createRobustProtocol
    local protocol = Protocol.create()
    
    protocol.onError = function(protocol, error)
        -- Categorizar erro
    --  Categorizar erro (traduzido)
        local errorType = categorizeError(error)
        
        -- Ações baseadas no tipo
        if errorType == "NETWORK" then
    -- Verificação condicional
            -- Problema de rede - tentar reconectar
    --  Problema de rede - tentar reconectar (traduzido)
            scheduleReconnect()
        elseif errorType == "PROTOCOL" then
            -- Erro de protocolo - log e continue
    --  Erro de protocolo - log e continue (traduzido)
            NetworkLogger.log("ERROR", "Protocol error", error)
        elseif errorType == "SECURITY" then
            -- Problema de segurança - desconectar imediatamente
            protocol:disconnect()
            showSecurityAlert(error)
        end
    end
    
    return protocol
end

function categorizeError(error)
    -- Função: categorizeError
    if string.find(error, "Connection") then
    -- Verificação condicional
        return "NETWORK"
    elseif string.find(error, "Invalid") or string.find(error, "Malformed") then
        return "PROTOCOL"
    elseif string.find(error, "Unauthorized") or string.find(error, "Forbidden") then
        return "SECURITY"
    else
        return "UNKNOWN"
    end
end
```

---

*Documentação gerada para OTClient - Redemption | Sistema de Rede*

---

<div class="success"> Navegação
> - [Getting_Started_Guide](Getting_Started_Guide.md) - Comece aqui
> - [Module_System_Guide](Module_System_Guide.md) - Desenvolvimento de módulos
> - [UI_System_Guide](UI_System_Guide.md) - Interface do usuário
> - [Lua_API_Reference](Lua_API_Reference.md) - Referência completa da API

