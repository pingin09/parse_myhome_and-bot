from email import message
from unicodedata import name
import telebot
from telebot import types
from params import Data
from parse import MyhomeParser
from token_tbot import id as id_token

bot = telebot.TeleBot(id_token)

town_list = ['тбилиси', 'кутаиси', 'батуми', 'рустави', 'мцхета', 'боржоми', 'кобулети']
tbilisi_district_list = ["глдани", "дидубе", "ваке", "исани", "крцанисси", "мтанцминда", "надзаладеви", "сабуртало",
                         "самгори", "чугурети", "окрестности тбилиси"]
batumi_disrtict_list = ["аэропорт", "агмашенебели", "багратиони", "бони-городокский район", "поселок тамар",
                        "кахаберийский район", "руставельский район", "старый батуми", "химшиашвили",
                        "джавахишвили район"]
kutaisi_district_list = ["поселок автокархана", "поселок асатиани", "пос. агмашенебели", "балахвани", "бжолеби",
                         "холм габашвили", "гора сакуслиа", "гуматеси", "вакисубани", "застава", "мепесутубани",
                         "мцванеквавила", "поселок никея", "ниноцминда", "рионгеси", "сафичхиа", "сагориа",
                         "укимериони", "кроника",
                         "поселок чавчавадзе", "чома"]
type_house_list = ["Комната", "Дом", "Квартира"]
flat_quolity_list = ["1", "2", "3", "4"]
owner_list = ["Да", "Нет"]


# @bot.message_handler(commands=["start"])
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    btn1 = types.KeyboardButton("Тбилиси")
    btn2 = types.KeyboardButton("Кутаиси")
    btn3 = types.KeyboardButton("Батуми")
    btn4 = types.KeyboardButton("Рустави")
    btn5 = types.KeyboardButton("Мцхета")
    btn6 = types.KeyboardButton("Боржоми")
    btn7 = types.KeyboardButton("Кобулети")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
    bot.send_message(message.from_user.id, "В каком городе вы ищете жилье?".format(message.from_user),
                     reply_markup=markup)
    bot.register_next_step_handler(message, handle_town)


def handle_town(message):
    if message.text.lower() not in town_list:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        btn1 = types.KeyboardButton("Тбилиси")
        btn2 = types.KeyboardButton("Кутаиси")
        btn3 = types.KeyboardButton("Батуми")
        btn4 = types.KeyboardButton("Рустави")
        btn5 = types.KeyboardButton("Мцхета")
        btn6 = types.KeyboardButton("Боржоми")
        btn7 = types.KeyboardButton("Кобулети")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        bot.send_message(message.from_user.id, "Выберите один из предложенных вариантов".format(message.from_user),
                         reply_markup=markup)
        bot.register_next_step_handler(message, handle_town)
    else:
        one_request_dict["town"] = message.text
        if one_request_dict["town"] in ['Мцхета', 'Боржоми', 'Кобулети']:
            one_request_dict["district"] = 0
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            btn1 = types.KeyboardButton("Квартира")
            btn2 = types.KeyboardButton("Комната")
            btn3 = types.KeyboardButton("Дом")
            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id, text="Вы ищете квартиру, комнату или дом?".format(message.from_user),
                             reply_markup=markup)
            bot.register_next_step_handler(message, handle_type_of_house)
        if one_request_dict["town"] == 'Тбилиси':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
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
            bot.send_message(message.from_user.id,
                             "Какой район " + one_request_dict["town"] + " вас интересует?".format(message.from_user),
                             reply_markup=markup)
            bot.register_next_step_handler(message, handle_district)
        if one_request_dict["town"] == 'Батуми':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
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
            bot.send_message(message.from_user.id,
                             "Какой район " + one_request_dict["town"] + " вас интересует?".format(message.from_user),
                             reply_markup=markup)
            bot.register_next_step_handler(message, handle_district)
        if one_request_dict["town"] == 'Кутаиси':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
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
            btn21 = types.KeyboardButton("Поселок Чавчавадзе")
            btn22 = types.KeyboardButton("Чома")
            markup.add(btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16,
                       btn17, btn18, btn19, btn20, btn21, btn22)
            bot.send_message(message.from_user.id,
                             "Какой район " + one_request_dict["town"] + " вас интересует?".format(message.from_user),
                             reply_markup=markup)
            bot.register_next_step_handler(message, handle_district)


def handle_district(message):
    if message.text.lower() not in tbilisi_district_list and one_request_dict["town"] == 'Тбилиси':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
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
        bot.send_message(message.from_user.id,
                         "Выберите из предложенных вариантов".format(message.from_user),
                         reply_markup=markup)
        bot.register_next_step_handler(message, handle_district)
    elif message.text.lower() not in batumi_disrtict_list and one_request_dict["town"] == 'Батуми':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
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
        bot.send_message(message.from_user.id,
                         "Выберите из предложенных вариантов".format(message.from_user),
                         reply_markup=markup)
        bot.register_next_step_handler(message, handle_district)
    elif message.text.lower() not in kutaisi_district_list and one_request_dict["town"] == 'Кутаиси':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
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
        btn21 = types.KeyboardButton("Поселок Чавчавадзе")
        btn22 = types.KeyboardButton("Чома")
        markup.add(btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9, btn10, btn11, btn12, btn13, btn14, btn15, btn16,
                   btn17, btn18, btn19, btn20, btn21, btn22)
        bot.send_message(message.from_user.id,
                         "Выберите из предложенных вариантов".format(message.from_user),
                         reply_markup=markup)
        bot.register_next_step_handler(message, handle_district)
    else:
        one_request_dict["district"] = message.text
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        btn1 = types.KeyboardButton("Квартира")
        btn2 = types.KeyboardButton("Комната")
        btn3 = types.KeyboardButton("Дом")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Вы ищете квартиру, комнату или дом?".format(message.from_user),
                         reply_markup=markup)
        bot.register_next_step_handler(message, handle_type_of_house)


def handle_type_of_house(message):
    if message.text not in type_house_list:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        btn1 = types.KeyboardButton("Квартира")
        btn2 = types.KeyboardButton("Комната")
        btn3 = types.KeyboardButton("Дом")
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id, text="Выберите из предложенных вариантов".format(message.from_user),
                         reply_markup=markup)
        bot.register_next_step_handler(message, handle_type_of_house)

    else:
        one_request_dict["type_of_house"] = message.text
        if one_request_dict["type_of_house"] != "Комната":
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            btn1 = types.KeyboardButton("1")
            btn2 = types.KeyboardButton("2")
            btn3 = types.KeyboardButton("3")
            btn4 = types.KeyboardButton("4")
            markup.add(btn1, btn2, btn3, btn4)
            bot.send_message(message.chat.id, text="Сколько вам нужно комнат?".format(message.from_user),
                             reply_markup=markup)
            bot.register_next_step_handler(message, handle_flat_quolity)
        else:
            one_request_dict["flat_quolity"] = 1
            bot.send_message(message.from_user.id, "Введите минимальный порог цены (в долларах)")
            bot.register_next_step_handler(message, handle_min_prise)


def handle_flat_quolity(message):
    if message.text not in flat_quolity_list:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        btn1 = types.KeyboardButton("1")
        btn2 = types.KeyboardButton("2")
        btn3 = types.KeyboardButton("3")
        btn4 = types.KeyboardButton("4")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id, text="Выберите из предложенных вариантов".format(message.from_user),
                         reply_markup=markup)
        bot.register_next_step_handler(message, handle_flat_quolity)
    else:
        one_request_dict["flat_quolity"] = int(message.text)
        bot.send_message(message.from_user.id, "Введите минимальный порог цены (в долларах)")
        bot.register_next_step_handler(message, handle_min_prise)


def handle_min_prise(message):
    one_request_dict["min_prise"] = 0
    if message.text.isdigit():
        one_request_dict["min_prise"] = int(message.text)
        bot.send_message(message.from_user.id, "Введите максимальный порог цены (в долларах)")
        bot.register_next_step_handler(message, handle_max_prise)
    else:
        bot.send_message(message.from_user.id, "Цифрами, пожалуйста. Попробуйте еще раз")
        bot.register_next_step_handler(message, handle_min_prise)


def handle_max_prise(message):
    one_request_dict["max_prise"] = 0
    if message.text.isdigit():
        one_request_dict["max_prise"] = int(message.text)
        if one_request_dict["max_prise"] < one_request_dict["min_prise"]:
            bot.send_message(message.from_user.id, 'Максимальный порог цены меньше минимального, попробуйте еще раз');
            bot.send_message(message.from_user.id, 'Введите минимальный порог цены (в долларах)');
            bot.register_next_step_handler(message, handle_min_prise)
        else:
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
            btn1 = types.KeyboardButton("Да")
            btn2 = types.KeyboardButton("Нет")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id,
                             text="Показывать объявления только от собственника?".format(message.from_user),
                             reply_markup=markup)
            bot.register_next_step_handler(message, handle_owner)
    else:
        bot.send_message(message.from_user.id, "Цифрами, пожалуйста. Попробуйте еще раз")
        bot.register_next_step_handler(message, handle_max_prise)


def handle_owner(message):
    if message.text not in owner_list:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        btn1 = types.KeyboardButton("Да")
        btn2 = types.KeyboardButton("Нет")
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id,
                         text="Выберите из предложенных вариантов".format(message.from_user),
                         reply_markup=markup)
        bot.register_next_step_handler(message, handle_owner)
    else:
        one_request_dict["handle_owner"] = message.text
        one_request_dict['count_page'] = 0
        d = Data(one_request_dict)
        last_forms = d.formats()
        print(message)
        MyParse = MyhomeParser(last_forms)
        result = MyParse.parse_all()
        one_request_dict['result'] = result
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        btn1 = types.KeyboardButton("Показать")
        markup.add(btn1)
        bot.send_message(message.chat.id, text='Показать варианты', reply_markup=markup)
        bot.register_next_step_handler(message, conclusion)


def conclusion(message):
    result = one_request_dict['result']
    if one_request_dict['count_page'] == 0:
        message.text = 'Вперёд'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    if one_request_dict['count_page'] == len(one_request_dict['result']) - 1:
        btn1 = types.KeyboardButton("Назад")
        btn3 = types.KeyboardButton('Новый поиск')
        markup.add(btn1, btn3)
    elif one_request_dict['count_page'] == 0:
        btn2 = types.KeyboardButton("Вперёд")
        btn3 = types.KeyboardButton('Новый поиск')
        markup.add(btn2, btn3)
    else:
        btn1 = types.KeyboardButton("Назад")
        btn3 = types.KeyboardButton('Новый поиск')
        btn2 = types.KeyboardButton("Вперёд")
        markup.add(btn1, btn2, btn3)
    if message.text != 'Новый поиск':
        for block in result[one_request_dict['count_page']]:
            bot.send_photo(message.chat.id, block['images1'],
                           caption=f"{block['title']} | {block['adress']} | {block['priceD']} |"
                                   f" Телефон {block['url']}", reply_markup=markup)
    print(message.text)
    if message.text == 'Назад':
        one_request_dict['count_page'] -= 1
        bot.register_next_step_handler(message, conclusion)
    elif message.text == 'Вперёд':
        one_request_dict['count_page'] += 1
        bot.register_next_step_handler(message, conclusion)
    elif message.text == 'Новый поиск':
        message.text = '/start'


one_request_dict = {}
bot.infinity_polling()

# def output(message):
#     bot.send_photo(message.chat.id, 'https://pbs.twimg.com/media/C5IoAwpWAAAa82G.jpg:large',
#                    caption="Тип жилья | Адрес | Цена | Телефон https://qna.habr.com/q/739457")
