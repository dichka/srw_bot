import telebot
import pickle
from nltk.stem import PorterStemmer as ps
import re
from nltk.corpus import stopwords

stemmer = ps()

API_TOKEN = open('config.txt')

bot = telebot.TeleBot(API_TOKEN.read())

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('Привет', 'Пока')


with open('dat.pickle', 'rb') as f:
    corpus = pickle.load(f)
    uniqueWords = pickle.load(f)

with open('mod.pickle', 'rb') as f:
    classifier_mnb = pickle.load(f)
    cv = pickle.load(f)


@bot.message_handler(commands=['start'])
def start_message(message):
    hello = bot.send_message(message.chat.id, text=' Привет, ' + message.from_user.first_name + '\nты написал мне '
                                                                                                '/start',
                             reply_markup=keyboard1)
    return print(hello)


@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, 'Привет, пользователь')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'До скорой встречи')
    else:
        corpus_bot = list()
        text = re.sub("[^a-zA-Z]", ' ', message.text)
        text = text.lower()
        text = text.split()
        text = [stemmer.stem(word) for word in text if not word in set(stopwords.words('english'))]
        text = ' '.join(text)
        corpus_bot.append(text)
        print(corpus_bot)
        test = cv.transform(corpus_bot).todense()
        if classifier_mnb.predict(test) == 1:
            bot.send_message(message.chat.id, 'Правда')
        else:
            bot.send_message(message.chat.id, 'Ложь')


bot.polling()
