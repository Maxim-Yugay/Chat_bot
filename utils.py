import json
import requests
from config import keys


class ConversionExcepton(Exception):
    pass

class Convecter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConversionExcepton (f'Невозможно перевести одинаковые валюты {base}.')
        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConversionExcepton (f'Не удалось обработать валюту {quote}')
        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConversionExcepton (f'Не удалось обработать валюту {base}.')
        try:
            amount = float(amount)
        except ValueError:
            raise ConversionExcepton (f'Не удалось обработать колличество {amount}')

        r = requests.get(f'https://v6.exchangerate-api.com/v6/c34d530a379b4af0f8d20a86/pair/{quote_ticker}/{base_ticker}')
        resp = json.loads(r.content)
        total_base = resp['conversion_rate']*float(amount)
        message = f'Цена {amount} {quote_ticker} в {base_ticker} : {total_base}'

        return message

