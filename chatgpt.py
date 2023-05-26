import os
os.environ['KMP_DUPLICATE_LIB_OK'] = 'True'
import openai
import telebot

# Configurar sua chave de API do OpenAI
openai.api_key = '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'

# Configurar o token do seu bot do Telegram
TOKEN = '6241260221:AAE8mYPaVJFFu56BQuOYRAOv4H31SPf_BpI'

# Criar uma instância do bot
bot = telebot.TeleBot(TOKEN)

# Lidar com o comando /start
@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Sou seu assistente virtual, primo do CHATGPT. Como posso ajudar?")

# Lidar com o comando /help
@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "Estou aqui para responder às suas perguntas. Basta digitar sua mensagem.")

# Lidar com as mensagens
@bot.message_handler(func=lambda message: True)
def handle_message(message):
    resposta = gpt3_responder(message.text)
    bot.send_message(message.chat.id, resposta)

# Função para obter a resposta do ChatGPT
def gpt3_responder(mensagem):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=mensagem,
        max_tokens=2000,
        temperature=0.7
    )

    return response.choices[0].text.strip()

# Iniciar o bot
bot.polling()
