import telebot
from config import TOKEN
from extensions import Convertor, APIException


bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Привет! \U0001F44B\n\
Это бот-валютчик. Он может перевести любое количество одной валюты в другую по актуальному \
курсу.\n\n\
\U0001F7E2 Чтобы сделать это, введи сообщение в формате <Валюта, из которой нужно конвертировать> <Валюта, в которую\
 нужно конвертировать> <Количество первой валюты>. Т.е. два тикера валют и одно число - просто через \
пробел.\n\n\
Тикеры основных валют:\n\U0001F1FA\U0001F1F8 Доллар США - USD\n\U0001F1EA\U0001F1FAЕвро - EUR\n\
\U0001F1EC\U0001F1E7Британский фунт стерлингов - GBP\n\U0001F1E8\U0001F1EDШвейцарский франк - CHF\n\
\U0001F1EF\U0001F1F5Японская йена - JPY\n\
\U0001F1F7\U0001F1FAРоссийский рубль - RUB\n\nЧтобы увидеть полный список тикеров доступных валют, введи \
команду /values\n\nПример запроса:\nUSD EUR 100'
    bot.send_message(message.chat.id, text)


@bot.message_handler(commands=['values', ])
def symbols(message: telebot.types.Message):
    symbols_dict = Convertor.get_symbols()
    text = ''
    for ticker in symbols_dict.keys():
        text += f'{symbols_dict[ticker]} - {ticker}\n'
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text', ])
def convert(message: telebot.types.Message):
    values = message.text.upper().split(' ')

    try:
        if len(values) != 3:
            raise APIException('Неверное количество параметров в запросе!')
        answer = Convertor.get_price(*values)
    except APIException as e:
        bot.reply_to(message, f'Ошибка в запросе:\n{e}')
    except Exception as e:
        traceback.print_tb(e.__traceback__)
        bot.reply_to(message, f"Неизвестная ошибка:\n{e}")
    else:
        bot.reply_to(message, answer)


bot.polling(none_stop=True)
