"""
Переписати останню версію банкомата з використанням ООП.
"""
import sqlite3


class User(object):
    role = None

    def start(self, user):
        while True:
            self.role.operation(user)
            if input('Продовжити? y/n \n\t') == 'n':
                break

    def checkusers(self):
        database = sqlite3.connect('atm.db')
        cur = database.cursor()

        cur.execute('''SELECT * FROM users''')
        fetched = cur.fetchall()
        database.close()
        return fetched

    def login(self, users):
        print('------------------------Login------------------------')
        username = input("Введіть ім'я користувача: ")
        password = input("Введіть пароль: ")
        for user in users:
            if len(user) == 4 and user[1] == username and user[2] == password and user[3] == 1:
                return username, True, True
            elif user[1] == username and user[2] == password:
                return username, True, False

        return username, False, False


class Admin(User):
    def operation(self, *args):
        mode = input('Виберіть режим:\n\t'
                     '(1)Перевірити баланс банкомата\n\t'
                     '(2)Поповнити баланс банкомата\n\t'
                     '(0)Вихід\n\n')

        if mode == '1':
            admin_user.check_bank_bal()
        elif mode == '2':
            admin_user.add_bank_cash()
        else:
            exit()

    def check_bank_bal(self):
        database = sqlite3.connect('atm.db')
        cur = database.cursor()

        cur.execute('''SELECT * FROM wallet''')
        wallet_list = {}
        fetched = cur.fetchall()
        database.close()
        for wal_key in fetched:
            wallet_list[wal_key[0]] = wal_key[1]

        for key in wallet_list:
            print(f'{key}: {wallet_list[key]}')

    def add_bank_cash(self):
        database = sqlite3.connect('atm.db')
        cur = database.cursor()

        cur.execute('''SELECT * FROM wallet''')
        wallet_list = {}
        fetched = cur.fetchall()

        for wal_key in fetched:
            wallet_list[wal_key[0]] = wal_key[1]

        add_wallet = input('Введіть розмір банкнот, які хочете додати на баланс(10/20/50/100/200/500/1000): ')

        if add_wallet not in ['10', '20', '50', '100', '200', '500', '1000']:
            print('Введіть дійсний розмір банкнот!')
            database.close()
            exit()

        add_num = int(input('Введіть к-ть банкнот: '))

        if add_num < 0:
            print('Введіть додатню к-ть!')
            database.close()
            exit()

        wallet_list[add_wallet] += add_num
        cur.execute('''UPDATE wallet SET wallet_num=? WHERE wallet=?''', (wallet_list[add_wallet], add_wallet))
        database.commit()
        database.close()


class DefaultUser(User):
    def operation(self, user):
        mode = input('Виберіть режим:\n\t'
                     '(1)Перевірити баланс\n\t'
                     '(2)Нарахувати кошти\n\t'
                     '(3)Зняти кошти\n\t'
                     '(0)Вихід\n\n')

        if mode == '1':
            default_user.check_bal(user)
        elif mode == '2':
            default_user.add_cash(user)
        elif mode == '3':
            default_user.get_cash(user)
        else:
            exit()

    def change_wallet(self, wallet):
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

    def check_bal(self, user):
        database = sqlite3.connect('atm.db')
        cur = database.cursor()
        cur.execute('''SELECT balance FROM balance WHERE username=?''', (user,))
        print(cur.fetchone()[0])
        database.close()

    def add_cash(self, user):
        cash = float(input('Введіть суму, яку ви б хотіли нарахувати на рахунок: '))
        if cash >= 0:
            database = sqlite3.connect('atm.db')
            cur = database.cursor()
            cur.execute('''SELECT balance FROM balance WHERE username=?''', (user,))
            wallet = cur.fetchone()[0] + cash
            cur.execute('''UPDATE balance SET balance=? WHERE username=?''', (wallet, user))
            print('Кошти успішно нараховано.')

            cur.execute('''INSERT INTO transactions VALUES (?, ?)''', (user, f'+ {cash} UAH.'))
            database.commit()
            database.close()

        else:
            print('Вкажіть справжню суму.')

    def get_cash(self, user):
        # get wallet_list
        database = sqlite3.connect('atm.db')
        cur = database.cursor()

        cur.execute('''SELECT * FROM wallet''')
        wallet_list = {}
        fetched = cur.fetchall()

        for wal_key in fetched:
            wallet_list[wal_key[0]] = wal_key[1]
        database.close()
        # --------------

        bank_bal = 0
        for key in wallet_list:
            wallet_name = key
            wallet_num = wallet_list[key]
            wallet_list[wallet_name] = int(wallet_num)
            bank_bal += int(wallet_name) * int(wallet_num)

        wallet_used = {'1000': 0, '500': 0, '200': 0, '100': 0, '50': 0, '20': 0, '10': 0}
        if wallet_list == wallet_used:
            print('Вибачте, на даний момент, в банкоматі немає грошей.')
            default_user.start(user)

        cash = int(input('Введіть суму, яку ви б хотіли зняти з рахунку: '))

        database = sqlite3.connect('atm.db')
        cur = database.cursor()
        cur.execute('''SELECT balance FROM balance WHERE username=?''', (user,))
        balance = cur.fetchone()[0]
        database.close()

        withdrawed_cash = cash
        transaction_cash = cash

        if 0 <= cash <= float(balance):
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
                            default_user.start(user)

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
                            default_user.start(user)
                else:
                    print('Введіть число, яке ділиться на 10.')
                    default_user.start(user)

                wallet_change_count = {'1000': 0, '500': 0, '200': 0, '100': 0, '50': 0, '20': 0, '10': 0}

                for i in wallet_used:
                    if wallet_list[i] < wallet_used[i]:
                        wallet_change_count[i] = wallet_used[i] - wallet_list[i]

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
                                        new_wallet = default_user.change_wallet(i)
                                        wallet_used[new_wallet[0]] += new_wallet[1]
                                        wallet_used[new_wallet[2]] += new_wallet[3]
                                        wallet_used[i] -= 1
                                    except TypeError:
                                        print('Недостатньо грошей на балансі банкомата')
                                        default_user.start(user)

                            else:
                                try:
                                    new_wallet = default_user.change_wallet(i)
                                    wallet_used[new_wallet[0]] += new_wallet[1]
                                    wallet_used[i] -= 1
                                except TypeError:
                                    print('Недостатньо грошей на балансі банкомата')
                                    default_user.start(user)
                wallet = {}
                for wal_dat in wallet_list:
                    wallet[wal_dat] = wallet_list[wal_dat] - wallet_used[wal_dat]

                for banknote in wallet:
                    if wallet[banknote] < 0:
                        print('Не вистачає грошей в банкоматі.')
                        default_user.start(user)

                for element in wallet_used:
                    if wallet_used[element] > 0:
                        print(f'{element}: {int(wallet_used[element])}')

                for wal_dat in wallet_list:
                    wallet[wal_dat] = wallet_list[wal_dat] - wallet_used[wal_dat]

                database = sqlite3.connect('atm.db')
                cur = database.cursor()
                for wal in wallet:
                    cur.execute('''UPDATE wallet SET wallet_num=? WHERE wallet=?''', (wallet[wal], wal))
                database.commit()
                database.close()

                print('Кошти успішно знято.')
            else:
                print('Недостатньо коштів на рахунку.')
                default_user.start(user)

            database = sqlite3.connect('atm.db')
            cur = database.cursor()
            cur.execute('''UPDATE balance SET balance=? WHERE username=?''', (balance - withdrawed_cash, user))

            cur.execute('''INSERT INTO transactions VALUES (?, ?)''', (user, f'- {transaction_cash} UAH.'))
            database.commit()
            database.close()
        else:
            if not cash >= 0:
                print('Вкажіть справжню суму.')
            else:
                print('Недостатньо коштів на рахунку.')


unknown_role_user = User()
admin_user = Admin()
default_user = DefaultUser()

users = unknown_role_user.checkusers()
username, login_result, collector = unknown_role_user.login(users)
if collector:
    unknown_role_user.role = admin_user
else:
    unknown_role_user.role = default_user

DefaultUser.role = default_user
Admin.role = admin_user

login_fail = 0

if not login_result:
    while login_fail < 2:
        print("Неправильне ім'я/пароль. Спробуйте ще раз.")
        username, login_result, collector = unknown_role_user.login(users)
        if login_result:
            unknown_role_user.start(username)
            unknown_role_user.collector = collector
            break
        else:
            login_fail += 1
    print('Спроби вичерпано, до побачення.')
else:
    unknown_role_user.start(username)
