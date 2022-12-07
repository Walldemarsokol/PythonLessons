import telebot
from telebot import types
from sourse import token
import telebot
from telebot import types
from bs4 import BeautifulSoup
import requests

bot = telebot.TeleBot(token)


def test_weather(message):
    markup = types.InlineKeyboardMarkup(row_width=5)
    item13 = types.InlineKeyboardButton("📍 Москва", callback_data='13')
    item14 = types.InlineKeyboardButton("📍 Санкт-Петербург", callback_data='14')
    item15 = types.InlineKeyboardButton("📍 Новосибирск", callback_data='15')
    item16 = types.InlineKeyboardButton("📍 Екатеринбург", callback_data='16')
    item17 = types.InlineKeyboardButton("📍 Казань", callback_data='17')
    item18 = types.InlineKeyboardButton("📍 Нижний Новгород", callback_data='18')
    item19 = types.InlineKeyboardButton("📍 Челябинск", callback_data='19')
    item20 = types.InlineKeyboardButton("📍 Красноярск", callback_data='20')
    item21 = types.InlineKeyboardButton("📍 Самара", callback_data='21')
    item22 = types.InlineKeyboardButton("📍 Уфа", callback_data='22')
    item23 = types.InlineKeyboardButton("📍 Ростов-на-Дону", callback_data='23')
    item24 = types.InlineKeyboardButton("📍 Омск", callback_data='24')
    markup.add(item13)
    markup.add(item14)
    markup.add(item15)
    markup.add(item16)
    markup.add(item17)
    markup.add(item18)
    markup.add(item19)
    markup.add(item20)
    markup.add(item21)
    markup.add(item22)
    markup.add(item23)
    markup.add(item24)
    bot.send_message(message.chat.id, 'Выберете город:', reply_markup=markup)


def weather(message_text):
    if message_text == '13':
        url = 'https://yandex.com.am/weather/?lat=55.75581741&lon=37.61764526'
    if message_text == '14':
        url = 'https://yandex.com.am/weather/?lat=59.93909836&lon=30.31587601'
    if message_text == '15':
        url = 'https://yandex.com.am/weather/?lat=55.03020096&lon=82.92043304'
    if message_text == '16':
        url = 'https://yandex.com.am/weather/?lat=56.8380127&lon=60.59747314'
    if message_text == '17':
        url = 'https://yandex.com.am/weather/?lat=55.79612732&lon=49.10641479'
    if message_text == '18':
        url = 'https://yandex.com.am/weather/?lat=56.32679749&lon=44.00651932'
    if message_text == '19':
        url = 'https://yandex.com.am/weather/?lat=55.15990067&lon=61.40255737'
    if message_text == '20':
        url = 'https://yandex.com.am/weather/?lat=56.01056671&lon=92.85257721'
    if message_text == '21':
        url = 'https://yandex.com.am/weather/?lat=53.19587708&lon=50.10020065'
    if message_text == '22':
        url = 'https://yandex.com.am/weather/?lat=54.73514938&lon=55.9587326'
    if message_text == '23':
        url = 'https://yandex.com.am/weather/?lat=47.22208023&lon=39.72035599'
    if message_text == '24':
        url = 'https://yandex.com.am/weather/?lat=54.98934555&lon=73.36821747'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "lxml")
    return (bs.find('h1', 'title title_level_1 header-title__title').text + '\n' +
            bs.find('span', 'temp__value temp__value_with-unit').text + '°C, ' +
            bs.find('div', 'link__condition day-anchor i-bem').text + '\nВетер: ' +
            bs.find('span', 'wind-speed').text + ' ' + bs.find('span', 'fact__unit').text + '\n' +
            bs.find('div', 'term term_orient_h fact__feels-like').text + '°C')



def test_goroscop(message):
    markup = types.InlineKeyboardMarkup(row_width=5)
    item1 = types.InlineKeyboardButton("♈ Овен", callback_data='1')
    item2 = types.InlineKeyboardButton("♉ Телец", callback_data='2')
    item3 = types.InlineKeyboardButton("♊ Близнецы", callback_data='3')
    item4 = types.InlineKeyboardButton("♋ Рак", callback_data='4')
    item5 = types.InlineKeyboardButton("♌ Лев", callback_data='5')
    item6 = types.InlineKeyboardButton("♍ Дева", callback_data='6')
    item7 = types.InlineKeyboardButton("♎ Весы", callback_data='7')
    item8 = types.InlineKeyboardButton("♏ Скорпион", callback_data='8')
    item9 = types.InlineKeyboardButton("♐ Стрелец", callback_data='9')
    item10 = types.InlineKeyboardButton("♑ Козерог", callback_data='10')
    item11 = types.InlineKeyboardButton("♒ Водолей", callback_data='11')
    item12 = types.InlineKeyboardButton("♓ Рыбы", callback_data='12')
    markup.add(item1)
    markup.add(item2)
    markup.add(item3)
    markup.add(item4)
    markup.add(item5)
    markup.add(item6)
    markup.add(item7)
    markup.add(item8)
    markup.add(item9)
    markup.add(item10)
    markup.add(item11)
    markup.add(item12)
    bot.send_message(message.chat.id, 'Выберете знак задиака:', reply_markup=markup)


def goroscop(message_text):
    if message_text == '1':
        url = 'https://horo.mail.ru/prediction/aries/tomorrow/'
    if message_text == '2':
        url = 'https://horo.mail.ru/prediction/taurus/tomorrow/'
    if message_text == '3':
        url = 'https://horo.mail.ru/prediction/gemini/tomorrow/'
    if message_text == '4':
        url = 'https://horo.mail.ru/prediction/cancer/tomorrow/'
    if message_text == '5':
        url = 'https://horo.mail.ru/prediction/leo/tomorrow/'
    if message_text == '6':
        url = 'https://horo.mail.ru/prediction/virgo/tomorrow/'
    if message_text == '7':
        url = 'https://horo.mail.ru/prediction/libra/tomorrow/'
    if message_text == '8':
        url = 'https://horo.mail.ru/prediction/scorpio/tomorrow/'
    if message_text == '9':
        url = 'https://horo.mail.ru/prediction/sagittarius/tomorrow/'
    if message_text == '10':
        url = 'https://horo.mail.ru/prediction/capricorn/tomorrow/'
    if message_text == '11':
        url = 'https://horo.mail.ru/prediction/aquarius/tomorrow/'
    if message_text == '12':
        url = 'https://horo.mail.ru/prediction/pisces/tomorrow/'
    response = requests.get(url)
    bs = BeautifulSoup(response.text, "lxml")
    return bs.find('div', 'article__item article__item_alignment_left article__item_html').text
    

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет ✌️ ")
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Погода сейчас (9р/сут)")
    item2 = types.KeyboardButton("Гороскоп (12р/сут)")
    markup.add(item1)
    markup.add(item2)
    bot.send_message(message.chat.id, '👇🏻Выберите нужный раздел👇🏻', reply_markup=markup)


@bot.message_handler(content_types=['text'])
def message_reply(message):
    if message.text == "Погода сейчас (9р/сут)":
        bot.send_message(message.chat.id, test_weather(message))
    elif message.text == "Гороскоп (12р/сут)":
        bot.send_message(message.chat.id, test_goroscop(message))


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    tag = int(call.data)
    if tag < 13:
        if call.message:
            bot.send_message(call.message.chat.id, text=goroscop(call.data))
    if tag > 12:
        if call.message:
            bot.send_message(call.message.chat.id, text=weather(call.data))



bot.infinity_polling()