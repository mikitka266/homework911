#Создайте программу для игры с конфетами человек против бота(интелект).

from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

bot = Bot(token='5644828597:AAFsWAWd0odE-9lN9h_okaySHTGTJEe4L00')
updater = Updater(token='5644828597:AAFsWAWd0odE-9lN9h_okaySHTGTJEe4L00')
dispatcher = updater.dispatcher

candies= int(input('Введите количество конфет'))

def start (update, context):
    global candies, max_move
    candies=(context.bot.send_message(update.effective_chat.id, "Cколько конфет в игре?"))
    max_move= (context.bot.send_message(update.effective_chat.id, "Cколько конфет можно брать за 1 ход максимально?"))

def first(update, context):
    move_1 = context.bot.send_message(update.effective_chat.id, "Cколько конфет вы возьмете?")
    move_1_bot = context.bot.send_message(update.effective_chat.id, f"бот взял {(candies-move_1)%max_move}?")
    if move_1_bot ==0:
        move_1_bot ==1
        context.bot.send_message(update.effective_chat.id, f'А Вы умеете считать!')    
    candies = candies - (move_1 +  move_1_bot)
    context.bot.send_message(update.effective_chat.id, f'вы взяли {move_1 } конфет, бот взял {move_1_bot } конфет, осталось {candies} конфет  ')
 


def message(update, context):
    while candies> max_move:
        move = context.bot.send_message(update.effective_chat.id, "Cколько конфет вы возьмете?")
        move_bot= 29-move
        candies= candies - move - move_bot
        context.bot.send_message(update.effective_chat.id, f'Бот возьмет{move_bot}конфет, на столе останется {candies}')
        if candies==max_move:
             context.bot.send_message(update.effective_chat.id, f'Бот победил')
        if candies<max_move:
             context.bot.send_message(update.effective_chat.id, f'Вы победили высокоинтеллектуального бота, ваш IQ предположительно 1000')
        


start_handler = MessageHandler(Filters.text, start)       
first_handler = MessageHandler(Filters.text, first)
message_handler = MessageHandler(Filters.text, message)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(first_handler)
dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()  # ctrl + c