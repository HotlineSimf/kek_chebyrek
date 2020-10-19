import telebot
import requests
import threading
import time


# 1080870764:AAGfKfQK8HpaKtGvovOlJtPekhIRtzL8L3s
BOT_TOKEN = ''
USERS_TOKEN = ['']
bot = telebot.TeleBot(BOT_TOKEN)


def parse(city):  # функция парсит синоптик и ищет гифку, максимум и минимум
    city = 'киев'
    inner_html = requests.get(
        "https://sinoptik.ua/погода-"+city+"/10-дней").text
    img = inner_html.split("""<img class="weatherImg" src=""")[1]
    minimum = img.split("alt=")[1]
    img = img.split("alt=")[0]
    img = img[1:len(img)-2]
    minimum = minimum.split("""<div class="min">мин. <span>""")[1]
    maximum = minimum.split("""&deg;</span></div>""")[1]
    minimum = minimum.split("""&deg;</span></div>""")[0]
    maximum = maximum.split("""<div class="max">макс. <span>""")[1]
    maximum = maximum.split("""&deg;</span></div>""")[0]
    output = [img, minimum,
              maximum]  # будем считать стандартным набором информации weather
    return output


def send_weather_without_handler(token, weather):
    bot.send_message(token, "min = " + weather[1] + "max = " + weather[2])


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(
        message.chat.id, 'Привіт, я скажу тобі погоду у Києві! Хочеш дізнатися про погоду? Використай /weather')


@bot.message_handler(commands=['me'])
def me(message):
    bot.send_message(message.chat.id, message.chat.id)


@bot.message_handler(commands=['weather'])
def weather_message(message):
    weather = parse("киев")
    bot.send_message(message.chat.id, "min = " +
                     weather[1] + " max = " + weather[2])


@bot.message_handler(content_types=['text'])
def send_text(message):
    bot.reply_to(message, "Пробач, я тебе не розумію...")


def demonfunc():
    while True:
        print('daemon')
        if time.strftime("%H") == '10':
            for user in USERS_TOKEN:
                send_weather_without_handler(user, parse("киев"))
        time.sleep(3600)


daemon = threading.Thread(target=demonfunc)

daemon.start()

bot.polling()
