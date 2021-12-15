"""
1. Доповніть програму-банкомат з попереднього завдання таким функціоналом, як використання банкнот.
   Отже, у банкомата повинен бути такий режим як "інкассація", за допомогою якого в нього можна "загрузити" деяку кількість банкнот (вибирається номінал і кількість).
   Зняття грошей з банкомату повинно відбуватись в межах наявних банкнот за наступним алгоритмом - видається мінімальна кількість банкнот наявного номіналу. P.S. Будьте обережні з використанням "жадібного" алгоритму (коли вибирається спочатку найбільша банкнота, а потім - наступна за розміром і т.д.) - в деяких випадках він працює неправильно або не працює взагалі. Наприклад, якщо треба видати 160 грн., а в наявності є банкноти номіналом 20, 50, 100, 500,  банкомат не зможе видати суму (бо спробує видати 100 + 50 + (невідомо), а потрібно було 100 + 20 + 20 + 20 ).
   Особливості реалізації:
   - перелік купюр: 10, 20, 50, 100, 200, 500, 1000;
   - у одного користувача повинні бути права "інкасатора". Відповідно і у нього буде своє власне меню із пунктами:
     - переглянути наявні купюри;
     - змінити кількість купюр;
   - видача грошей для користувачів відбувається в межах наявних купюр;
   - якщо гроші вносяться на рахунок - НЕ ТРЕБА їх розбивати і вносити в банкомат - не ускладнюйте собі життя, та й, наскільки я розумію, банкомати все, що в нього входить, відкладає в окрему касету.
"""

import json


def check_bank_bal():
    try:
        with open('wallet.json', 'x') as wallet_data:
            wallet = {1000: 0, 500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0}
            json.dump(wallet, wallet_data)
    except FileExistsError:
        pass

    with open('wallet.json', 'rt') as wallet_data:
        wallet = json.load(wallet_data)
        for key in wallet:
            print(f'{key}: {wallet[key]}')


def add_bank_cash():
    try:
        with open('wallet.json', 'x') as wallet_data:
            wallet = {1000: 0, 500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0}
            json.dump(wallet, wallet_data)
    except FileExistsError:
        pass

    with open('wallet.json', 'r') as wallet_data:
        wallet = json.load(wallet_data)
        add_wallet = input('Введіть розмір банкнот, які хочете додати на баланс(10/20/50/100/200/500/1000): ')
        add_num = int(input('Введіть к-ть банкнот: '))

        wallet[add_wallet] += add_num

    with open('wallet.json', 'w') as wallet_data:
        json.dump(wallet, wallet_data)


def change_wallet(wallet):
    if wallet == '1000':
        return ['500', 2]
    elif wallet == '500':
        return ['200', 2, '100', 1]
    elif wallet == '200':
        return ['100', 2]
    elif wallet == '100':
        return ['50', 2]
    elif wallet == '50':
        return ['20', 2, '10', 1]
    elif wallet == '20':
        return ['10', 2]
    else:
        return


def checkusers():
    user_data = open('user.data', 'rt')

    user_list = []
    users = user_data.read().split('\n')
    for i in range(len(users)):
        user = users[i].split(', ')
        user_list.append(user)
    return user_list


def login(users):
    print('------------------------Login------------------------')
    username = input("Введіть ім'я користувача: ")
    password = input("Введіть пароль: ")
    for user in users:
        if len(user) == 3 and user[0] == username and user[1] == password and user[2] == 'True':
            return username, True, True
        elif user[0] == username and user[1] == password:
            return username, True, False

    return username, False, False


def operation(user):
    mode = input('Виберіть режим:\n\t(1)Перевірити баланс\n\t(2)Нарахувати кошти\n\t(3)Зняти кошти\n\t(0)Вихід\n\n')

    if mode == '1':
        check_bal(user)
    elif mode == '2':
        add_cash(user)
    elif mode == '3':
        get_cash(user)
    else:
        exit()


def operation_collector():
    mode = input('Виберіть режим:\n\t(1)Перевірити баланс банкомата\n\t(2)Поповнити баланс банкомата\n\t(0)Вихід\n\n')

    if mode == '1':
        check_bank_bal()
    elif mode == '2':
        add_bank_cash()
    else:
        exit()


def check_bal(user):
    try:
        with open(f'{user}_balance.data', 'r') as balance:
            print(balance.read())
    except FileNotFoundError:
        print(0)


def add_cash(user):
    cash = float(input('Введіть суму, яку ви б хотіли нарахувати на рахунок: '))
    if cash >= 0:
        try:
            with open(f'{user}_balance.data', 'x') as balance_data:
                balance_data.write(str(cash))
            print('Кошти успішно нараховано.')
        except FileExistsError:
            with open(f'{user}_balance.data', 'rt') as balance_data:
                balance = float(balance_data.read())

            with open(f'{user}_balance.data', 'w') as balance_data:
                balance_data.truncate(0)
                balance_data.write(str(balance + cash))
            print('Кошти успішно нараховано.')

            try:
                transactions = open(f'{user}_transactions.json', 'x')
                transactions.close()
            except FileExistsError:
                pass

            with open(f'{user}_transactions.json', 'a') as transactions_data:
                json.dump(f'+ {cash} UAH.', transactions_data)
                transactions_data.write('\n')
    else:
        print('Вкажіть справжню суму.')


def get_cash(user):
    try:
        with open('wallet.json', 'x') as wallet_data:
            wallet = {1000: 0, 500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0}
            json.dump(wallet, wallet_data)
            print('Вибачте, на даний момент, в банкоматі немає грошей.')
            start(user, False)

    except FileExistsError:
        pass

    wallet_list = {}
    bank_bal = 0
    with open('wallet.json', 'rt') as wallet_data:
        wallet = json.load(wallet_data)
        for key in wallet:
            wallet_name = key
            wallet_num = wallet[key]
            wallet_list[wallet_name] = int(wallet_num)
            bank_bal += int(wallet_name) * int(wallet_num)

    wallet_used = {'1000': 0, '500': 0, '200': 0, '100': 0, '50': 0, '20': 0, '10': 0}
    if wallet_list == wallet_used:
        print('Вибачте, на даний момент, в банкоматі немає грошей.')
        start(user, False)

    cash = int(input('Введіть суму, яку ви б хотіли зняти з рахунку: '))

    with open(f'{user}_balance.data', 'r') as bal:
        user_balance = bal.read()

    withdrawed_cash = cash
    transaction_cash = cash

    if 0 <= cash <= float(user_balance):
        try:
            with open(f'{user}_balance.data', 'rt') as balance_data:
                balance = float(balance_data.read())

            if balance >= cash or bank_bal >= cash:
                if cash % 10 == 0:
                    if not wallet_list['10'] == 0:
                        if cash % 100 == 10 or cash % 100 == 30:
                            wallet_used['20'] += cash % 100 // 20
                            wallet_used['10'] += 1

                        elif cash % 100 == 20:
                            wallet_used['20'] += cash % 100 // 20

                        elif cash % 100 == 40:
                            wallet_used['20'] += 2

                        elif cash % 100 == 50 or cash % 100 == 70:
                            wallet_used['50'] += 1
                            wallet_used['20'] += (cash % 100 - 50) // 20

                        elif cash % 100 == 90:
                            wallet_used['50'] += 1
                            wallet_used['20'] += 2

                        elif cash % 100 == 60 or cash % 100 == 80:
                            wallet_used['50'] += 1
                            wallet_used['20'] += (cash % 100 - 60) // 20
                            wallet_used['10'] += 1

                        cash = cash - cash % 100

                        for wallet in wallet_list:
                            wallet_number = int(cash // int(wallet))
                            cash = cash % int(wallet)

                            if wallet_number > 0:
                                wallet_used[wallet] += wallet_number

                    elif wallet_list['10'] == 0 and not wallet_list['20'] == 0:
                        if cash == 10 or cash == 30:
                            print('Не можливо видати')
                            start(user, False)

                        if cash % 100 == 10 or cash % 100 == 30:
                            wallet_used['100'] -= 1
                            wallet_used['50'] += 1
                            wallet_used['20'] += (50 + cash % 100) // 20

                        elif cash % 100 == 20:
                            wallet_used['20'] += cash % 100 // 20

                        elif cash % 100 == 40:
                            wallet_used['20'] += 2

                        elif cash % 100 == 50 or cash % 100 == 70:
                            wallet_used['50'] += 1
                            wallet_used['20'] += (cash % 100 - 50) // 20

                        elif cash % 100 == 90:
                            wallet_used['50'] += 1
                            wallet_used['20'] += (cash % 100 - 50) // 20

                        elif cash % 100 == 60 or cash % 100 == 80:
                            wallet_used['20'] += cash % 100 // 20

                        cash = cash - cash % 100

                        for wallet in wallet_list:
                            wallet_number = int(cash // int(wallet))
                            cash = cash % int(wallet)

                            if wallet_number > 0:
                                wallet_used[wallet] += wallet_number

                    else:
                        if cash % min(map(int, wallet_list.keys())) == 0:
                            for wallet in wallet_list:
                                wallet_number = int(cash // int(wallet))
                                cash = cash % int(wallet)

                                if wallet_number > 0:
                                    wallet_used[wallet] += wallet_number

                        else:
                            print('Неможливо видати.')
                            start(user, False)

                start_used = list(wallet_used.values())


                wallet_change_count = wallet_used
                wallet_end = {'1000': 0, '500': 0, '200': 0, '100': 0, '50': 0, '20': 0, '10': 0}

                for i in wallet_used:
                    if wallet_list[i] < wallet_used[i]:
                        wallet_change_count[i] = wallet_used[i] - wallet_list[i]
                        wallet_end[i] -= wallet_change_count[i]

                        for wallet_change_cycle in range(wallet_change_count[i]):
                            if i == '500' or i == '50':
                                if wallet_change_count[i] % 2 == 0:
                                    if i == '500':
                                        wallet_used['200'] += int(500 * wallet_change_count[i] / 200)

                                    else:
                                        wallet_used['20'] += int(50 * wallet_change_count[i] / 20)
                                    wallet_used[i] -= wallet_change_count[i]
                                    break
                                else:
                                    try:
                                        new_wallet = change_wallet(i)
                                        wallet_used[new_wallet[0]] += new_wallet[1]
                                        wallet_used[new_wallet[2]] += new_wallet[3]
                                        wallet_used[i] -= 1
                                    except TypeError:
                                        print('Недостатньо грошей на балансі банкомата')
                                        start(user, False)

                            else:
                                try:
                                    new_wallet = change_wallet(i)
                                    wallet_used[new_wallet[0]] += new_wallet[1]
                                    wallet_used[i] -= 1
                                except TypeError:
                                    print('Недостатньо грошей на балансі банкомата')
                                    start(user, False)

                        for element1 in wallet_end:
                            wallet_end[element1] += wallet_used[element1]

                list_counter = 0
                for element2 in wallet_end:
                    wallet_end[element2] += start_used[list_counter]
                    list_counter += 1
                wallet_list_new = {}
                with open('wallet.json', 'rt') as wallet_data:
                    wallet = json.load(wallet_data)
                    for key in wallet:
                        wallet_name = key
                        wallet_num = wallet[key]
                        wallet_list_new[wallet_name] = int(wallet_num)

                for wal_dat in wallet_list:
                    wallet[wal_dat] = wallet_list_new[wal_dat] - wallet_end[wal_dat]

                for banknote in wallet:
                    if wallet[banknote] < 0:
                        print('Не вистачає грошей в банкоматі.')
                        start(user, False)

                for element in wallet_end:
                    if wallet_end[element] > 0:
                        print(f'{element}: {int(wallet_end[element])}')

                with open('wallet.json', 'w') as wallet_data:
                    for wal_dat in wallet_list:
                        wallet[wal_dat] = wallet_list_new[wal_dat] - wallet_end[wal_dat]

                    json.dump(wallet, wallet_data)

                print('Кошти успішно знято.')
            else:
                print('Недостатньо коштів на рахунку.')
                start(user, False)

            with open(f'{user}_balance.data', 'w') as balance_data:
                balance_data.truncate(0)
                balance_data.write(str(balance - withdrawed_cash))

            try:
                transactions = open(f'{user}_transactions.json', 'x')
                transactions.close()
            except FileExistsError:
                pass

            with open(f'{user}_transactions.json', 'a') as transactions_data:
                json.dump(f'- {transaction_cash} UAH.', transactions_data)
                transactions_data.write('\n')

        except FileNotFoundError:
            print('У вас немає коштів на рахунку.')
    else:
        if not cash >= 0:
            print('Вкажіть справжню суму.')
        else:
            print('Недостатньо коштів на рахунку.')

def start(user, collector):
    if collector:
        while True:
            operation_collector()
            if input('Продовжити? y/n \n\t') == 'n':
                break
    else:
        while True:
            operation(user)
            if input('Продовжити? y/n \n\t') == 'n':
                break


users = checkusers()
username, login_result, collector = login(users)

login_fail = 0

if not login_result:
    while login_fail < 2:
        print("Неправильне ім'я/пароль. Спробуйте ще раз.")
        username, login_result, collector = login(users)
        if login_result:
            start(username, collector)
            break
        else:
            login_fail += 1
    print('Спроби вичерпано, до побачення.')
else:
    start(username, collector)
