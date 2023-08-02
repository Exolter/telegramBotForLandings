import telebot
from telebot import types

TOKEN = ''

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('Каталог сайтів')
    item2 = types.KeyboardButton('Допомога')
    item3 = types.KeyboardButton('Постачальники')

    markup.add(item1, item2, item3)

    bot.send_message(message.chat.id, 'Вітаю, {0.first_name}! В каталозі ви зможете знайти всі доступні на зараз сайти ;)'.format(message.from_user), reply_markup = markup)

bot.polling(non_stop = True)
