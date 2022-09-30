from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

bot = Bot(token='')
updater = Updater(token='')
dispatcher = updater.dispatcher


def voice(update, context):
    context.bot.send_message(update.effective_chat.id, 'Надоели Ваши голосовые сообщения! Не умею я их читать!')


voice_handler = MessageHandler(Filters.voice, voice)


dispatcher.add_handler(voice_handler)

updater.start_polling()
updater.idle()  # ctrl + c
