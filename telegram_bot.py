import os
import telebot
import pandas as pd
from sheet_values import *

TOKEN = None

with open("token.txt") as f:
    TOKEN = f.read().strip()

bot = telebot.TeleBot(TOKEN)
costs = []


@bot.message_handler(commands=['start'])
def start(message):
    text = '''Здравствуйте. Я бот, который считает ER учитывая важность разных типов взаимодействий: лайков, комментариев, репостов.
    
Новый показатель мой создатель назвал индекс эффективного вовлечения или Effective Engagement Index (EEI). Знать его полезно, чтобы понимать, насколько качественно вовлечена аудиториия во взаимодействие с контентом.

Напишите «Поехали» и я начну считать.'''
    bot.send_message(message.chat.id, text, parse_mode='html')


@bot.message_handler(content_types=['text'])
def costs_request(message):
    if message.text.lower() == 'поехали':
        msg = bot.send_message(message.chat.id, '''Оцените важность лайков, комментариев и репостов от 1 до 10.

Передайте оценки, отделяя их пробелами. Например: 4 6 9''')
        bot.register_next_step_handler(msg, costs_fixation)
    else:
        text = 'На это я ничего не отвечу — потому что такой команды не знаю.'
        bot.send_message(message.chat.id, text, parse_mode='html')


def costs_fixation(message):
    global costs
    costs = message.text.split(' ')

    msg = f'<b>Принято. Фиксирую.</b>\n\nВажность лайков: {costs[0]}\nВажность комментариев: {costs[1]}\nВажность репостов: {costs[2]}'

    bot.send_message(message.chat.id, msg, parse_mode='html')
    bot.send_message(message.chat.id, '''Последний шаг: пришлите выгрузку в виде Excel-таблицы из LiveDune.

Чтобы её скачать, зайдите в любой аккаунт в LiveDune и нажмите на иконку скачивания в левом верхнем углу.''')


@bot.message_handler(content_types=['document'])
def doc_receipt(message):
    try:
        chat_id = message.chat.id

        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        # Specify the path to save the file. For the health of the code, we cannot delete the semicolon.
        src = 'E:/Python/smm-analys/files/' + message.document.file_name;
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)

        # Reading the received table.
        df = pd.read_excel(src)

        # Output of the current number of subscribers from the received table.
        subscribers = subscribers_count()
        correct_output_subscribers = '{:,}'.format(subscribers).replace(',', ' ')

        # Calculation of average values for key metrics.
        means = means_list()

        # Calculation Effective Engagement Index (EEI).
        metric_results = []
        for i in range(len(means)):
            metric_results.append(float(costs[i]) * float(means[i]))

        effective_engagement_index = (sum(metric_results) / float(subscribers)) * 100
        effective_engagement_index = round(effective_engagement_index, 2)

        # Sending a response to the user.
        final_answer = f'''Всё получилось!
        
Значения из вашей таблицы:
&#129492; Самое свежее число подписчиков — {correct_output_subscribers}
&#10084; Среднее число лайков — {means[0]}
&#128173; Среднее число комментариев — {means[1]}
&#128266; Среднее число репостов — {means[2]}

<b>Индекс эффективного вовлечения (EEI): {effective_engagement_index}%</b>'''

        bot.send_message(message.chat.id, final_answer, parse_mode='html')

    except Exception as e:
        bot.reply_to(message, e)


bot.polling(none_stop=True)
