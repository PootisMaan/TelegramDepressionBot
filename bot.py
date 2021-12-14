# Main bot file. Start with it.
# GitHub: https://github.com/PootisMaan/TelegramDepressionBot

import telebot
from markups import Markups
from source import CalculationSystem

result = CalculationSystem()

bot = telebot.TeleBot("1991005309:AAEEhZDkMthxz6WntlUN0XA1ClpguWb9t7k")

questions = ["Я нервничаю по поводу того, что раньше меня не беспокоило",
             "Я не получаю удовольствия от еды, у меня плохой аппетит",
             "Несмотря на помощь друзей и членов моей семьи, мне не удается избавиться от чувства тоски",
             "Мне кажется, что я хуже других",
             "Мне трудно сконцентрироваться на том, чем приходится заниматься",
             "Я чувствую подавленность",
             "Все, что я делаю, требует от меня дополнительных усилий",
             "Я не надеюсь на хорошее будущее",
             "Мне кажется, что моя жизнь сложилась неудачно",
             "Я испытываю беспокойство, страхи",
             "У меня плохой ночной сон",
             "Я чувствую себя несчастливым человеком",
             "Мне кажется, что я стал меньше говорить",
             "Меня беспокоит чувство одиночества",
             "Окружающие настроены недружелюбно ко мне",
             "Жизнь не доставляет мне удовольствие",
             "Я легко могу заплакать",
             "Я испытываю грусть, хандру",
             "Мне кажется, что люди меня не любят",
             "У меня нет сил и желания начинать что-либо делать", ]


def if_statement(message):
    global result
    if message.text == "Иногда":
        result.add_1()
    if message.text == "Значительную часть времени":
        result.add_2()
    if message.text == "Практически все время":
        result.add_3()


def question(num: int = 0):
    current = 0

    def inner():
        nonlocal current
        if current == 20:
            current = 0
        if num != -1:
            current += 1
            return current - 1
        else:
            current = 0

    return inner


get_question = question()


# ========================   MAIN LOGIC   =============================================================================
@bot.message_handler(commands=['start'])
def send_welcome(message):
    message = bot.send_message(message.chat.id, f"<b>Привет {message.from_user.first_name}!</b>", parse_mode='html',
                               reply_markup=Markups.start_markup())
    message = bot.send_message(message.chat.id, "Желаете начать тест?")
    bot.register_next_step_handler(message, test)


@bot.message_handler(commands=['info'])
def info(message):
    message = bot.send_message(message.chat.id, f"<b>Some info!</b>", parse_mode='html',
                               reply_markup=Markups.info_markup())
    bot.register_next_step_handler(message, send_welcome)


def get_result_and_try_again(message):
    if_statement(message)
    bot.send_message(message.chat.id, result.get_result())
    try_markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn_try_again = telebot.types.KeyboardButton('Начать снова')
    try_markup.add(btn_try_again)
    message = bot.send_message(message.chat.id, f"Жедаете попробовать снова?", parse_mode='html',
                               reply_markup=try_markup)
    bot.register_next_step_handler(message, send_welcome)


@bot.message_handler(commands=['test'])
def test(message):
    if_statement(message)
    next_question = questions[get_question()]
    question_msg = bot.send_message(message.chat.id, next_question, reply_markup=Markups.markup1())
    if next_question == 'У меня нет сил и желания начинать что-либо делать':
        bot.register_next_step_handler(question_msg, get_result_and_try_again)
    else:
        bot.register_next_step_handler(question_msg, test)


bot.polling(none_stop=True)
