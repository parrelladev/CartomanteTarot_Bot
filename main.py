import telebot
import random
import openai
import os

# Insira o token do seu bot do Telegram aqui
bot_token = 'SUA_API_KEY_DO_OPENAI'
bot = telebot.TeleBot(bot_token)

# Configuração da API do OpenAI
openai.api_key = 'SUA_API_KEY_DO_OPENAI'

# Mensagem de boas-vindas
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Olá! Eu sou o CartomanteTarot_Bot. Por favor, digite a pergunta que você deseja fazer ao Tarot e espere eu fazer a leitura das cartas.")

# Gerar as cartas de Tarot aleatoriamente
def gerar_cartas():
    cartas = [
        "O Louco",
        "O Mago",
        "A Sacerdotisa",
        "A Imperatriz",
        "O Imperador",
        "O Hierofante",
        "Os Amantes",
        "A Carruagem",
        "A Justiça",
        "O Eremita",
        "A Roda da Fortuna",
        "A Força",
        "O Enforcado",
        "A Morte",
        "A Temperança",
        "O Diabo",
        "A Torre",
        "A Estrela",
        "A Lua",
        "O Sol",
        "O Julgamento",
        "O Mundo"
    ]

    return random.sample(cartas, 5)

# Comando para receber a pergunta e mostrar as cartas de Tarot
@bot.message_handler(func=lambda message: True)
def interpretar_tarot(message):
    pergunta_usuario = message.text

    # Gerar as cartas aleatoriamente
    cartas_tiradas = gerar_cartas()

    # Montar a mensagem das cartas tiradas
    mensagem_cartas = "\n".join([f"{i+1}. {carta}" for i, carta in enumerate(cartas_tiradas)])

    # Enviar a mensagem com as cartas ao usuário
    resposta = (
        f"🧙‍♀️ Acabei de tirar do baralho algumas cartas aleatórios para você. Elas são:\n\n"
        f"{mensagem_cartas}\n\n"
    )

    # Enviar a mensagem com as cartas e o botão de reinício ao usuário
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    reiniciar_botao = telebot.types.KeyboardButton('/start')
    markup.add(reiniciar_botao)

    bot.send_message(message.chat.id, resposta, reply_markup=markup)
    

    # Acionar a API do ChatGPT
    prompt_gpt = (
        "A partir de agora, você deve agir como um interpretador e cartomante de tarot. "
        "Gostaria que você interpretasse as cartas que serão indicadas pelo usuário e fornecesse "
        "alguma orientação ou reflexão adicional com base na combinação delas. Por favor, ajude o usuário a "
        "compreender melhor as mensagens ocultas do tarot para a situação que será também será informada pelo usuário.\n\n"
    )

    cartas_para_gpt = "\n".join(cartas_tiradas)
    prompt_gpt += cartas_para_gpt + "\n\n" + pergunta_usuario

    # Chamar a API do ChatGPT usando a biblioteca openai
    resposta_gpt = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt_gpt,
        max_tokens=400
    )

    # Extrair a resposta do GPT da API
    resposta_texto = resposta_gpt.choices[0].text.strip()

    # Enviar a resposta do GPT para o usuário
    bot.send_message(message.chat.id, resposta_texto, reply_markup=markup)

# Iniciar o bot
bot.polling()
