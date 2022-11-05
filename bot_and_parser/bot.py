from email import message
from unicodedata import name
import telebot
from telebot import types

#5624965452:AAGrdQGCu8O6AzbiHr7snSuJXi884-EEuHM
bot = telebot.TeleBot("5624965452:AAGrdQGCu8O6AzbiHr7snSuJXi884-EEuHM")

town_list = ['тбилиси', 'кутаиси', 'батуми', 'рустави', 'tbilisi', 'kutaisi', 'batumi', 'rustavi']

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'В каком городе вы ищете жилье?')

one_request_dict = {}

@bot.message_handler(content_types=["text"])
def handle_town(message):
    if message.text.lower() not in town_list:
        bot.send_message(message.from_user.id, "Попробуйте ввести название города, например, Тбилиси")
    else:
        one_request_dict["town"] = message.text
        if one_request_dict["town"] == 'тбилиси' or 'tbilisi':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Глдани")
            btn2 = types.KeyboardButton("Дидубе")
            btn3 = types.KeyboardButton("Ваке")
            btn4 = types.KeyboardButton("Исани")
            btn5 = types.KeyboardButton("Крцанисси")
            btn6 = types.KeyboardButton("Мтацминда")
            btn7 = types.KeyboardButton("Надзаладеви")
            btn8 = types.KeyboardButton("Сабуртало")
            btn9 = types.KeyboardButton("Самгори")
            btn10 = types.KeyboardButton("Чугурети")
            btn11 = types.KeyboardButton("Окрестности Тбилиси")
            markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11)
        if one_request_dict["town"] == 'батуми' or 'batumi':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Аэропорт")
            btn2 = types.KeyboardButton("Агмашенебели")
            btn3 = types.KeyboardButton("Багратиони")
            btn4 = types.KeyboardButton("Бони-Городокский район")
            btn5 = types.KeyboardButton("Поселок Тамар")
            btn6 = types.KeyboardButton("Кахаберийский район")
            btn7 = types.KeyboardButton("Руставельский район")
            btn8 = types.KeyboardButton("Старый Батуми")
            btn9 = types.KeyboardButton("Химшиашвили")
            btn10 = types.KeyboardButton("Джавахишвили Район")
            markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10)
        if one_request_dict["town"] == 'кутаиси' or 'kutaisi':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("Поселок Авангарди")
            btn2 = types.KeyboardButton("Поселок Автокархана")
            btn3 = types.KeyboardButton("Поселок Асатиани")
            btn4 = types.KeyboardButton("Пос. Агмашенебели")
            btn5 = types.KeyboardButton("Балахвани")
            btn6 = types.KeyboardButton("Бжолеби")
            btn7 = types.KeyboardButton("Холм Габашвили")
            btn8 = types.KeyboardButton("Гора Сакуслиа")
            btn9 = types.KeyboardButton("Гуматеси")
            btn10 = types.KeyboardButton("Вакисубани")
            btn11 = types.KeyboardButton("Застава")
            btn12 = types.KeyboardButton("Мепесутубани")
            btn13 = types.KeyboardButton("Мцванеквавила")
            btn14 = types.KeyboardButton("Поселок Никея")
            btn15 = types.KeyboardButton("Ниноцминда")
            btn16 = types.KeyboardButton("Рионгеси")
            btn17 = types.KeyboardButton("Сафичхиа")
            btn18 = types.KeyboardButton("Сагориа")
            btn19 = types.KeyboardButton("Укимериони")
            btn20 = types.KeyboardButton("Кроника")
            btn21 = types.KeyboardButton("Укимериони")
            btn22 = types.KeyboardButton("Кроника")
            markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16, btn17, btn18, btn19, btn20, btn21, btn22)
        bot.send_message(message.from_user.id, "Какой район "+one_request_dict["town"]+" вас интересует?".format(message.from_user), reply_markup=markup)
        bot.register_next_step_handler(message, handle_district)
def handle_district(message):
    one_request_dict["district"] = message.text
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Квартира")
    btn2 = types.KeyboardButton("Комната")
    btn3 = types.KeyboardButton("Дом")
    markup.add(btn1, btn2, btn3)
    bot.send_message(message.chat.id, text="Вы ищете квартиру, комнату или дом?".format(message.from_user), reply_markup=markup)
    bot.register_next_step_handler(message, handle_type_of_house)
def handle_type_of_house(message):
    one_request_dict["type_of_house"] = message.text
    if one_request_dict["type_of_house"] != "Комната":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("1")
        btn2 = types.KeyboardButton("2")
        btn3 = types.KeyboardButton("3")
        btn4 = types.KeyboardButton("4")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, text="Сколько вам нужно комнат?".format(message.from_user), reply_markup=markup)
        bot.register_next_step_handler(message, handle_flat_quolity)
    else:
        one_request_dict["flat_quolity"] = 1
        bot.send_message(message.from_user.id, "Введите минимальный порог цены (в долларах)")
        bot.register_next_step_handler(message, handle_min_prise)       
def handle_flat_quolity(message):
    one_request_dict["flat_quolity"] = int(message.text)
    bot.send_message(message.from_user.id, "Введите минимальный порог цены (в долларах)")
    bot.register_next_step_handler(message, handle_min_prise)
def handle_min_prise(message):
    one_request_dict["min_prise"] = 0
    while one_request_dict["min_prise"] == 0:
        try:
            one_request_dict["min_prise"] = int(message.text)
            bot.send_message(message.from_user.id, "Введите максимальный порог цены (в долларах)")
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
    bot.register_next_step_handler(message, handle_max_prise)
def handle_max_prise(message):
    one_request_dict["max_prise"] = 0
    while one_request_dict["max_prise"] == 0:
        try:
            one_request_dict["max_prise"] = int(message.text)
        except Exception:
            bot.send_message(message.from_user.id, 'Цифрами, пожалуйста');
    if one_request_dict["max_prise"] < one_request_dict["min_prise"]:
        bot.send_message(message.from_user.id, 'Максимальный порог цены меньше минимального, попробуйте еще раз');
        bot.register_next_step_handler(message, handle_min_prise)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Да")
        btn2 = types.KeyboardButton("Нет")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id, text="Показывать объявления только от собственника?".format(message.from_user), reply_markup=markup)
        bot.register_next_step_handler(message, handle_owner)
def handle_owner(message):
    one_request_dict["handle_owner"] = message.text
one_request_dict = {}
bot.infinity_polling()

