import requests
import json
from config import url, headers


class APIException(Exception):
    pass


class Convertor:
    @staticmethod
    def get_price(base, symb, amount):
        symbols_dict = Convertor.get_symbols()

        if base not in symbols_dict.keys():
            raise APIException(f'Валюта {base} не найдена')

        if symb not in symbols_dict.keys():
            raise APIException(f'Валюта {symb} не найдена')

        if base == symb:
            raise APIException(f'Невозможно конвертировать одинаковые валюты {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Не удалось обработать количество {amount}!')

        querystring = {"from": base, "to": symb, "amount": str(amount)}
        response = requests.request("GET", url, headers=headers, params=querystring)
        resp = json.loads(response.content)

        return f"Цена {amount} {base} - {resp['result']} {symb}"

    @staticmethod
    def get_symbols():
        url = "https://fixer-fixer-currency-v1.p.rapidapi.com/symbols"

        headers = {
            'x-rapidapi-host': "fixer-fixer-currency-v1.p.rapidapi.com",
            'x-rapidapi-key': "fcb32d0d47msh7f5167c60ad5b2cp1a44f9jsnc23be5d0f196"
        }

        response = requests.request("GET", url, headers=headers)
        resp = json.loads(response.content)

        return resp['symbols']
