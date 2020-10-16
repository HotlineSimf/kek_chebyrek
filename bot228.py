import telebot

bot = telebot.TeleBot('1080870764:AAGfKfQK8HpaKtGvovOlJtPekhIRtzL8L3s')
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Привет', 'Пока')

@bot.message_handler(commands=['help'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start', reply_markup=keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    bot.reply_to(message, message.text+" , говоришь?" ) #ответить на все
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Прощай, создатель')
    elif message.text.lower() == 'я тебя люблю':
        bot.send_message(message.chat.id, 'а я люблю кодить')

@bot.message_handler(content_types=['sticker'])
def sticker_id(message):
    print(message)

 bot.polling()#фукция, зставляющая бота работать в цикле
