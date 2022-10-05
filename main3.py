#калькулятор для комплексных чисел с логированием
from telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

bot = Bot(token='5644828597:AAFsWAWd0odE-9lN9h_okaySHTGTJEe4L00')
updater = Updater(token='5644828597:AAFsWAWd0odE-9lN9h_okaySHTGTJEe4L00')
dispatcher = updater.dispatcher

def init(update, context):
    global number1,number2
    number1 = update.message.text
    number2 = update.message.text
    context.bot.send_message(update.effective_chat.id, f'Вы ввели числа {number1} и {number2}')


def choice(update, context):
    context.bot.send_message(update.effective_chat.id, f'выберите операцию, которую нужно произвести с введенными данными: \n 1 - Сложение \n 2 - деление \n 3-Вычитание \n 4- умножение')
    choice = update.message.text
    if choice=='1':
         context.bot.send_message(update.effective_chat.id, f'Сумма введенных чисел: {number1} + {number2} = {number1 + number2}')
    if choice=='2':
         context.bot.send_message(update.effective_chat.id, f'Частное введенных чисел: {number1} / {number2} = {number1 / number2}')
    if choice=='3':
         context.bot.send_message(update.effective_chat.id, f'Разность введенных чисел: {number1} - {number2} = {number1 - number2}')
    if choice=='4':
         context.bot.send_message(update.effective_chat.id, f'Произведение введенных чисел: {number1} * {number2} = {number1 * number2}')
    
    



def message(update, context):
    text = update.message.text
    text1= text.replace('абв', "")
    context.bot.send_message(update.effective_chat.id, f'{text1}\t Я не знаю букв сочетания букв абв :)')


message_handler = MessageHandler(Filters.text, message)


dispatcher.add_handler(message_handler)

updater.start_polling()
updater.idle()  # ctrl + c
