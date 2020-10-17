
import telebot
# import json

bot = telebot.TeleBot('841729239:AAG9QCGYlTReRnwVgYOuLY6JwN6c5ZAN-HM')


keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Привет', 'Пока')


@bot.message_handler(commands=['start'])
def start_message(message):
    hello = bot.send_message(message.chat.id, text=' Привет, ' + message.from_user.first_name + '\nты написал мне '
                                                                                                '/start', reply_markup=keyboard1)
    return print(hello)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, пользователь')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'До скорой встречи')



bot.polling()
