from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

bot = Bot(token='5644828597:AAFsWAWd0odE-9lN9h_okaySHTGTJEe4L00')
updater = Updater(token='5644828597:AAFsWAWd0odE-9lN9h_okaySHTGTJEe4L00')
dispatcher = updater.dispatcher


def message(update, context):
    text = update.message.text
    context.bot.send_message(update.effective_chat.id, f'{text * 10}\t Я повторюшка :)')


message_handler = MessageHandler(Filters.text, message)


dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()  # ctrl + c
