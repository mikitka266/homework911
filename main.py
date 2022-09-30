from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler

bot = Bot(token='')
updater = Updater(token='')
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(update.effective_chat.id, 'Привет\nКак твои дела?')


start_handler = CommandHandler('start', start)


dispatcher.add_handler(start_handler)

updater.start_polling()
updater.idle()  # ctrl + c
