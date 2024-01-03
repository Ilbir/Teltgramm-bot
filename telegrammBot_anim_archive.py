from telebot import *
token = open('list_anim_bot.txt').readline()
bot = TeleBot(f'{token}') #попробоваать поменять имя и во всех строках с @bot

#@bot.message_handler(content_types=['text']) #отслеживание сообщений - текст
#def test_hello(message): #любое название def

@bot.message_handler(commands = ['start']) #отслеживание сомманды - start
def starting(mes): #получаем на вход параметр сообщения от пользователя(любое название)
    print(mes.text)
    bot.send_message(mes.chat.id, 'Бот работает') #есть не только отправка сообщения(стикеры, анимки, действие и т.д.) 
    #(к строчке сверху) указываем обязательно: в какой чат отправляем(в данном случае получаем id чата через полученное сообщение)
    # и сам текст
    #(необязательно) режим отправки текста (просто текст или html(тогда можно использовать html теги(пример ниже)))
    user_name = [mes.from_user.first_name, mes.from_user.last_name] #получить информацию о пользователе - имя, фамилия
    bot.send_message(mes.chat.id, f'<b>{user_name[0]}</b>', parse_mode = 'html')

@bot.message_handler()
def get_send(message):
    print(message.text)
    #bot.send_message(message.chat.id, message) #вернуть всю информацию, хранящуюся в message
    if message.text == '1': #если текст сообщения - 1
        bot.send_message(message.chat.id, message.text)
    else:
        bot.send_message(message.chat.id, '2')

bot.polling(none_stop=True) #постоянная работа бота
#сделать reply или inline кнопки
