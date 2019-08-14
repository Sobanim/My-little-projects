## -*- coding: utf-8 -*-
import telebot
import random
from telebot import types

bot = telebot.TeleBot("747435985:AAHYHek-cxvsaJADsgCGUCVB4Zy_LFKQwak")

lang = ''

answers_posit = ["Абсолютно!", "Уже всё и так известно, что да", "Определённо да", "Никаких сомнений, ДА, Maza Faka!", "Можешь быть уверен в этом"]
answers_hesitantly_posit = ["Мне кажется — «да»", "Вероятнее всего", "Вполне возможно", "Знаки говорят — «да», а гороскоп что «Нет»", "Да я вообще хз"]
answers_neutral = ["Пока не понятно, попробуй снова", "Спроси позже, связь со Вселенной потеряна", "Лучше не стоит пробовать", "Сейчас нельзя предсказать, Юпитер в созвездии Девы", "Сконцентрируйся, пукни и спроси опять"]
answers_negative = ["Даже не думай", "Мой ответ — «нет»", "По моим данным — «нет»", "Перспектив вообще нету", "Вообще не знаю. Скорее нет чем да"]
answers = [answers_posit, answers_hesitantly_posit, answers_neutral, answers_negative]

@bot.message_handler(commands=['start'])
def start_lang(message):
    keyboard = types.InlineKeyboardMarkup()
    key_eng = types.InlineKeyboardButton(text='ENG', callback_data='eng')
    keyboard.add(key_eng)
    key_rus = types.InlineKeyboardButton(text='RUS', callback_data='rus')
    keyboard.add(key_rus)
    key_ukr = types.InlineKeyboardButton(text='UKR', callback_data='ukr')
    keyboard.add(key_ukr)
       
    bot.send_message(message.from_user.id, text="Please, choose your onw language:", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "eng": #call.data это callback_data, которую мы указали при объявлении кнопки
        #код сохранения данных, или их обработки
        bot.send_message(call.message.chat.id, 'You choose very universal language - English')
    elif call.data == "rus":
        bot.send_message(call.message.chat.id, 'Ты выбрал великий и могучий Русский Язык! Поздравляю тебя, ТОВАРИЩ)')
    elif call.data == "ukr":
        bot.send_message(call.message.chat.id, 'Ти вибрав українську, солов\'їну, співучу мову!!')

# def greeting(message):
#     bot.send_message(message.chat.id, 'Привет ' + str(message.from_user.first_name) + ' ' + str(message.from_user.last_name) + '! Я тренировочный Python бот.\n')
#     bot.send_message(message.chat.id, 'Данный бот поможет Вам с ответом на вопрос \"Да\" или \"Нет\". Напиши свой вопрос')
@bot.message_handler(content_types=['text'])
def question(message):
    if len(message.text) <= 5:
        bot.reply_to(message, "Ваш вопрос слишком короткий. Пожалуйста, напишите более подробнее")
    else:
        reakcion = random.randrange(4)
        answer = random.randrange(4)
        bot.reply_to(message, answers[reakcion][answer])
bot.polling(timeout=30)