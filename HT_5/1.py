"""
1. Створіть функцію, всередині якої будуть записано список із п'яти користувачів (ім'я та пароль).
   Функція повинна приймати три аргументи: два - обов'язкових (<username> та <password>) і третій - необов'язковий параметр <silent> (значення за замовчуванням - <False>).
   Логіка наступна:
       якщо введено коректну пару ім'я/пароль - вертається <True>;
       якщо введено неправильну пару ім'я/пароль і <silent> == <True> - функція вертає <False>, інакше (<silent> == <False>) - породжується виключення LoginException
"""

class LoginException(Exception):
    pass

def login(username, password, silent=False):
    users = [["admin", "admin123"], ["hehe", "justnothin'"], ["userlol", "lolololo"], ["hacker", "qwerty143"], ["username", "password"]]
      
    for user in users:
        if user[0] == username and user[1] == password:
            return True

    if silent:
        return False
    else:
        raise LoginException
        

username = input("Введіть ім'я користувача: ")
password = input("Введіть пароль: ")
silent = input('Silent(True/False/Пустий): ')

if silent == 'True' or silent == 'False':
    print(login(username, password, bool(silent)))
else:
    print(login(username, password))
