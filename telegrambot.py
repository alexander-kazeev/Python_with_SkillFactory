import telebot
from config import TOKEN, currencies
from extensions import APIException, Converter

bot = telebot.TeleBot(TOKEN)


# Обработка команд /start и /help - вывод приветственного сообщения
@bot.message_handler(commands=['start', 'help'])
def start_help(message: telebot.types.Message):
    text = ('Для перевода количества валюты1 в валюту2 введите запрос в следующем формате:\n'
            'валюта1 валюта2 количество\n'
            'Список доступных валют: /values')
    bot.send_message(message.chat.id, text)


# Обработка команды /values - вывод списка доступных валют
@bot.message_handler(commands=['values'])
def values(message: telebot.types.Message):
    text = 'Доступные валюты:\n' + '\n'.join(currencies.keys())
    bot.send_message(message.chat.id, text)


# Обработка введенного пользователем запроса на конвертацию
@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):
    try:
        # Разбиваем введеное пользователем на элементы списка в нижнем регистре
        inputs = list(map(str.lower, message.text.split()))

        # Проверяем количество введенных параметров
        if len(inputs) != 3:
            raise APIException(f"Количество параметров должно быть 3. Введено: {len(inputs)}")

        # Присваиваем значения переменным, указанным в задании, и конвертируем
        base, quote, amount = inputs
        result = Converter.get_price(base, quote, amount)
    except APIException as e:
        bot.send_message(message.chat.id, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.send_message(message.chat.id, f'Ошибка программы\n{e}')
    else:
        bot.send_message(message.chat.id, f'{amount} {base} перевести в {quote} = {result} {currencies[quote]}')


# Запуск бота
bot.polling(none_stop=True, interval=0)
