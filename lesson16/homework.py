#     Створіть клас, який реалізує підключення до API НБУ ( документація тут https://bank.gov.ua/ua/open-data/api-dev ). Обʼєкт класу повинен вміти отримувати курс валют станом на певну дату. Обʼєкт класу повинен вміти записати курси  в текстовий файл. Назва файлу повинна містити дату на яку шукаємо курс, наприклад:
#
#  21_11_2019.txt
#
# Дані в файл запишіть у вигляді списку :
#
# 1. [назва валюти 1] to UAH: [значення курсу до валюти 1]
# 2. [назва валюти 2] to UAH: [значення курсу до валюти 2]
# 3. [назва валюти 3] to UAH: [значення курсу до валюти 3]
# ...
# n. [назва валюти n] to UAH: [значення курсу до валюти n]
#
#
# P.S. Архітектура класу - на розсуд розробника. Не забувайте про DRY, KISS, YAGNI, SRP та перевірки!)


import requests

class CurrencyForDate:

    @staticmethod
    def request_currency(date):
        """

        Args:
            date: str of time in format ddmmyyyy

        results in a file with currency rates for UAH and date, received in 'date' argument.

        """
        nbu_api_url = f'https://bank.gov.ua/NBU_Exchange/exchange?date={date}&json'
        response = requests.get(nbu_api_url)
        response_json = response.json()
        file = open(f'{date}.txt', 'w')
        for i in response_json:
            currency = i.get('CurrencyCodeL')
            amount = i.get('Amount')
            file.write(f'{currency} to UAH: {amount} \n')


a = CurrencyForDate()
a.request_currency('20022022')