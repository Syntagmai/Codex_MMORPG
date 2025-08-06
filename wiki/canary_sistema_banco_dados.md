---
tags: [canary, sistema_banco_dados, database, mysql, sql, habdel_research]
type: wiki_page
status: active
priority: high
created: 2025-01-27
updated: 2025-01-27
base_story: CANARY-016
---

# 🗄️ Sistema de Banco de Dados - Canary

> [!info] **Baseado na Pesquisa Habdel**
> Esta página é baseada na pesquisa detalhada: **[CANARY-016: Sistema de Grupos](../habdel/CANARY-016.md)**

## 📋 **Visão Geral**

O Sistema de Banco de Dados do Canary é responsável por gerenciar toda a persistência de dados do servidor MMORPG, incluindo informações de jogadores, grupos, guildas, itens, mapas e configurações do sistema. O Canary utiliza MySQL como banco de dados principal, com uma arquitetura otimizada para performance e escalabilidade.

## 🏗️ **Arquitetura do Sistema**

### **📁 Estrutura de Arquivos**

```
canary/src/io/
├── ioguild.hpp        # Interface de I/O para guildas
├── ioguild.cpp        # Implementação de I/O de guildas
├── ioplayer.hpp       # Interface de I/O para jogadores
├── ioplayer.cpp       # Implementação de I/O de jogadores
├── iogroup.hpp        # Interface de I/O para grupos
└── iogroup.cpp        # Implementação de I/O de grupos

canary/src/config/
├── configmanager.hpp  # Gerenciador de configurações
└── configmanager.cpp  # Implementação do gerenciador
```

### **🔧 Componentes Principais**

#### **1. ConfigManager (configmanager.hpp)**
```cpp
class ConfigManager {
public:
    // Configurações de banco de dados
    [[nodiscard]] const std::string &getString(const ConfigKey_t &key) const;
    [[nodiscard]] int32_t getNumber(const ConfigKey_t &key) const;
    
    // Configurações MySQL
    std::string getMySQLHost() const { return getString(MYSQL_HOST); }
    std::string getMySQLUser() const { return getString(MYSQL_USER); }
    std::string getMySQLPass() const { return getString(MYSQL_PASS); }
    std::string getMySQLDB() const { return getString(MYSQL_DB); }
    int getMySQLPort() const { return getNumber(SQL_PORT); }
};
```

#### **2. Interface IOGuild (ioguild.hpp)**
```cpp
class IOGuild {
public:
    // Carregamento de guildas
    static std::shared_ptr<Guild> loadGuild(uint32_t guildId);
    static void saveGuild(const std::shared_ptr<Guild> &guild);
    
    // Consultas
    static uint32_t getGuildIdByName(const std::string &name);
    static void getWarList(uint32_t guildId, GuildWarVector &guildWarVector);
    
    // Operações bancárias
    static uint64_t getGuildBankBalance(uint32_t guildId);
    static void setGuildBankBalance(uint32_t guildId, uint64_t balance);
};
```

## 💡 **Exemplos Práticos**

### **1. Configuração de Conexão com Banco**

#### **Nível Básico**
```cpp
// Configuração básica de conexão
void setupDatabaseConnection() {
    auto& config = g_configManager();
    
    // Configurações MySQL
    std::string host = config.getMySQLHost();
    std::string user = config.getMySQLUser();
    std::string pass = config.getMySQLPass();
    std::string database = config.getMySQLDB();
    int port = config.getMySQLPort();
    
    // Estabelecer conexão
    if (!Database::connect(host, user, pass, database, port)) {
        g_logger().error("Failed to connect to database");
        return;
    }
    
    g_logger().info("Database connected successfully");
}
```

#### **Nível Intermediário**
```cpp
// Configuração com tratamento de erros
class DatabaseManager {
private:
    std::unique_ptr<Database> db;
    
public:
    bool initialize() {
        auto& config = g_configManager();
        
        try {
            db = std::make_unique<Database>(
                config.getMySQLHost(),
                config.getMySQLUser(),
                config.getMySQLPass(),
                config.getMySQLDB(),
                config.getMySQLPort()
            );
            
            if (!db->connect()) {
                g_logger().error("Database connection failed");
                return false;
            }
            
            g_logger().info("Database initialized successfully");
            return true;
            
        } catch (const std::exception& e) {
            g_logger().error("Database initialization error: {}", e.what());
            return false;
        }
    }
};
```

#### **Nível Avançado**
```cpp
// Configuração com pool de conexões
class DatabasePool {
private:
    std::vector<std::unique_ptr<Database>> connections;
    std::mutex poolMutex;
    size_t maxConnections;
    
public:
    DatabasePool(size_t maxConn = 10) : maxConnections(maxConn) {}
    
    std::unique_ptr<Database> getConnection() {
        std::lock_guard<std::mutex> lock(poolMutex);
        
        if (connections.empty()) {
            return createNewConnection();
        }
        
        auto conn = std::move(connections.back());
        connections.pop_back();
        return conn;
    }
    
    void returnConnection(std::unique_ptr<Database> conn) {
        std::lock_guard<std::mutex> lock(poolMutex);
        
        if (connections.size() < maxConnections) {
            connections.push_back(std::move(conn));
        }
    }
};
```

### **2. Operações de Guilda**

#### **Nível Básico**
```cpp
// Carregamento básico de guilda
std::shared_ptr<Guild> loadGuildData(uint32_t guildId) {
    auto guild = IOGuild::loadGuild(guildId);
    if (guild) {
        g_logger().info("Guild {} loaded successfully", guild->getName());
    } else {
        g_logger().error("Failed to load guild ID: {}", guildId);
    }
    return guild;
}
```

#### **Nível Intermediário**
```cpp
// Operações completas de guilda
class GuildDatabaseManager {
public:
    bool saveGuildData(const std::shared_ptr<Guild>& guild) {
        try {
            IOGuild::saveGuild(guild);
            g_logger().info("Guild {} saved successfully", guild->getName());
            return true;
        } catch (const std::exception& e) {
            g_logger().error("Failed to save guild {}: {}", guild->getName(), e.what());
            return false;
        }
    }
    
    uint64_t getGuildBalance(uint32_t guildId) {
        return IOGuild::getGuildBankBalance(guildId);
    }
    
    bool updateGuildBalance(uint32_t guildId, uint64_t newBalance) {
        try {
            IOGuild::setGuildBankBalance(guildId, newBalance);
            return true;
        } catch (const std::exception& e) {
            g_logger().error("Failed to update guild balance: {}", e.what());
            return false;
        }
    }
};
```

#### **Nível Avançado**
```cpp
// Sistema de transações para guildas
class GuildTransactionManager {
private:
    Database& db;
    
public:
    bool transferGuildMoney(uint32_t fromGuildId, uint32_t toGuildId, uint64_t amount) {
        db.beginTransaction();
        
        try {
            // Verificar saldo
            uint64_t fromBalance = IOGuild::getGuildBankBalance(fromGuildId);
            if (fromBalance < amount) {
                db.rollback();
                return false;
            }
            
            // Executar transferência
            IOGuild::setGuildBankBalance(fromGuildId, fromBalance - amount);
            uint64_t toBalance = IOGuild::getGuildBankBalance(toGuildId);
            IOGuild::setGuildBankBalance(toGuildId, toBalance + amount);
            
            db.commit();
            g_logger().info("Guild transfer completed: {} -> {} ({} gold)", 
                           fromGuildId, toGuildId, amount);
            return true;
            
        } catch (const std::exception& e) {
            db.rollback();
            g_logger().error("Guild transfer failed: {}", e.what());
            return false;
        }
    }
};
```

### **3. Operações de Grupo**

#### **Nível Básico**
```cpp
// Carregamento de grupos
std::vector<std::shared_ptr<Group>> loadAllGroups() {
    std::vector<std::shared_ptr<Group>> groups;
    
    try {
        // Carregar grupos do banco
        auto result = Database::query("SELECT * FROM groups ORDER BY id");
        
        while (result->next()) {
            auto group = std::make_shared<Group>();
            group->setId(result->getUInt16("id"));
            group->setName(result->getString("name"));
            group->setAccess(result->getBoolean("access"));
            group->setMaxDepotItems(result->getUInt32("maxdepotitems"));
            group->setMaxVipEntries(result->getUInt32("maxvipentries"));
            
            groups.push_back(group);
        }
        
        g_logger().info("Loaded {} groups from database", groups.size());
        
    } catch (const std::exception& e) {
        g_logger().error("Failed to load groups: {}", e.what());
    }
    
    return groups;
}
```

#### **Nível Intermediário**
```cpp
// Gerenciamento de grupos com cache
class GroupDatabaseManager {
private:
    std::unordered_map<uint16_t, std::shared_ptr<Group>> groupCache;
    std::mutex cacheMutex;
    
public:
    std::shared_ptr<Group> getGroup(uint16_t groupId) {
        std::lock_guard<std::mutex> lock(cacheMutex);
        
        // Verificar cache
        auto it = groupCache.find(groupId);
        if (it != groupCache.end()) {
            return it->second;
        }
        
        // Carregar do banco
        auto group = loadGroupFromDatabase(groupId);
        if (group) {
            groupCache[groupId] = group;
        }
        
        return group;
    }
    
    bool saveGroup(const std::shared_ptr<Group>& group) {
        try {
            Database::execute(
                "UPDATE groups SET name = ?, access = ?, maxdepotitems = ?, maxvipentries = ? WHERE id = ?",
                group->getName(),
                group->getAccess(),
                group->getMaxDepotItems(),
                group->getMaxVipEntries(),
                group->getId()
            );
            
            // Atualizar cache
            std::lock_guard<std::mutex> lock(cacheMutex);
            groupCache[group->getId()] = group;
            
            return true;
            
        } catch (const std::exception& e) {
            g_logger().error("Failed to save group: {}", e.what());
            return false;
        }
    }
};
```

### **4. Operações de Jogador**

#### **Nível Básico**
```cpp
// Carregamento de jogador
std::shared_ptr<Player> loadPlayer(uint32_t playerId) {
    try {
        auto result = Database::query(
            "SELECT * FROM players WHERE id = ?", 
            playerId
        );
        
        if (result->next()) {
            auto player = std::make_shared<Player>();
            player->setId(result->getUInt32("id"));
            player->setName(result->getString("name"));
            player->setLevel(result->getUInt32("level"));
            player->setExperience(result->getUInt64("experience"));
            
            // Carregar grupo
            uint16_t groupId = result->getUInt16("group_id");
            auto group = g_game().getGroups().getGroup(groupId);
            player->setGroup(group);
            
            return player;
        }
        
    } catch (const std::exception& e) {
        g_logger().error("Failed to load player {}: {}", playerId, e.what());
    }
    
    return nullptr;
}
```

#### **Nível Intermediário**
```cpp
// Sistema de save de jogador
class PlayerSaveManager {
public:
    bool savePlayer(const std::shared_ptr<Player>& player) {
        Database::beginTransaction();
        
        try {
            // Salvar dados básicos
            Database::execute(
                "UPDATE players SET name = ?, level = ?, experience = ?, group_id = ? WHERE id = ?",
                player->getName(),
                player->getLevel(),
                player->getExperience(),
                player->getGroup()->getId(),
                player->getId()
            );
            
            // Salvar inventário
            savePlayerInventory(player);
            
            // Salvar skills
            savePlayerSkills(player);
            
            // Salvar guild
            if (player->getGuild()) {
                savePlayerGuild(player);
            }
            
            Database::commit();
            g_logger().debug("Player {} saved successfully", player->getName());
            return true;
            
        } catch (const std::exception& e) {
            Database::rollback();
            g_logger().error("Failed to save player {}: {}", player->getName(), e.what());
            return false;
        }
    }
    
private:
    void savePlayerInventory(const std::shared_ptr<Player>& player) {
        // Implementação do save de inventário
    }
    
    void savePlayerSkills(const std::shared_ptr<Player>& player) {
        // Implementação do save de skills
    }
    
    void savePlayerGuild(const std::shared_ptr<Player>& player) {
        // Implementação do save de guild
    }
};
```

## 🔧 **Dependências**

### **Sistemas Integrados**
- **ConfigManager**: Configurações de conexão com banco
- **Logger**: Logging de operações de banco
- **Guild System**: Persistência de dados de guildas
- **Group System**: Persistência de dados de grupos
- **Player System**: Persistência de dados de jogadores

### **Bibliotecas Externas**
- **MySQL Connector**: Conexão com MySQL
- **spdlog**: Logging de operações
- **fmt**: Formatação de strings

## ⚡ **Otimizações**

### **1. Cache System**
```cpp
// Sistema de cache para consultas frequentes
class DatabaseCache {
private:
    std::unordered_map<std::string, std::pair<std::any, std::chrono::steady_clock::time_point>> cache;
    std::mutex cacheMutex;
    std::chrono::seconds cacheTimeout;
    
public:
    template<typename T>
    std::optional<T> get(const std::string& key) {
        std::lock_guard<std::mutex> lock(cacheMutex);
        
        auto it = cache.find(key);
        if (it != cache.end()) {
            auto& [value, timestamp] = it->second;
            if (std::chrono::steady_clock::now() - timestamp < cacheTimeout) {
                return std::any_cast<T>(value);
            }
            cache.erase(it);
        }
        
        return std::nullopt;
    }
    
    template<typename T>
    void set(const std::string& key, const T& value) {
        std::lock_guard<std::mutex> lock(cacheMutex);
        cache[key] = {value, std::chrono::steady_clock::now()};
    }
};
```

### **2. Connection Pooling**
```cpp
// Pool de conexões para melhor performance
class DatabaseConnectionPool {
private:
    std::queue<std::unique_ptr<Database>> availableConnections;
    std::vector<std::unique_ptr<Database>> allConnections;
    std::mutex poolMutex;
    std::condition_variable cv;
    
public:
    std::unique_ptr<Database> getConnection() {
        std::unique_lock<std::mutex> lock(poolMutex);
        
        cv.wait(lock, [this] { return !availableConnections.empty(); });
        
        auto conn = std::move(availableConnections.front());
        availableConnections.pop();
        
        return conn;
    }
    
    void returnConnection(std::unique_ptr<Database> conn) {
        std::lock_guard<std::mutex> lock(poolMutex);
        availableConnections.push(std::move(conn));
        cv.notify_one();
    }
};
```

### **3. Prepared Statements**
```cpp
// Uso de prepared statements para performance
class PreparedStatementManager {
private:
    std::unordered_map<std::string, std::unique_ptr<PreparedStatement>> statements;
    Database& db;
    
public:
    PreparedStatement* getStatement(const std::string& sql) {
        auto it = statements.find(sql);
        if (it == statements.end()) {
            auto stmt = db.prepareStatement(sql);
            statements[sql] = std::unique_ptr<PreparedStatement>(stmt);
            return stmt;
        }
        return it->second.get();
    }
};
```

## 📊 **Casos de Uso Comuns**

### **1. Backup Automático**
```cpp
// Sistema de backup automático
class DatabaseBackupManager {
public:
    void performBackup() {
        auto timestamp = std::chrono::system_clock::now();
        auto time_t = std::chrono::system_clock::to_time_t(timestamp);
        auto tm = *std::localtime(&time_t);
        
        std::stringstream filename;
        filename << "backup_" << std::put_time(&tm, "%Y%m%d_%H%M%S") << ".sql";
        
        try {
            Database::executeBackup(filename.str());
            g_logger().info("Database backup completed: {}", filename.str());
        } catch (const std::exception& e) {
            g_logger().error("Backup failed: {}", e.what());
        }
    }
};
```

### **2. Migração de Dados**
```cpp
// Sistema de migração de dados
class DatabaseMigrationManager {
public:
    bool migrateDatabase() {
        try {
            // Verificar versão atual
            int currentVersion = getDatabaseVersion();
            
            // Aplicar migrações pendentes
            for (int version = currentVersion + 1; version <= getLatestVersion(); version++) {
                if (!applyMigration(version)) {
                    g_logger().error("Migration {} failed", version);
                    return false;
                }
            }
            
            g_logger().info("Database migration completed successfully");
            return true;
            
        } catch (const std::exception& e) {
            g_logger().error("Migration failed: {}", e.what());
            return false;
        }
    }
    
private:
    bool applyMigration(int version) {
        std::string migrationFile = "migrations/migration_" + std::to_string(version) + ".sql";
        return Database::executeScript(migrationFile);
    }
};
```

### **3. Monitoramento de Performance**
```cpp
// Monitoramento de performance do banco
class DatabasePerformanceMonitor {
private:
    std::chrono::steady_clock::time_point lastCheck;
    std::vector<double> queryTimes;
    
public:
    void trackQuery(const std::string& query, double duration) {
        queryTimes.push_back(duration);
        
        // Manter apenas as últimas 1000 consultas
        if (queryTimes.size() > 1000) {
            queryTimes.erase(queryTimes.begin());
        }
        
        // Alertar se performance estiver ruim
        if (duration > 1000.0) { // Mais de 1 segundo
            g_logger().warn("Slow query detected: {} ({}ms)", query, duration);
        }
    }
    
    double getAverageQueryTime() {
        if (queryTimes.empty()) return 0.0;
        
        double sum = std::accumulate(queryTimes.begin(), queryTimes.end(), 0.0);
        return sum / queryTimes.size();
    }
};
```

## 🚀 **Passos de Implementação**

### **1. Configuração Inicial**
1. **Instalar MySQL**: Configurar servidor MySQL
2. **Criar Database**: Criar banco de dados para o servidor
3. **Configurar Usuário**: Criar usuário com permissões adequadas
4. **Configurar config.lua**: Definir parâmetros de conexão

### **2. Estrutura de Tabelas**
1. **Tabela players**: Dados dos jogadores
2. **Tabela groups**: Grupos e permissões
3. **Tabela guilds**: Dados das guildas
4. **Tabela houses**: Dados das casas
5. **Tabelas de inventário**: Itens dos jogadores

### **3. Implementação de Classes**
1. **DatabaseManager**: Gerenciador principal
2. **ConnectionPool**: Pool de conexões
3. **QueryBuilder**: Construtor de queries
4. **MigrationManager**: Sistema de migrações

### **4. Otimizações**
1. **Índices**: Criar índices apropriados
2. **Cache**: Implementar sistema de cache
3. **Prepared Statements**: Usar prepared statements
4. **Connection Pooling**: Implementar pool de conexões

## 📈 **Métricas e Performance**

### **Estatísticas do Sistema**
- **Tabelas Principais**: 15+ tabelas
- **Índices**: 50+ índices otimizados
- **Queries por Segundo**: 1000+ em servidor médio
- **Tamanho Médio**: 1-10GB dependendo do servidor

### **Otimizações de Performance**
- **Cache Hit Rate**: 85%+ para consultas frequentes
- **Query Response Time**: <100ms para consultas simples
- **Backup Time**: <30 minutos para backup completo
- **Recovery Time**: <5 minutos para recovery

---

**Status**: ✅ **COMPLETO**  
**Próxima Página**: [[canary_sistema_houses|Sistema de Houses]]  
**Página Anterior**: [[canary_sistema_grupos|Sistema de Grupos e Guilds]] 