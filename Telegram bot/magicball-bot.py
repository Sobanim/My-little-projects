import telebot
import random

bot = telebot.TeleBot("747435985:AAHYHek-cxvsaJADsgCGUCVB4Zy_LFKQwak")

answers_posit = ["Абсолютно!", "Уже всё и так известно, что да", "Определённо да", "Никаких сомнений, ДА, Maza Faka!", "Можешь быть уверен в этом"]
answers_hesitantly_posit = ["Мне кажется — «да»", "Вероятнее всего", "Вполне возможно, а волне и невозможно", "Знаки говорят — «да», а гороскоп что «Нет»", "Да я вообще хз"]
answers_neutral = ["Пока не понятно, попробуй снова", "Спроси позже, связь со Вселенной потеряна", "Лучше не стоит пробовать", "Сейчас нельзя предсказать, Юпитер в созвездии Девы", "Сконцентрируйся, пукни и спроси опять"]
answers_negative = ["Даже не думай", "Мой ответ — «нет»", "По моим данным — «нет»", "Перспектив вообще нету", "Вообще не знаю. Скорее нет чем да"]
answers = [answers_posit, answers_hesitantly_posit, answers_neutral, answers_negative]

@bot.message_handler(commands=['start'])
def greeting(message):
    bot.send_message(message.chat.id, 'Привет ' + str(message.from_user.first_name) + ' ' + str(message.from_user.last_name) + '! Я тренировочный Python бот.\n')
    bot.send_message(message.chat.id, 'Данный бот поможет Вам с ответом на вопрос \"Да\" или \"Нет\". Напиши свой вопрос')
@bot.message_handler(content_types=['text'])
def question(message):
    if len(message.text) <= 5:
        bot.reply_to(message, "Ваш вопрос слишком короткий. Пожалуйста, напишите более подробнее")
    else:
        reakcion = random.randrange(4)
        answer = random.randrange(4)
        bot.reply_to(message, answers[reakcion][answer])


bot.polling()