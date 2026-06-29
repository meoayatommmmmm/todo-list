import telebot
import arch 
import os 

bot = telebot.TeleBot("8468539381:AAHPewDiHd_B9ttrlRhxJqOx2t9c4v1xinM")

main_button_1 = telebot.types.ReplyKeyboardMarkup()
button_1 = telebot.types.KeyboardButton('показать задачу')
main_button_1.row(button_1)

def read_py_file():
    return arch.todos

todos = read_py_file()

@bot.message_handler(regexp='start')
def start(command):
    bot.send_message(command.chat.id, "hello", reply_markup=main_button_1)

@bot.message_handler(regexp='показать задачу')
def listtodo(command):
    for user, tasks in todos.items():
        bot.send_message(command.chat.id, f"Пользователь: {user}")
        for task in tasks:
            status = "✅ выполнено" if task['done'] else "⬜ не выполнено"
            bot.send_message(command.chat.id, f"{status} — {task['text']}")

bot.polling()
