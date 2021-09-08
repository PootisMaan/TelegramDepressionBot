from telebot import types
import telebot

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
    