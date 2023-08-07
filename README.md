# Bot de Tarot no Telegram

Este é um bot de Tarot para o aplicativo de mensagens Telegram. O bot fornece leituras de Tarot interativas e orientações com base nas cartas tiradas e na pergunta do usuário.

## Funcionalidades

- O bot responde ao comando `/start` para iniciar a interação.
- O usuário pode fazer uma pergunta ao Tarot, e o bot seleciona aleatoriamente cinco cartas para responder à pergunta.
- O bot aciona a API do ChatGPT para fornecer interpretações personalizadas das cartas e orientações adicionais com base na pergunta do usuário.
- Após a resposta, o bot oferece a opção de reiniciar a interação.

## Pré-requisitos

- Python 3.x
- Bibliotecas Python: `telebot`, `openai`

## Configuração

1. Clone o repositório para sua máquina local.
2. Instale as dependências usando o seguinte comando:
   ```
   pip install -r requirements.txt
   ```
3. Configure o bot no Telegram:
   - Crie um novo bot no Telegram e obtenha o token do bot.
   - Substitua `'SEU_TOKEN_AQUI'` no código pelo token do seu bot.

4. Configure a API do OpenAI:
   - Crie uma conta no OpenAI e obtenha sua chave de API.
   - Substitua `'SUA_API_KEY_DO_OPENAI'` no código pela sua chave de API.

## Uso

1. Execute o script `bot.py` para iniciar o bot:
   ```
   python bot.py
   ```
2. No Telegram, procure pelo nome do seu bot e inicie a interação enviando o comando `/start`.
3. Digite sua pergunta para o Tarot e aguarde a resposta do bot.

## Contribuição

Contribuições são bem-vindas! Se você tiver sugestões, correções ou novas funcionalidades para adicionar, sinta-se à vontade para abrir um PR (pull request).