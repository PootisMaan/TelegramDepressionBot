# Main bot file. Start with it.
# GitHub: https://github.com/dborodin836/TelegramDepressionBot

import logging
import telebot
from source import CalculationSystem
import Markups

result = CalculationSystem()

bot = telebot.TeleBot("1991005309:AAEEhZDkMthxz6WntlUN0XA1ClpguWb9t7k")

# TODO: Add random guestions
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


def evaluate(message):
    global result
    if message.text == "Иногда":
        result.add(1)
    if message.text == "Значительную часть времени":
        result.add(2)
    if message.text == "Практически все время":
        result.add(3)


def question_counter(num: int = 0):
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


get_question = question_counter()


# ========================   MAIN LOGIC   ==============================================================================
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"<b>Привет,  {message.from_user.first_name}!</b>", parse_mode='html')
    bot.send_message(message.chat.id, f"Ниже будут приведены вопросы, касающиеся Вашего самочувствия, активности, "
                                      f"эмоционального состояния в течение последнего месяца.")
    bot.send_message(message.chat.id, f"Выберите ответ, который наилучшим образом соответствует Вашему сегодняшнему "
                                      f"состоянию.")
    bot.send_message(message.chat.id, "Желаете начать тест?", reply_markup=Markups.start_markup)


@bot.message_handler(content_types=['text'])
def router(message):
    if message.text in ['Начать снова', 'Начать тест']:
        test(message)
    elif message.text in ['Информация']:
        info(message)
    elif message.text in ['Об авторе бота']:
        author(message)


def info(message):
    bot.send_message(message.chat.id, "Методика шкалы-опросника Центра эпидемиологических исследований депрессии "
                                      "CES-D (Center for Epidemiologic Studies Depression Scale) предназначена для "
                                      "скринингового выявления у пациентов депрессивного расстройства. Опросник "
                                      "разработан в США в 1977 г. и на сегодняшний день наиболее часто используемый "
                                      "в мире для проведения эпидемиологических исследований депрессии. Шкала "
                                      "состоит из 20 пунктов, измеряющих депрессивные нарушения, отмечающиеся у "
                                      "обследуемых за последние семь дней. Общий балл по данной шкале от 0 до 60 "
                                      "отражает уровень депрессии.", parse_mode='html',
                     reply_markup=Markups.info_markup)


def author(message):
    bot.send_message(message.chat.id, f"Привет!, это мой первый опыт написания Telegram бота код код можете"
                                      "посмотреть в Github: https://github.com/dborodin836/TelegramDepressionBot",
                     reply_markup=Markups.start_markup_cl)


def get_result_and_again(message):
    evaluate(message)
    bot.send_message(message.chat.id, result.get_result())
    bot.send_message(message.chat.id, f"Желаете попробовать снова?", parse_mode='html',
                     reply_markup=Markups.start_markup)


def test(message):
    evaluate(message)
    next_question = questions[get_question()]
    question_msg = bot.send_message(message.chat.id, next_question, reply_markup=Markups.answers_mark)
    if next_question == questions[-1]:
        bot.register_next_step_handler(question_msg, get_result_and_again)
    else:
        bot.register_next_step_handler(question_msg, test)


try:
    bot.polling(none_stop=True)
except:
    logging.error("DEAD")
    bot.stop_polling()
    bot.polling(none_stop=True)
