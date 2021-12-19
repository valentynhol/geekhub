"""
2. Написати скрипт, який буде приймати від користувача назву валюти і початкову дату.
   - Перелік валют краще принтануть.
   - Також не забудьте указати, в якому форматі коритувач повинен ввести дату.
   - Додайте перевірку, чи введена дата не знаходиться у майбутньому ;)
   - Також перевірте, чи введена правильна валюта.
   Виконуючи запроси до API архіву курсу валют Приватбанку, вивести інформацію про зміну
   курсу обраної валюти (Нацбанк) від введеної дати до поточної. Приблизний вивід наступний:
   Currency: USD
   Date: 12.12.2021
   NBU:  27.1013   -------
   Date: 13.12.2021
   NBU:  27.0241   -0,0772
   Date: 14.12.2021
   NBU:  26.8846   -0,1395
"""

from time import sleep
import datetime
import requests


def change_watcher():
    start_date_input = tuple(map(int, input('Введіть початкову дату у форматі DD-MM-YYYY: ').split('-')))

    start_date = datetime.date(day=start_date_input[0], month=start_date_input[1], year=start_date_input[2])
    stop_date = datetime.date.today()
    days = (stop_date - start_date).days

    if not len(start_date_input) == 3 or start_date > stop_date:
        print('Введіть дійсну дату!')
        exit()

    print('\nAZN BYN CAD CHF CNY CZK DKK EUR GBP GEL HUF ILS JPY KZT MDL NOK PLN RUB SEK SGD TMT TRY UAH USD UZS')
    currency = input('Виберіть валюту з списку вище: ')

    if days <= 365*4 and currency in ['AZN', 'BYN', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'GEL', 'HUF',
                                      'ILS', 'JPY', 'KZT', 'MDL', 'NOK', 'PLN', 'RUB', 'SEK', 'SGD', 'TMT', 'TRY',
                                      'UAH', 'USD', 'UZS']:

        print('\n\nCurrency: ', currency)

        for day_counter in range(days + 1):
            date = start_date + datetime.timedelta(days=day_counter)
            if date <= stop_date:
                exchange_rate = requests.get('https://api.privatbank.ua/p24api/exchange_rates?json&date='
                                             f'{date.day}.{date.month}.{date.year}').json()
                for exchange_currency in exchange_rate['exchangeRate']:
                    try:
                        if exchange_currency['currency'] == currency:
                            if day_counter == 0:
                                print('\nDate: ', date)
                                print('NBU: ', round(exchange_currency['saleRateNB'], 4), '--------')
                                prev_exchange_rate = exchange_currency['saleRateNB']
                            else:
                                print('\nDate: ', date)
                                print('NBU: ', round(exchange_currency['saleRateNB'], 4),
                                      round(exchange_currency['saleRateNB'] - prev_exchange_rate, 4))
                                prev_exchange_rate = exchange_currency['saleRateNB']
                    except KeyError:
                        pass
                sleep(0.5)
    else:
        if currency not in ['AZN', 'BYN', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'GEL', 'HUF',
                            'ILS', 'JPY', 'KZT', 'MDL', 'NOK', 'PLN', 'RUB', 'SEK', 'SGD', 'TMT', 'TRY',
                            'UAH', 'USD', 'UZS']:
            print('Немає такої валюти!')
        else:
            print('Введіть дату не далі ніж 4 роки назад!')


change_watcher()
