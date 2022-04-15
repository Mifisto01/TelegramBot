import telebot
from telebot import types


bot = telebot.TeleBot('5363872993:AAHZ82agzCnjBPId8foR_HqX0opTHCaToNU')
                                                                                                                                                           # С помощью данной программы выводится при команде Хелп и Старт - Привет
@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, <b>{message.from_user.first_name} <u>{message.from_user.last_name}</u></b>'   #выводит Привет, Имя(жирным шрифтом) и Фамилию(жирным и подчеркнутым шрифтом)
    bot.send_message(message.chat.id, mess, parse_mode='html')                                                             #сюда добовляем все что написанно выше
    
#@bot.message_handler(content_types=['text'])                                                                                                                        #обработка текста
#def get_user_text(message):
#    if message.text == "Привет":                                                                                                                 #то что вводит пользователь
#       bot.send_message(message.chat.id, "И тебе привет, Бро!", parse_mode='html')                               #то что выведет бот
#    elif message.text == "id":
#        bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')           #то что выведет бот
#    elif message.text == "фото":                                                                                                              #вывести фото для пользователя на его запрос
#        photo = open('C:\\Users\profi.mag008\Desktop\Papa.jpg', 'rb')                                                        #тут открываем фото с компа, а так же можем указать какой формат
#        bot.send_photo(message.chat.id, photo)
#    else:
#        bot.send_message(message.chat.id, "Я тебя не понял, слушай...", parse_mode='html')

@bot.message_handler(content_types=['photo'])                                                                                       #отслеживани текста, стикеров, фото и тд.
def get_user_photo(message):
    bot.send_message(message.chat.id, 'Вау, круто')                                                                                  #так же обязательно прогружать формат загруженных аудио видео и фото
    
@bot.message_handler(commands=['website'])                                                                                          #создание кнопок
def website(message):
    markup=types.InlineKeyboardMarkup()                                                                                               #тайпс импортируем с верху, инлайн-простая кнопка
    markup.add(types.InlineKeyboardButton("Посетить веб сайт", url="https://youtube.com/"))
    bot.send_message(message.chat.id, "Перейли", parse_mode='html', reply_markup=markup)

@bot.message_handler(commands=['help'])                                                                                          #создание кнопок в поле для ввода текста
def website(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)                                                                                           #тайпс импортируем с верху, инлайн-простая кнопка
    website=types.KeyboardButton('Вебсайт')                                                                                       #добавление кнопок
    start=types.KeyboardButton('Старт')
    markup.add(types.InlineKeyboardButton("Посетить веб сайт", url="https://youtube.com/"))
    bot.send_message(message.chat.id, "Перейли", parse_mode='html', reply_markup=markup)





bot.polling(none_stop=True)
