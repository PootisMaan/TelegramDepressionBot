# Main bot file. Start with it.
# GitHub: https://github.com/dborodin836/TelegramDepressionBot

import logging
import random
from time import sleep

import telebot

from source import CalculationSystem
import Markups
from models import *

result = CalculationSystem()

bot = telebot.TeleBot("1991005309:AAEEhZDkMthxz6WntlUN0XA1ClpguWb9t7k")

questions = ["Я нервничаю по поводу того, что раньше меня не беспокоило",
             "Я не получаю удовольствия от еды, у меня плохой аппетит",
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
             "Несмотря на помощь друзей и членов моей семьи, мне не удается избавиться от чувства тоски",
             ]


def evaluate(message):
    global result
    if message.text == "Иногда":
        result.add(1)
    elif message.text == "Значительную часть времени":
        result.add(2)
    elif message.text == "Практически все время":
        result.add(3)
    elif message.text == "Очень редко или никогда":
        result.add(0)
    else:
        get_question(-1)


def question_counter():
    current = 0

    def inner(num):
        nonlocal current

        if num == 1:
            current += 1

        if num == -1 and current != 0:
            current -= 1

        # If current question no. exceeds amount of questions
        if current == 20:
            current = 0

        return current

    return inner


get_question = question_counter()


# ========================   MAIN LOGIC   ==============================================================================
# Sends first message/start command
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"<b>Привет,  {message.from_user.first_name}!</b>", parse_mode='html')
    bot.send_message(message.chat.id, "Желаете начать тест?", reply_markup=Markups.start_markup)


# Routes all the incoming text
@bot.message_handler(content_types=['text'])
def router(message):
    if message.text in ['Начать снова', 'Начать тест']:
        send_rules(message)
        test(message)
    elif message.text in ['Информация']:
        info(message)
    elif message.text in ['Об авторе бота']:
        author(message)
    elif message.text in ['qwerty']:
        save_result_db(message, 'test')
    elif message.text in ['Посмотреть историю']:
        user_history = get_history(message)
        mes = parse_history(message, user_history)
        send_history_user(message, mes)


# Starts the test
def test(message):
    evaluate(message)
    next_question = questions[get_question(1)]
    question_msg = bot.send_message(message.chat.id, next_question, reply_markup=Markups.answers_mark)
    if next_question == questions[-1]:
        bot.register_next_step_handler(question_msg, get_result_and_again)
    else:
        bot.register_next_step_handler(question_msg, test)


# Gives the result to user and saves it to db
def get_result_and_again(message):
    if message.text not in ["Очень редко или никогда", "Практически все время", "Значительную часть времени", "Иногда"]:
        err_message = bot.send_message(message.chat.id, questions[-1])
        bot.register_next_step_handler(err_message, test)
    else:
        evaluate(message)
        res = result.get_result()
        logging.info(res)
        bot.send_message(message.chat.id, res)
        bot.send_message(message.chat.id, f"Желаете попробовать снова?", parse_mode='html',
                         reply_markup=Markups.start_markup)
        random.shuffle(questions)
        # save_result_ask(message)
        save_result_db(message, res)


# Sends general info about the test
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


def send_rules(message):
    bot.send_message(message.chat.id, f"Ниже будут приведены вопросы, касающиеся Вашего самочувствия, активности, "
                                      f"эмоционального состояния в течение последнего месяца.")
    sleep(1)
    bot.send_message(message.chat.id, f"Выберите ответ, который наилучшим образом соответствует Вашему сегодняшнему "
                                      f"состоянию.")
    sleep(1)


# Shows the information about author
def author(message):
    bot.send_message(message.chat.id, f"Привет!, это мой первый опыт написания Telegram бота код код можете "
                                      "посмотреть в Github: https://github.com/dborodin836/TelegramDepressionBot",
                     reply_markup=Markups.start_markup_cl)


def save_result_db(message, string: str):
    try:
        Test.create(user_id=message.from_user.id, result=string)
        logging.info(f"{message.from_user.first_name} is {result}")
    except:
        logging.critical("Error while committing to db")


def get_history(message):
    query = Test.select().where(Test.user_id == message.from_user.id).order_by(Test.date.desc())
    selected_results = query.dicts().execute()
    return selected_results


def parse_history(message, selected_results):
    results = []
    for element in selected_results:
        results.append(element)
    return generate_message(results)


# Gonna use it later or not
def save_result_ask(message):
    bot.send_message(message.chat.id, "Хотите сохранить результат для последующего просмотра?",
                     reply_markup=Markups.save_result_markup)


def generate_message(list_message: list) -> str:
    mes = ""
    for dictionary in list_message:
        mes += f"➔ Результат: {dictionary['result']}\n  Дата: {dictionary['date']}\n"
    return mes


def send_history_user(message, mes):
    bot.send_message(message.chat.id, mes)


while True:
    try:
        bot.polling(none_stop=True, timeout=130)
    except:
        bot.stop_polling()
        logging.critical("DEAD")
        bot.polling(none_stop=True)
