from telebot import types

# Markup for the question (answers)
answers_mark = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn1 = types.KeyboardButton('Очень редко или никогда')
btn2 = types.KeyboardButton('Иногда')
btn3 = types.KeyboardButton('Значительную часть времени')
btn4 = types.KeyboardButton('Практически все время')
answers_mark.add(btn1, btn2, btn3, btn4)

# Start markup
start_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_start = types.KeyboardButton('Начать тест')
btn_info = types.KeyboardButton('Информация')
btn_history = types.KeyboardButton('Посмотреть историю')
start_markup.add(btn_start, btn_info, btn_history)

# Save result markup
save_result_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_yes = types.KeyboardButton('Сохранить резутьтат в базу')
btn_no = types.KeyboardButton('Не сохранять результат в базу')
save_result_markup.add(btn_yes, btn_no)

# Clear start markup
start_markup_cl = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_start = types.KeyboardButton('Начать тест')
btn_history = types.KeyboardButton('Посмотреть историю')
start_markup_cl.add(btn_start, btn_history)

# Info markup
info_markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
btn_back = types.KeyboardButton('Начать тест')
btn_info = types.KeyboardButton('Об авторе бота')
btn_history = types.KeyboardButton('Посмотреть историю')
info_markup.add(btn_back, btn_info, btn_history)
