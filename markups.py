from telebot import types


class Markups():

    def markup1():
        markup1 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Очень редко или никогда')
        btn2 = types.KeyboardButton('Иногда')
        btn3 = types.KeyboardButton('Значительную часть времени')
        btn4 = types.KeyboardButton('Практически все время')
        markup1.add(btn1, btn2, btn3, btn4)
        return markup1

    def markup2():
        markup2 = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Практически все время')
        btn2 = types.KeyboardButton('Значительную часть времени')
        btn3 = types.KeyboardButton('Иногда')
        btn4 = types.KeyboardButton('Очень редко или никогда')
        markup2.add(btn1, btn2, btn3, btn4)
        return markup2

    def start_markup():
        start_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn_start = types.KeyboardButton('Начать тест')
        btn_info = types.KeyboardButton('Информация')
        start_markup.add(btn_start, btn_info)
        return start_markup

    def info_markup():
        info_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn_back = types.KeyboardButton('Назад')
        btn_info = types.KeyboardButton('Something')
        info_markup.add(btn_back, btn_info)
        return info_markup
