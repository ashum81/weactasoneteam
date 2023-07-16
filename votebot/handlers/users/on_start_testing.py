import json
import random
import time

from aiogram.dispatcher.filters import Command
from aiogram import types

from loader import dp


def get_questions():
    with open('questions.json', encoding='utf-8') as json_file:
        data = json.load(json_file).get("questions")
    return data


questions = get_questions()
TOTAL_QUESTIONS = 5
LIST_OF_QUESTIONS = random.sample(range(len(questions)), TOTAL_QUESTIONS)
NUM = 0
RESULTS = 0
DURATION = time.time()
BALLS = ["🟣", "🟢", "⚪"]


@dp.message_handler(Command('onstarttest'))
async def on_start_test(message: types.Message):
    global NUM, RESULTS, DURATION
    NUM = 0
    RESULTS = 0
    DURATION = time.time()

    num_of_question = LIST_OF_QUESTIONS[NUM]
    question = questions[num_of_question].get("question")
    answers = questions[num_of_question].get("answers")
    correct_answer = questions[num_of_question].get("correct_answer")
    await message.answer_poll(
        question=BALLS[random.randrange(3)]+" "+question,
        options=answers,
        type='quiz',
        correct_option_id=correct_answer,
        is_anonymous=False
    )


@dp.poll_answer_handler()
async def question(message: types.PollAnswer):
    global NUM, RESULTS, DURATION
    if message.user.username == "radioas":
        if NUM < len(LIST_OF_QUESTIONS):
            answer = message.option_ids[0]
            print(f"num {NUM}, list_of_questions {LIST_OF_QUESTIONS}")
            num_of_question = LIST_OF_QUESTIONS[NUM]
            if answer == questions[num_of_question].get("correct_answer"):
                RESULTS += 1
            print(f"num_of_question {num_of_question}, answer {answer}, correct answer {questions[num_of_question].get('correct_answer')}")
            print(f"results: {RESULTS}")
            NUM += 1
            if NUM < len(LIST_OF_QUESTIONS):
                num_of_question = LIST_OF_QUESTIONS[NUM]
                question = questions[num_of_question].get("question")
                answers = questions[num_of_question].get("answers")
                correct_answer = questions[num_of_question].get("correct_answer")
                await dp.bot.send_poll(
                    chat_id=message.user.id,
                    question="🟣 "+question,
                    options=answers,
                    type='quiz',
                    correct_option_id=correct_answer,
                    is_anonymous=False
                )
            else:
                DURATION = round(time.time() - DURATION, 4)
                await dp.bot.send_message(
                    message.user.id,
                    f"Правильных ответов: {RESULTS}\nВремя: {DURATION}"
                )
                print(f"duration {DURATION}")
