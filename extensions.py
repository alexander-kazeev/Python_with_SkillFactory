import requests
import json
from config import currencies


# Класс пользовательских исключений
class APIException(Exception):
    pass


# Класс конвертации
class Converter:
    @staticmethod
    def get_price(base, quote, amount):
        # Проверки на существование валют и корректность суммы
        try:
            base_code = currencies[base]
        except Exception:
            raise APIException(f'Не найдена валюта: {base}\nСписок доступных валют: /values')
        try:
            quote_code = currencies[quote]
        except Exception:
            raise APIException(f'Не найдена валюта: {quote}\nСписок доступных валют: /values')
        try:
            amount = float(amount)
        except Exception:
            raise APIException(f'Некорректное количество: {amount}\nУкажите целое или десятичное число')

        # Если валюты равны, то результат - введенная сумма
        if base == quote:
            return amount

        # Запрос курса валюты и расчет итогового курса
        request = requests.get(f'https://api.exchangeratesapi.io/latest?base={base_code}&symbols={quote_code}')
        result = round(float(json.loads(request.content)['rates'][quote_code]) * amount, 4)

        return result
