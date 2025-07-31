---
tags: [integration, api_templates, canary, otclient, unified_apis]
type: documentation
status: active
priority: high
created: 2025-01-27
---

# 🔗 Templates de APIs Unificadas - Integração OTClient-Canary

## 🚀 **Visão Geral**

Este documento fornece **templates de APIs unificadas** para integração entre OTClient e Canary, definindo estruturas padrão, interfaces e implementações de referência.

---

## ⚠️ **LIMITAÇÕES ATUAIS**

> [!warning] **CONTEXTO IMPORTANTE**
> Este repositório contém apenas o código-fonte do OTClient. O código-fonte do Canary **NÃO está disponível** para análise. Esta documentação foca em **preparação** para integração futura.

---

## 📋 **1. Template de API Base**

### **🎯 Estrutura Padrão de API**
```lua
-- Template base para todas as APIs unificadas
local UnifiedAPITemplate = {
    -- Metadados da API
    metadata = {
        name = "api_name",
        version = "1.0.0",
        description = "API description",
        author = "OTClient-Canary Integration",
        created = "2025-01-27"
    },
    
    -- Configuração da API
    configuration = {
        timeout = 5000,        -- ms
        retry_count = 3,
        buffer_size = 1024,    -- bytes
        compression = true,
        encryption = true
    },
    
    -- Endpoints da API
    endpoints = {
        -- Endpoints obrigatórios
        required = {
            "initialize",
            "connect",
            "authenticate",
            "disconnect",
            "health_check"
        },
        
        -- Endpoints específicos
        specific = {
            -- Implementar conforme necessidade
        }
    },
    
    -- Tratamento de erros
    error_handling = {
        error_codes = {
            SUCCESS = 0,
            INVALID_REQUEST = 400,
            UNAUTHORIZED = 401,
            NOT_FOUND = 404,
            INTERNAL_ERROR = 500,
            TIMEOUT = 408
        },
        
        error_messages = {
            [0] = "Success",
            [400] = "Invalid request",
            [401] = "Unauthorized",
            [404] = "Not found",
            [500] = "Internal server error",
            [408] = "Request timeout"
        }
    }
}
```

---

## 🎮 **2. Game API Templates**

### **🌍 World API Template**
```lua
-- Template para API de mundo
local WorldAPITemplate = {
    metadata = {
        name = "world_api",
        version = "1.0.0",
        description = "World management API for OTClient-Canary integration"
    },
    
    endpoints = {
        -- Gerenciamento de mapa
        map = {
            get_map = {
                method = "GET",
                path = "/api/world/map/:x/:y/:z",
                description = "Get map tile at coordinates",
                parameters = {
                    x = { type = "integer", required = true },
                    y = { type = "integer", required = true },
                    z = { type = "integer", required = true }
                },
                response = {
                    success = {
                        tile_id = "integer",
                        items = "array",
                        creatures = "array"
                    }
                }
            },
            
            update_map = {
                method = "PUT",
                path = "/api/world/map/:x/:y/:z",
                description = "Update map tile",
                parameters = {
                    x = { type = "integer", required = true },
                    y = { type = "integer", required = true },
                    z = { type = "integer", required = true },
                    tile_data = { type = "object", required = true }
                }
            }
        },
        
        -- Gerenciamento de criaturas
        creatures = {
            get_creature = {
                method = "GET",
                path = "/api/world/creatures/:id",
                description = "Get creature information"
            },
            
            update_creature = {
                method = "PUT",
                path = "/api/world/creatures/:id",
                description = "Update creature state"
            },
            
            move_creature = {
                method = "POST",
                path = "/api/world/creatures/:id/move",
                description = "Move creature to new position"
            }
        },
        
        -- Gerenciamento de itens
        items = {
            get_item = {
                method = "GET",
                path = "/api/world/items/:id",
                description = "Get item information"
            },
            
            update_item = {
                method = "PUT",
                path = "/api/world/items/:id",
                description = "Update item state"
            },
            
            create_item = {
                method = "POST",
                path = "/api/world/items",
                description = "Create new item"
            }
        }
    }
}
```

### **⚔️ Combat API Template**
```lua
-- Template para API de combate
local CombatAPITemplate = {
    metadata = {
        name = "combat_api",
        version = "1.0.0",
        description = "Combat system API for OTClient-Canary integration"
    },
    
    endpoints = {
        -- Ações de combate
        actions = {
            attack = {
                method = "POST",
                path = "/api/combat/attack",
                description = "Perform attack action",
                parameters = {
                    attacker_id = { type = "integer", required = true },
                    target_id = { type = "integer", required = true },
                    weapon_id = { type = "integer", required = false }
                },
                response = {
                    success = {
                        damage = "integer",
                        hit = "boolean",
                        critical = "boolean"
                    }
                }
            },
            
            cast_spell = {
                method = "POST",
                path = "/api/combat/spell",
                description = "Cast spell",
                parameters = {
                    caster_id = { type = "integer", required = true },
                    spell_id = { type = "integer", required = true },
                    target_id = { type = "integer", required = false }
                }
            }
        },
        
        -- Status de combate
        status = {
            get_health = {
                method = "GET",
                path = "/api/combat/health/:id",
                description = "Get creature health"
            },
            
            get_mana = {
                method = "GET",
                path = "/api/combat/mana/:id",
                description = "Get creature mana"
            },
            
            get_effects = {
                method = "GET",
                path = "/api/combat/effects/:id",
                description = "Get creature effects"
            }
        }
    }
}
```

### **💰 Trade API Template**
```lua
-- Template para API de trade
local TradeAPITemplate = {
    metadata = {
        name = "trade_api",
        version = "1.0.0",
        description = "Trade system API for OTClient-Canary integration"
    },
    
    endpoints = {
        -- Gerenciamento de ofertas
        offers = {
            create_offer = {
                method = "POST",
                path = "/api/trade/offers",
                description = "Create trade offer",
                parameters = {
                    seller_id = { type = "integer", required = true },
                    item_id = { type = "integer", required = true },
                    quantity = { type = "integer", required = true },
                    price = { type = "integer", required = true }
                }
            },
            
            get_offers = {
                method = "GET",
                path = "/api/trade/offers",
                description = "Get available trade offers",
                parameters = {
                    item_id = { type = "integer", required = false },
                    min_price = { type = "integer", required = false },
                    max_price = { type = "integer", required = false }
                }
            },
            
            accept_offer = {
                method = "POST",
                path = "/api/trade/offers/:id/accept",
                description = "Accept trade offer",
                parameters = {
                    buyer_id = { type = "integer", required = true }
                }
            }
        },
        
        -- Transações
        transactions = {
            get_transaction = {
                method = "GET",
                path = "/api/trade/transactions/:id",
                description = "Get transaction details"
            },
            
            get_transaction_history = {
                method = "GET",
                path = "/api/trade/transactions",
                description = "Get transaction history",
                parameters = {
                    player_id = { type = "integer", required = false },
                    start_date = { type = "string", required = false },
                    end_date = { type = "string", required = false }
                }
            }
        }
    }
}
```

---

## 🔧 **3. System API Templates**

### **⚙️ Configuration API Template**
```lua
-- Template para API de configuração
local ConfigAPITemplate = {
    metadata = {
        name = "config_api",
        version = "1.0.0",
        description = "Configuration management API for OTClient-Canary integration"
    },
    
    endpoints = {
        -- Gerenciamento de configurações
        configs = {
            get_config = {
                method = "GET",
                path = "/api/config/:key",
                description = "Get configuration value",
                parameters = {
                    key = { type = "string", required = true }
                }
            },
            
            set_config = {
                method = "PUT",
                path = "/api/config/:key",
                description = "Set configuration value",
                parameters = {
                    key = { type = "string", required = true },
                    value = { type = "any", required = true }
                }
            },
            
            get_all_configs = {
                method = "GET",
                path = "/api/config",
                description = "Get all configurations"
            },
            
            reset_config = {
                method = "DELETE",
                path = "/api/config/:key",
                description = "Reset configuration to default"
            }
        },
        
        -- Sincronização de configurações
        sync = {
            sync_config = {
                method = "POST",
                path = "/api/config/sync",
                description = "Synchronize configurations between client and server"
            },
            
            export_config = {
                method = "GET",
                path = "/api/config/export",
                description = "Export configurations to file"
            },
            
            import_config = {
                method = "POST",
                path = "/api/config/import",
                description = "Import configurations from file"
            }
        }
    }
}
```

### **📦 Module API Template**
```lua
-- Template para API de módulos
local ModuleAPITemplate = {
    metadata = {
        name = "module_api",
        version = "1.0.0",
        description = "Module management API for OTClient-Canary integration"
    },
    
    endpoints = {
        -- Gerenciamento de módulos
        modules = {
            load_module = {
                method = "POST",
                path = "/api/modules/load",
                description = "Load module",
                parameters = {
                    module_name = { type = "string", required = true },
                    module_path = { type = "string", required = true }
                }
            },
            
            unload_module = {
                method = "POST",
                path = "/api/modules/unload",
                description = "Unload module",
                parameters = {
                    module_name = { type = "string", required = true }
                }
            },
            
            reload_module = {
                method = "POST",
                path = "/api/modules/reload",
                description = "Reload module",
                parameters = {
                    module_name = { type = "string", required = true }
                }
            },
            
            get_module_info = {
                method = "GET",
                path = "/api/modules/:name",
                description = "Get module information"
            },
            
            list_modules = {
                method = "GET",
                path = "/api/modules",
                description = "List all loaded modules"
            }
        },
        
        -- Comunicação entre módulos
        communication = {
            send_message = {
                method = "POST",
                path = "/api/modules/message",
                description = "Send message between modules",
                parameters = {
                    from_module = { type = "string", required = true },
                    to_module = { type = "string", required = true },
                    message = { type = "object", required = true }
                }
            },
            
            get_messages = {
                method = "GET",
                path = "/api/modules/messages",
                description = "Get messages for module",
                parameters = {
                    module_name = { type = "string", required = true }
                }
            }
        }
    }
}
```

### **🐛 Debug API Template**
```lua
-- Template para API de debug
local DebugAPITemplate = {
    metadata = {
        name = "debug_api",
        version = "1.0.0",
        description = "Debug and logging API for OTClient-Canary integration"
    },
    
    endpoints = {
        -- Gerenciamento de logs
        logs = {
            add_log = {
                method = "POST",
                path = "/api/debug/logs",
                description = "Add log entry",
                parameters = {
                    level = { type = "string", required = true, enum = ["debug", "info", "warning", "error"] },
                    message = { type = "string", required = true },
                    module = { type = "string", required = false },
                    timestamp = { type = "string", required = false }
                }
            },
            
            get_logs = {
                method = "GET",
                path = "/api/debug/logs",
                description = "Get log entries",
                parameters = {
                    level = { type = "string", required = false },
                    module = { type = "string", required = false },
                    start_time = { type = "string", required = false },
                    end_time = { type = "string", required = false },
                    limit = { type = "integer", required = false }
                }
            },
            
            clear_logs = {
                method = "DELETE",
                path = "/api/debug/logs",
                description = "Clear all logs"
            }
        },
        
        -- Monitoramento de performance
        performance = {
            get_metrics = {
                method = "GET",
                path = "/api/debug/performance",
                description = "Get performance metrics"
            },
            
            start_profiling = {
                method = "POST",
                path = "/api/debug/performance/start",
                description = "Start performance profiling"
            },
            
            stop_profiling = {
                method = "POST",
                path = "/api/debug/performance/stop",
                description = "Stop performance profiling"
            },
            
            get_profile = {
                method = "GET",
                path = "/api/debug/performance/profile",
                description = "Get profiling results"
            }
        },
        
        -- Relatórios de erro
        errors = {
            report_error = {
                method = "POST",
                path = "/api/debug/errors",
                description = "Report error",
                parameters = {
                    error_type = { type = "string", required = true },
                    error_message = { type = "string", required = true },
                    stack_trace = { type = "string", required = false },
                    context = { type = "object", required = false }
                }
            },
            
            get_errors = {
                method = "GET",
                path = "/api/debug/errors",
                description = "Get error reports",
                parameters = {
                    error_type = { type = "string", required = false },
                    start_time = { type = "string", required = false },
                    end_time = { type = "string", required = false }
                }
            }
        }
    }
}
```

---

## 🔄 **4. Communication API Templates**

### **📡 REST API Template**
```lua
-- Template para APIs REST
local RESTAPITemplate = {
    metadata = {
        name = "rest_api",
        version = "1.0.0",
        description = "REST API template for OTClient-Canary integration"
    },
    
    -- Headers padrão
    headers = {
        "Content-Type: application/json",
        "Accept: application/json",
        "Authorization: Bearer {token}",
        "X-Client-Version: {version}",
        "X-Request-ID: {request_id}"
    },
    
    -- Padrões de resposta
    response_patterns = {
        success = {
            status = 200,
            body = {
                success = true,
                data = "response_data",
                timestamp = "timestamp",
                request_id = "request_id"
            }
        },
        
        error = {
            status = "error_code",
            body = {
                success = false,
                error = {
                    code = "error_code",
                    message = "error_message",
                    details = "error_details"
                },
                timestamp = "timestamp",
                request_id = "request_id"
            }
        }
    },
    
    -- Padrões de paginação
    pagination_patterns = {
        request = {
            page = { type = "integer", default = 1 },
            limit = { type = "integer", default = 10 },
            offset = { type = "integer", default = 0 }
        },
        
        response = {
            data = "array",
            pagination = {
                page = "integer",
                limit = "integer",
                total = "integer",
                pages = "integer"
            }
        }
    }
}
```

### **🔌 WebSocket API Template**
```lua
-- Template para APIs WebSocket
local WebSocketAPITemplate = {
    metadata = {
        name = "websocket_api",
        version = "1.0.0",
        description = "WebSocket API template for OTClient-Canary integration"
    },
    
    -- Padrões de mensagem
    message_patterns = {
        -- Mensagem de conexão
        connect = {
            type = "connect",
            data = {
                client_id = "string",
                client_version = "string",
                capabilities = "array"
            }
        },
        
        -- Mensagem de autenticação
        authenticate = {
            type = "authenticate",
            data = {
                token = "string",
                session_id = "string"
            }
        },
        
        -- Mensagem de heartbeat
        heartbeat = {
            type = "heartbeat",
            data = {
                timestamp = "timestamp",
                client_time = "timestamp"
            }
        },
        
        -- Mensagem de evento
        event = {
            type = "event",
            data = {
                event_type = "string",
                event_data = "object",
                timestamp = "timestamp"
            }
        },
        
        -- Mensagem de erro
        error = {
            type = "error",
            data = {
                error_code = "integer",
                error_message = "string",
                error_details = "object"
            }
        }
    },
    
    -- Padrões de evento
    event_patterns = {
        -- Eventos de jogo
        game_events = {
            "player_move",
            "creature_spawn",
            "item_drop",
            "combat_start",
            "combat_end"
        },
        
        -- Eventos de sistema
        system_events = {
            "module_load",
            "module_unload",
            "config_change",
            "error_occurred"
        }
    }
}
```

---

## 🧪 **5. Testing API Templates**

### **🔬 Test API Template**
```lua
-- Template para APIs de teste
local TestAPITemplate = {
    metadata = {
        name = "test_api",
        version = "1.0.0",
        description = "Testing API template for OTClient-Canary integration"
    },
    
    endpoints = {
        -- Testes de conectividade
        connectivity = {
            ping = {
                method = "GET",
                path = "/api/test/ping",
                description = "Test basic connectivity"
            },
            
            health_check = {
                method = "GET",
                path = "/api/test/health",
                description = "Comprehensive health check"
            }
        },
        
        -- Testes de performance
        performance = {
            latency_test = {
                method = "GET",
                path = "/api/test/latency",
                description = "Test API latency"
            },
            
            throughput_test = {
                method = "POST",
                path = "/api/test/throughput",
                description = "Test API throughput"
            }
        },
        
        -- Testes de funcionalidade
        functionality = {
            echo = {
                method = "POST",
                path = "/api/test/echo",
                description = "Echo back request data",
                parameters = {
                    data = { type = "any", required = true }
                }
            },
            
            validate = {
                method = "POST",
                path = "/api/test/validate",
                description = "Validate request format",
                parameters = {
                    schema = { type = "string", required = true },
                    data = { type = "any", required = true }
                }
            }
        }
    }
}
```

---

## 📝 **6. Implementação de Referência**

### **🎯 Template de Implementação**
```lua
-- Template para implementação de API unificada
local APIImplementationTemplate = {
    -- Inicialização da API
    initialize = function(config)
        local api = {
            config = config or {},
            endpoints = {},
            middleware = {},
            error_handlers = {}
        }
        
        -- Configurar middleware padrão
        api:add_middleware("cors")
        api:add_middleware("authentication")
        api:add_middleware("logging")
        
        return api
    end,
    
    -- Adicionar endpoint
    add_endpoint = function(self, method, path, handler, options)
        self.endpoints[method .. ":" .. path] = {
            handler = handler,
            options = options or {}
        }
    end,
    
    -- Adicionar middleware
    add_middleware = function(self, middleware)
        table.insert(self.middleware, middleware)
    end,
    
    -- Tratamento de erro
    handle_error = function(self, error_code, error_message)
        return {
            success = false,
            error = {
                code = error_code,
                message = error_message
            }
        }
    end,
    
    -- Resposta de sucesso
    handle_success = function(self, data)
        return {
            success = true,
            data = data
        }
    end
}
```

### **🧪 Testes de API**
```lua
-- Testes para APIs unificadas
local APITests = {
    -- Testes de conectividade
    connectivity_tests = {
        "test_api_connection",
        "test_authentication",
        "test_heartbeat"
    },
    
    -- Testes de funcionalidade
    functionality_tests = {
        "test_endpoint_responses",
        "test_error_handling",
        "test_data_validation"
    },
    
    -- Testes de performance
    performance_tests = {
        "test_response_time",
        "test_throughput",
        "test_concurrent_requests"
    },
    
    -- Testes de segurança
    security_tests = {
        "test_authentication",
        "test_authorization",
        "test_input_validation"
    }
}
```

---

## 🎯 **7. Próximos Passos**

### **📋 Tarefas de Implementação**
1. **Validar templates** com implementação real
2. **Testar APIs** em ambiente real
3. **Documentar endpoints** específicos do Canary
4. **Criar exemplos** de implementação
5. **Estabelecer testes** automatizados

### **🔄 Integração Futura**
- **Fase 1**: Preparação e estrutura (ATUAL)
- **Fase 2**: Implementação básica
- **Fase 3**: Testes e validação
- **Fase 4**: Deploy e monitoramento

---

**Documento Criado**: 2025-01-27  
**Responsável**: Epic 3.3 - Criar Templates de APIs Unificadas  
**Status**: ✅ **COMPLETO**  
**Próximo**: Epic 3.4 - Preparar Guias de Integração 