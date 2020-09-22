import telebot
import config
#from telebot import apihelper
from telebot import types


bot = telebot.TeleBot(config.token)
#apihelper.proxy = {'https': config.proxy_name}


@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(True)
    markup.row('камень', 'ножницы', 'бумага')
    bot.send_message(message.from_user.id, "выбери значение:", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == "привет":
        bot.send_message(message.from_user.id, "Привет! давай сыгрем, командуй /start")
    elif message.text in ["камень","ножницы","бумага"]:
        bot.send_message(message.from_user.id, "Играем")
    elif message.text == "/help":
        bot.send_message(message.from_user.id, "Привет! если хочешь сыграть напиши /start")
    else:
        bot.send_message(message.from_user.id, "Ты сказал " + message.text)

if __name__ == '__main__':
    bot.polling(none_stop=True, interval=0)
