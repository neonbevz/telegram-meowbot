import os
import logging
import telegram.ext
from telegram.error import NetworkError, Unauthorized
from time import sleep
import random


TOKEN = '532795634:AAFxEdOiKyfAdreJDp48I32bXZfSbWsIUto'
PORT = int(os.environ.get('PORT', '8443'))

MEOWS = ['Meow', 'Meow meow', 'Meooow']
ENDINGS = ['', '.', '?', '!']
START = 'Meow!'
HELP = 'Meow.'


def main():
    updater = telegram.ext.Updater(TOKEN)
    # add handlers
    dp = updater.dispatcher

    dp.add_handler(telegram.ext.CommandHandler('start', start))
    dp.add_handler(telegram.ext.CommandHandler('help', help))

    updater.start_webhook(listen='0.0.0.0',
                          port=PORT,
                          url_path=TOKEN)
    updater.bot.set_webhook('https://telegram-meowbot.herokuapp.com/' + TOKEN)
    updater.idle()


def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=START)


def help(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=HELP)


def handle_update(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=generate_response(update.message.text))


def generate_response(text):
    response = random.choice(MEOWS) + random.choice(ENDINGS)
    return response


if __name__ == "__main__":
    while True:
        try:
            main()
            break
        except NetworkError as ne:
            print(ne)
            continue
