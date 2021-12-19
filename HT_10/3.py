"""
3. Конвертер валют. Прийматиме від користувача назву двох валют і суму (для першої).
   Робить запрос до API архіву курсу валют Приватбанку (на поточну дату) і виконує
   конвертацію введеної суми з однієї валюти в іншу.
"""

import datetime
import requests


def converter(currency_input, currency_output, cash):
    date = datetime.date.today().strftime('%d.%m.20%y')
    current_exchange_rate = requests.get(f'https://api.privatbank.ua/p24api/exchange_rates?json&date={date}').json()

    for currency in current_exchange_rate['exchangeRate']:
        try:
            if currency['currency'] == currency_input:
                sale_rate = currency['saleRateNB']
            elif currency['currency'] == currency_output:
                purchase_rate = currency['purchaseRateNB']
        except KeyError:
            pass

    return f'\n\n{round(cash*sale_rate/purchase_rate, 2)} {currency_output}'


print('\nAZN BYN CAD CHF CNY CZK DKK EUR GBP GEL HUF ILS JPY KZT MDL NOK PLN RUB SEK SGD TMT TRY UAH USD UZS')
currency_in = input('\nВведіть валюту, яку обмінюєте: ')

if currency_in not in ['AZN', 'BYN', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'GEL', 'HUF',
                       'ILS', 'JPY', 'KZT', 'MDL', 'NOK', 'PLN', 'RUB', 'SEK', 'SGD', 'TMT', 'TRY',
                       'UAH', 'USD', 'UZS']:
    print('Такої валюти нема!')
    exit()

currency_out = input('Введіть валюту, на яку хочете обміняти: ')

if currency_out not in ['AZN', 'BYN', 'CAD', 'CHF', 'CNY', 'CZK', 'DKK', 'EUR', 'GBP', 'GEL', 'HUF',
                        'ILS', 'JPY', 'KZT', 'MDL', 'NOK', 'PLN', 'RUB', 'SEK', 'SGD', 'TMT', 'TRY',
                        'UAH', 'USD', 'UZS']:
    print('Такої валюти нема!')
    exit()

cash = float(input(f'\nВведіть к-ть {currency_in}: '))

if cash < 0:
    print('Обмінюйте додатню суму!')

print(converter(currency_in, currency_out, cash))
