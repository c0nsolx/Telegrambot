import telebot
from telebot import types

bot = telebot.TeleBot('5139247544:AAGdZ9VJANQOJhLJbhN7Z2-2Lis5DSnnaE8')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Hello {message.from_user.first_name} {message.from_user.last_name}, This is a telegram bot, through which you can find the logos of some German cars, pictures of cars and information about the brands of those cars. use /help command to get some information how to use bot'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler(commands=['help'])
def start(message):
    mess = 'Send your favourite car brand name starting with a capital letter + space + logo or photo or exhaust sound or website or models with space'
    bot.send_message(message.chat.id, mess, parse_mode='html')


@bot.message_handler()
# Bmw
def get_user_text(message):
    if message.text == "Bmw logo":
        photo = open('Pictures/BMW-logo.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        mess = 'Bmw logo'
        bot.send_message(message.chat.id, mess, parse_mode='html')

    if message.text == "Bmw photo":
        photo = open('Pictures/BMW-car.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        mess = 'Bmw photo'
        bot.send_message(message.chat.id, mess, parse_mode='html')

    if message.text == "Bmw sound":
        exhaust_sound = open('Audio files/Bmw.mp3', 'rb')
        bot.send_voice(message.chat.id, exhaust_sound)
        mess = 'random exhaust sound'
        bot.send_message(message.chat.id, mess, parse_mode='html')

    if message.text == "Bmw website":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Enter website",url="https://www.bmw.com"))
        bot.send_message(message.chat.id, 'Enter the website', reply_markup=markup)

    if message.text == "Bmw models":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Enter website", url="https://www.auto-data.net/en/bmw-brand-86"))
        bot.send_message(message.chat.id, 'Enter the website to see models', reply_markup=markup)

    # Mercedes

    if message.text == "Mercedes logo":
        photo = open('Pictures/MERCEDES-logo.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        mess = 'Mercedes logo'
        bot.send_message(message.chat.id, mess, parse_mode='html')

    if message.text == "Mercedes photo":
        photo = open('Pictures/MERCEDES-car.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        mess = 'Mercedes photo'
        bot.send_message(message.chat.id, mess, parse_mode='html')

    if message.text == "Mercedes sound":
        exhaust_sound = open('Audio files/Mercedes.mp3', 'rb')
        bot.send_voice(message.chat.id, exhaust_sound)
        mess = 'random exhaust sound'
        bot.send_message(message.chat.id, mess, parse_mode='html')

    if message.text == "Mercedes website":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Enter website",url="https://www.mercedes-benz.com/en/"))
        bot.send_message(message.chat.id, 'Enter the website', reply_markup=markup)

    if message.text == "Mercedes models":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Enter website",url="https://www.auto-data.net/en/mercedes-benz-brand-138"))
        bot.send_message(message.chat.id, 'Enter the website to see models', reply_markup=markup)


    # Audi

    if message.text == "Audi logo":
        photo = open('Pictures/AUDI-logo.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        mess = 'Audi logo'
        bot.send_message(message.chat.id, mess, parse_mode='html')

    if message.text == "Audi photo":
        photo = open('Pictures/AUDI-car.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        mess = 'Audi photo'
        bot.send_message(message.chat.id, mess, parse_mode='html')

    if message.text == "Audi sound":
        exhaust_sound = open('Audio files/Audi.mp3', 'rb')
        bot.send_voice(message.chat.id, exhaust_sound)
        mess = 'random exhaust sound'
        bot.send_message(message.chat.id, mess, parse_mode='html')

    if message.text == "Audi website":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Enter website",url="https://www.audi.com/en.html"))
        bot.send_message(message.chat.id, 'Enter the website', reply_markup=markup)

    if message.text == "Audi models":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Enter website",url="https://www.auto-data.net/en/audi-brand-41"))
        bot.send_message(message.chat.id, 'Enter the website to see models', reply_markup=markup)


    # porsche

    if message.text == "Porsche logo":
        photo = open('Pictures/PORSCHE-logo.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        mess = 'Porsche logo'
        bot.send_message(message.chat.id, mess, parse_mode='html')

    if message.text == "Porsche photo":
        photo = open('Pictures/PORSCHE-car.jpg', 'rb')
        bot.send_photo(message.chat.id, photo)
        mess = 'Porsche photo'
        bot.send_message(message.chat.id, mess, parse_mode='html')

    if message.text == "Porsche sound":
        exhaust_sound = open('Audio files/Porsche.mp3', 'rb')
        bot.send_voice(message.chat.id, exhaust_sound)
        mess = 'random exhaust sound'
        bot.send_message(message.chat.id, mess, parse_mode='html')

    if message.text == "Porsche website":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Enter website",url="https://www.porsche.com"))
        bot.send_message(message.chat.id, 'Enter the website', reply_markup=markup)

    if message.text == "Porsche models":
        markup = types.InlineKeyboardMarkup()
        markup.add(types.InlineKeyboardButton("Enter website",url="https://www.auto-data.net/en/porsche-brand-64"))
        bot.send_message(message.chat.id, 'Enter the website to see models', reply_markup=markup)

    if message.text == "Enter the website to see models" or 'Enter the website' or 'random exhaust sound' or 'Bmw logo' or 'Bmw photo' or 'Mercedes logo' or 'Mercedes photo' or 'Audi logo' or 'Porsche logo' or 'Audi photo' or 'Porsche photo' :
        pass

    else:
        bot.send_message(message.chat.id, '<b>I dont understand you please use valid commandsor type /help to see how to do that :) </b>', parse_mode='html')



bot.polling(none_stop=True)
