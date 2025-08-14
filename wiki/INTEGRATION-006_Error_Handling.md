---
tags: [integration, error-handling, otclient, canary]
status: 'in-progress'
aliases:
  - Tratamento de Erros
  - Error Handling
---

# Página "Tratamento de Erros"

## 1. Explicação Teórica

O tratamento de erros é um componente crítico de qualquer software robusto. Ele garante que o sistema possa lidar com condições inesperadas—seja uma falha de rede, um arquivo corrompido ou entrada inválida—sem travar ou se comportar de maneira imprevisível. Em sistemas complexos como o OTClient e o Canary, um tratamento de erros eficaz é fundamental para a estabilidade e a experiência do usuário.

As principais estratégias abordadas neste documento são o uso de blocos `try/catch` em C++ para o manejo de exceções e a verificação de retornos de funções.

---

## 2. Abordagem de Tratamento de Erros no OTClient

O OTClient, sendo uma aplicação C++ com uma camada de script em Lua, concentra seu tratamento de erros na camada C++. A estratégia principal é o uso extensivo de blocos `try/catch` para capturar exceções em tempo de execução.

### Exemplos Práticos de Código (OTClient)

#### a) Gerenciamento de Interface Gráfica (`UIMananger`)

No arquivo `framework/ui/uimanager.cpp`, múltiplos eventos de interface gráfica são envolvidos em blocos `try/catch` para evitar que um erro em um único widget cause o travamento de toda a UI.

```cpp
// Extraído de otclient/src/framework/ui/uimanager.cpp

void UIManager::sendWidgetUpdate(const UIWidgetPtr& widget)
{
    // ...
    try {
        if(!widget->isDestroyed())
            widget->update();
    } catch (stdext::exception& e) {
        g_logger.error(stdext::format("failed to update widget #%d: %s", widget->getId(), e.what()));
    }
    // ...
}
```
**Análise**: Este padrão protege o loop de atualização da UI. Se um widget específico falhar durante sua atualização, o erro é registrado (`g_logger.error`) e o resto da aplicação continua funcionando normalmente.

#### b) Carregamento de Recursos (`TextureManager`)

Ao carregar texturas, que podem estar ausentes ou corrompidas, o tratamento de erros é crucial para evitar o fechamento abrupto do cliente.

```cpp
// Extraído de otclient/src/framework/graphics/texturemanager.cpp

TexturePtr TextureManager::getTexture(const std::string& fileName)
{
    // ...
    try {
        ImagePtr image = Image::load(realPath);
        texture->upload(image);
    } catch (const stdext::exception& e) {
        g_logger.error(stdext::format("failed to load texture '%s': %s", fileName, e.what()));
    }
    return texture;
}
```
**Análise**: Se o carregamento de uma imagem (`Image::load`) ou o upload para a GPU (`texture->upload`) falhar, a exceção é capturada, um erro é logado, e o programa continua sua execução, geralmente com uma textura "padrão" ou invisível.

---

## 3. Abordagem de Tratamento de Erros no Canary

O servidor Canary também é escrito em C++, mas seu código Lua não utiliza a função `pcall` para tratamento de erros. A lógica de tratamento de exceções está quase que inteiramente na camada C++, que é responsável por gerenciar o banco de dados, a rede e a lógica principal do jogo.

### Exemplos Práticos de Código (Canary)

#### a) Operações de Rede (`Connection`)

No servidor, lidar com conexões de rede que podem cair ou enviar dados malformados é essencial.

```cpp
// Extraído de canary/src/server/network/connection/connection.cpp

void Connection::receive()
{
    // ...
    asio::async_read(*socket, asio::buffer(headerBuffer, HEADER_SIZE),
        [this, self](const std::error_code& error, std::size_t)
        {
            try {
                if (error) {
                    handleError(error);
                    return;
                }
                // ...
            } catch (const std::system_error& e) {
                SPDLOG_ERROR("system_error in Connection::receive, error: {}", e.what());
                disconnect();
            }
        });
}
```
**Análise**: O tratamento de erros de rede é feito de forma assíncrona. Qualquer erro de sistema (`std::system_error`) ou erro de leitura (`error`) é capturado, logado usando `SPDLOG_ERROR`, e a conexão do cliente é encerrada (`disconnect()`), protegendo o resto do servidor.

#### b) Operações de Banco de Dados (`Database`)

Consultas ao banco de dados podem falhar por uma infinidade de razões. O Canary protege essas operações para garantir a integridade dos dados.

```cpp
// Extraído de canary/src/database/database.hpp

bool get(const std::string& key, std::string& value) {
    try {
        leveldb::Status status = db->Get(leveldb::ReadOptions(), key, &value);
        return status.ok();
    } catch (const std::exception& exception) {
        SPDLOG_ERROR("Failed to get value from database, exception: {}", exception.what());
        return false;
    }
}
```
**Análise**: Uma operação de leitura no banco de dados LevelDB é encapsulada em um `try/catch`. Se qualquer exceção padrão (`std::exception`) ocorrer, o erro é logado e a função retorna `false`, indicando que a operação falhou sem travar o servidor.

---

## 4. Conclusão e Boas Práticas

Ambos os projetos, OTClient e Canary, adotam uma estratégia robusta de tratamento de erros focada na camada C++, utilizando blocos `try/catch` para isolar falhas e registrá-las em logs detalhados.

-   **No OTClient**: O foco é garantir a fluidez da experiência do usuário, impedindo que falhas em subsistemas (UI, som, gráficos) travem o cliente.
-   **No Canary**: O foco é a estabilidade e a integridade do servidor, garantindo que falhas de rede ou de banco de dados não comprometam o estado do jogo.

Para desenvolvedores, a prática recomendada é sempre envolver operações de I/O (rede, disco) e interações com subsistemas externos em blocos `try/catch`, além de logar informações de erro detalhadas para facilitar a depuração.
