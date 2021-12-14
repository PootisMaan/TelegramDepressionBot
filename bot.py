# Main bot file. Start with it.
# GitHub: https://github.com/PootisMaan/TelegramDepressionBot

import telebot
from markups import Markups
from source import CalculationSystem

result = CalculationSystem()

bot = telebot.TeleBot("1991005309:AAEEhZDkMthxz6WntlUN0XA1ClpguWb9t7k")

# Rewriting this question to one markup may be useful af.
questions = ["Я нервничаю по поводу того, что раньше меня не беспокоило",
             "Я не получаю удовольствия от еды, у меня плохой аппетит",
             "Несмотря на помощь друзей и членов моей семьи, мне не удается избавиться от чувства тоски",
             "Мне кажется, что я не хуже других",
             "Мне трудно сконцентрироваться на том, чем приходится заниматься",
             "Я чувствую подавленность",
             "Все, что я делаю, требует от меня дополнительных усилий",
             "Я надеюсь на хорошее будущее",
             "Мне кажется, что моя жизнь сложилась неудачно",
             "Я испытываю беспокойство, страхи",
             "У меня плохой ночной сон",
             "Я чувствую себя счастливым человеком",
             "Мне кажется, что я стал меньше говорить",
             "Меня беспокоит чувство одиночества",
             "Окружающие настроены недружелюбно ко мне",
             "Жизнь доставляет мне удовольствие",
             "Я легко могу заплакать",
             "Я испытываю грусть, хандру",
             "Мне кажется, что люди меня не любят",
             "У меня нет сил и желания начинать что-либо делать", ]


# 			Statements
# Getting rid of global var is essential.
def if_statement_markup1(message):
    global result
    if message.text == "Иногда":
        result.add_1()
    if message.text == "Значительную часть времени":
        result.add_2()
    if message.text == "Практически все время":
        result.add_3()


def if_statement_markup2(message):
    global result
    if message.text == "Значительную часть времени":
        result.add_1()
    if message.text == "Иногда":
        result.add_2()
    if message.text == "Очень редко или никогда":
        result.add_3()


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


def get_result(message):
    if_statement_markup1(message)
    bot.send_message(message.chat.id, result.get_result())
    print(result.get_result())


# Add "try again" func.

# ==============================================================================================================
# Main test block. Should be redo ASAP. I think that's stupid. Add some cycles, or something... 
# ==============================================================================================================

@bot.message_handler(commands=['test'])
def test(message):
    result.set_to_zero()
    question_msg = bot.send_message(message.chat.id, questions[0], reply_markup=Markups.markup1())
    bot.register_next_step_handler(question_msg, question1)


def question1(message):
    if_statement_markup1(message)
    question_msg = bot.send_message(message.chat.id, questions[1], reply_markup=Markups.markup1())
    bot.register_next_step_handler(question_msg, question2)


def question2(message):
    if_statement_markup1(message)
    question_msg = bot.send_message(message.chat.id, questions[2], reply_markup=Markups.markup1())
    bot.register_next_step_handler(question_msg, question3)


def question3(message):
    if_statement_markup1(message)
    question_msg = bot.send_message(message.chat.id, questions[3], reply_markup=Markups.markup2())
    bot.register_next_step_handler(question_msg, question4)


def question4(message):
    if_statement_markup2(message)
    question_msg = bot.send_message(message.chat.id, questions[4], reply_markup=Markups.markup1())
    bot.register_next_step_handler(question_msg, question5)


def question5(message):
    if_statement_markup1(message)
    question_msg = bot.send_message(message.chat.id, questions[5], reply_markup=Markups.markup1())
    bot.register_next_step_handler(question_msg, question6)


def question6(message):
    if_statement_markup1(message)
    question_msg = bot.send_message(message.chat.id, questions[6], reply_markup=Markups.markup1())
    bot.register_next_step_handler(question_msg, question7)


def question7(message):
    if_statement_markup1(message)
    question_msg = bot.send_message(message.chat.id, questions[7], reply_markup=Markups.markup2())
    bot.register_next_step_handler(question_msg, question8)


def question8(message):
    if_statement_markup2(message)
    question_msg = bot.send_message(message.chat.id, questions[8], reply_markup=Markups.markup1())
    bot.register_next_step_handler(question_msg, question9)


def question9(message):
    question_msg = bot.send_message(message.chat.id, questions[9], reply_markup=Markups.markup1())
    if_statement_markup1(message)
    bot.register_next_step_handler(question_msg, question10)


def question10(message):
    question_msg = bot.send_message(message.chat.id, questions[10], reply_markup=Markups.markup1())
    if_statement_markup1(message)
    bot.register_next_step_handler(question_msg, question11)


def question11(message):
    question_msg = bot.send_message(message.chat.id, questions[11], reply_markup=Markups.markup2())
    if_statement_markup1(message)
    bot.register_next_step_handler(question_msg, question12)


def question12(message):
    question_msg = bot.send_message(message.chat.id, questions[12], reply_markup=Markups.markup1())
    if_statement_markup2(message)
    bot.register_next_step_handler(question_msg, question13)


def question13(message):
    question_msg = bot.send_message(message.chat.id, questions[13], reply_markup=Markups.markup1())
    if_statement_markup1(message)
    bot.register_next_step_handler(question_msg, question14)


def question14(message):
    question_msg = bot.send_message(message.chat.id, questions[14], reply_markup=Markups.markup1())
    if_statement_markup1(message)
    bot.register_next_step_handler(question_msg, question15)


def question15(message):
    question_msg = bot.send_message(message.chat.id, questions[15], reply_markup=Markups.markup2())
    if_statement_markup1(message)
    bot.register_next_step_handler(question_msg, question16)


def question16(message):
    question_msg = bot.send_message(message.chat.id, questions[16], reply_markup=Markups.markup1())
    if_statement_markup2(message)
    bot.register_next_step_handler(question_msg, question17)


def question17(message):
    question_msg = bot.send_message(message.chat.id, questions[17], reply_markup=Markups.markup1())
    if_statement_markup1(message)
    bot.register_next_step_handler(question_msg, question18)


def question18(message):
    question_msg = bot.send_message(message.chat.id, questions[18], reply_markup=Markups.markup1())
    if_statement_markup1(message)
    bot.register_next_step_handler(question_msg, question19)


def question19(message):
    question_msg = bot.send_message(message.chat.id, questions[19], reply_markup=Markups.markup1())
    if_statement_markup1(message)
    bot.register_next_step_handler(question_msg, get_result)


#
# =======================================================================================================
#                                          End of stupid block.
# =======================================================================================================

bot.polling(none_stop=True)
