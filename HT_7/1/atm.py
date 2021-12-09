"""
1. Програма-банкомат.
   Створити програму з наступним функціоналом:
      - підтримка 3-4 користувачів, які валідуються парою ім'я/пароль (файл <users.data>);
      - кожен з користувачів має свій поточний баланс (файл <{username}_balance.data>) та історію транзакцій (файл <{username}_transactions.data>);
      - є можливість як вносити гроші, так і знімати їх. Обов'язкова перевірка введених даних (введено число; знімається не більше, ніж є на рахунку).
   Особливості реалізації:
      - файл з балансом - оновлюється кожен раз при зміні балансу (містить просто цифру з балансом);
      - файл - транзакціями - кожна транзакція у вигляді JSON рядка додається в кінець файла;
      - файл з користувачами: тільки читається. Якщо захочете реалізувати функціонал додавання нового користувача - не стримуйте себе :)
   Особливості функціонала:
      - за кожен функціонал відповідає окрема функція;
      - основна функція - <start()> - буде в собі містити весь workflow банкомата:
      - спочатку - логін користувача - програма запитує ім'я/пароль. Якщо вони неправильні - вивести повідомлення про це і закінчити роботу (хочете - зробіть 3 спроби, а потім вже закінчити роботу - все на ентузіазмі :) )
      - потім - елементарне меню типа:
        Введіть дію:
           1. Продивитись баланс
           2. Поповнити баланс
           3. Вихід
      - далі - фантазія і креатив :)
"""


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
    globals()['username'] = username
    for user in users:
        if user[0] == username and user[1] == password:
            return True

    return False


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
    cash = float(input('Введіть суму, яку ви б хотіли зняти з рахунку: '))
    if cash >= 0:
        try:
            with open(f'{user}_balance.data', 'rt') as balance_data:
                balance = float(balance_data.read())

            if balance >= cash:
                with open(f'{user}_balance.data', 'w') as balance_data:
                    balance_data.truncate(0)
                    balance_data.write(str(balance - cash))

                print('Кошти успішно знято.')
            else:
                print('Недостатньо коштів на рахунку.')

            try:
                transactions = open(f'{user}_transactions.data', 'x')
                transactions.close()
            except FileExistsError:
                pass

            with open(f'{user}_transactions.data', 'a') as transactions_data:
                transactions_data.write(f'\nЗ рахунку знято {cash} грн.')

        except FileNotFoundError:
            print('У вас немає коштів на рахунку.')
    else:
            print('Вкажіть справжню суму.')


def start(user):
    while True:
        operation(user)
        if input('Продовжити? y/n \n\t') == 'n':
            break


users = checkusers()
login_result = login(users)


username = globals()['username']

if login_result:
    start(username)
else:
    print("Неправильне ім'я/пароль. Спробуйте ще раз.")
    login_result = login(users)
    if login_result:
        start(username)
    else:
        print("Неправильне ім'я/пароль. Спробуйте ще раз.")
        login_result = login(users)
        if login_result:
            start(username)
        else:
            print('Спроби вичерпано. До побачення.')
            exit()
