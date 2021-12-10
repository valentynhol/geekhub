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


def check_bank_bal():
    try:
        with open('wallet.data', 'x') as wallet_data:
            wallet_data.write('1000: 0, 500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0')
    except FileExistsError:
        pass

    with open('wallet.data', 'rt') as wallet:
        wallet_data = wallet.read().split(', ')
        for i in wallet_data:
            wallet_name, wallet_num = i.split(': ')
            print(f'{wallet_name}: {wallet_num}')


def add_bank_cash():
    try:
        with open('wallet.data', 'x') as wallet_data:
            wallet_data.write('1000: 0, 500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0')
    except FileExistsError:
        pass

    wallet_data_list = {}
    with open('wallet.data', 'rt+') as wallet:
        wallet_data = wallet.read().split(', ')
        for i in wallet_data:
            wallet_name, wallet_num = map(int, i.split(': '))
            wallet_data_list[wallet_name] = wallet_num

        add_wallet = int(input('Введіть розмір банкнот, які хочете додати на баланс(10/20/50/100/200/500/1000): '))
        add_num = int(input('Введіть к-ть банкнот: '))

        wallet_data_list[add_wallet] += add_num
        end_count = 0
        writestr = ''

    with open('wallet.data', 'w') as wallet:
        for wal_dat in wallet_data_list:
            if end_count == 6:
                writestr += f'{wal_dat}: {wallet_data_list[wal_dat]}'
            else:
                writestr += f'{wal_dat}: {wallet_data_list[wal_dat]}, '
            end_count += 1

        wallet.write(writestr)



def change_wallet(wallet):
    if wallet == 1000:
        return [500, 2]
    elif wallet == 500:
        return [200, 2, 100, 1]
    elif wallet == 200:
        return [100, 2]
    elif wallet == 100:
        return [50, 2]
    elif wallet == 50:
        return [20, 2, 10, 1]
    elif wallet == 20:
        return [10, 2]


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
                transactions = open(f'{user}_transactions.data', 'x')
                transactions.close()
            except FileExistsError:
                pass

            with open(f'{user}_transactions.data', 'a') as transactions_data:
                transactions_data.write(f'\nРахунок поповнено на {cash} грн.')
    else:
        print('Вкажіть справжню суму.')


def get_cash(user):
    try:
        with open('wallet.data', 'x') as wallet_data:
            wallet_data.write('1000: 0, 500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0')
            print('Вибачте, на даний момент, в банкоматі немає грошей.')
            exit()
    except FileExistsError:
        pass

    wallet_list = {}
    bank_bal = 0
    with open('wallet.data', 'rt') as wallet:
        wallet_data = wallet.read().split(', ')
        for i in wallet_data:
            wallet_name, wallet_num = i.split(': ')
            wallet_list[int(wallet_name)] = int(wallet_num)
            bank_bal += int(wallet_name) * int(wallet_num)

    wallet_used = {1000: 0, 500: 0, 200: 0, 100: 0, 50: 0, 20: 0, 10: 0}
    if wallet_list == wallet_used:
        print('Вибачте, на даний момент, в банкоматі немає грошей.')
        exit()

    cash = float(input('Введіть суму, яку ви б хотіли зняти з рахунку: '))

    transaction_cash = cash
    try:
        if cash % wallet_list[min(wallet_list.keys())] == 0:
            pass
    except ZeroDivisionError:
        print('Неможливо видати.')
        exit()

    if cash >= 0:
        try:
            with open(f'{user}_balance.data', 'rt') as balance_data:
                balance = float(balance_data.read())

            if balance >= cash or bank_bal >= cash:
                with open(f'{user}_balance.data', 'w') as balance_data:
                    balance_data.truncate(0)
                    balance_data.write(str(balance - cash))

                if cash % 10 == 0:
                    if not wallet_list[10] == 0:
                        for wallet in wallet_list:
                            wallet_number = int(cash // wallet)
                            cash = cash % wallet

                            if wallet_number > 0:
                                wallet_used[wallet] += wallet_number

                    elif wallet_list[10] == 0 and not wallet_list[20] == 0:
                        if cash % 100 == 10 or cash % 100 == 30:
                            wallet_used[50] += 1
                            wallet_used[20] += (50 + cash % 100) // 20

                        elif cash % 100 == 20 or cash % 100 == 40:
                            wallet_used[100] += 1
                            wallet_used[20] += cash % 100 // 20

                        elif cash % 100 == 50 or cash % 100 == 70 or cash % 100 == 90:
                            wallet_used[50] += 1
                            wallet_used[20] += (cash % 100 - 50) // 20

                        elif cash % 100 == 60 or cash % 100 == 80:
                            wallet_used[100] += 1
                            wallet_used[20] += cash % 100 // 20

                        if cash % 100 == 0:
                            pass
                        else:
                            cash = cash - (100 + cash % 100)
                        for wallet in wallet_list:
                            wallet_number = int(cash // wallet)
                            cash = cash % wallet

                            if wallet_number > 0:
                                wallet_used[wallet] += wallet_number
                    else:
                        if cash % wallet_list[min(wallet_list.keys())] == 0:
                            for wallet in wallet_list:
                                wallet_number = int(cash // wallet)
                                cash = cash % wallet

                                if wallet_number > 0:
                                    wallet_used[wallet] += wallet_number

                        else:
                            print('Неможливо видати.')

                able = True
                for i in wallet_used:
                    if wallet_list[i] >= wallet_used[i]:
                        wallet_list[i] -= wallet_used[i]

                    elif wallet_list[i] < wallet_used[i]:
                        changing_wal = i
                        for wallet_change_cycle in range(wallet_used[i]):
                            changed = False
                            while not changed:
                                if changing_wal == 500 or changing_wal == 50:
                                    if change_wallet(changing_wal)[1] < wallet_list[change_wallet(changing_wal)[0]]:
                                        if change_wallet(changing_wal)[3] < wallet_list[change_wallet(changing_wal)[2]]:
                                            changed = True
                                            new_wallet = change_wallet(changing_wal)
                                            wallet_used[new_wallet[0]] = new_wallet[1]
                                            wallet_used[new_wallet[2]] = new_wallet[3]
                                        else:
                                            changing_wal = change_wallet(changing_wal)[2]
                                    else:
                                        changing_wal = change_wallet(changing_wal)[0]
                                else:
                                    if change_wallet(changing_wal)[1] < wallet_list[change_wallet(changing_wal)[0]]:
                                        changed = True
                                        new_wallet = change_wallet(changing_wal)
                                        wallet_used[new_wallet[0]] += new_wallet[1]
                                        wallet_used[i] -= 1
                                    else:
                                        changing_wal = change_wallet(changing_wal)[0]

                    else:
                        able = False
                        print('Неможливо видати.')
                        break

                if able:
                    for element in wallet_used:
                        if wallet_used[element] > 0:
                            print(f'{element}: {int(wallet_used[element])}')

                    wallet_list[i] -= wallet_used[i]
                with open('wallet.data', 'w') as wallet_data:
                    wallet_data.truncate(0)
                    writestr = ''
                    end_count = 0

                    for wal_dat in wallet_list:
                        if end_count == 6:
                            writestr += f'{wal_dat}: {wallet_list[wal_dat]}'
                        else:
                            writestr += f'{wal_dat}: {wallet_list[wal_dat]}, '
                        end_count += 1
                    wallet_data.write(writestr)


                print('Кошти успішно знято.')
            else:
                print('Недостатньо коштів на рахунку.')

            try:
                transactions = open(f'{user}_transactions.data', 'x')
                transactions.close()
            except FileExistsError:
                pass

            with open(f'{user}_transactions.data', 'a') as transactions_data:
                transactions_data.write(f'\nЗ рахунку знято {transaction_cash} грн.')

        except FileNotFoundError:
            print('У вас немає коштів на рахунку.')
    else:
        print('Вкажіть справжню суму.')


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
        else:
            login_fail += 1
    print('Спроби вичерпано, до побачення.')
else:
    start(username, collector)
