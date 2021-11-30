"""
2. Створіть функцію для валідації пари ім'я/пароль за наступними правилами:
   - ім'я повинно бути не меншим за 3 символа і не більшим за 50;
   - пароль повинен бути не меншим за 8 символів і повинен мати хоча б одну цифру;
   - щось своє :)
   Якщо якийсь із параментів не відповідає вимогам - породити виключення із відповідним текстом.
"""

class NameLenException(Exception):
    pass

class PassLenException(Exception):
    pass

class DigitPassException(Exception):
    pass

class UpperLowerPassException(Exception):
    pass


def validation(username, password, *args):
    if len(username) < 3 or len(username) > 50:
        print("Ім'я має бути не меншим від 3 і не більшим від 50 символів.")
        raise NameLenException
    elif len(password) < 8:
        print("Пароль має бути не менше 8 символів.")
        raise PassLenException
    else:
        print("Ім'я і пароль підходять")
    digit = False
    upper = False
    lower = False

    for i in password:
        if i.isdigit():
            digit = True
            break

    for k in password:
        if k.isupper():
            upper = True
            break

    for m in password:
        if m.islower():
            lower = True
            break

    if not digit:
        print("Пароль має бути хочаб з 1 цифрою.")
        raise DigitPassException

    if not upper or not lower:
        print("Пароль має бути хочаб з 1 великою і 1 малою буквами.")
        raise UpperLowerPassException

username = input("Введіть ім'я користувача: ")
password = input("Введіть пароль: ")

validation(username, password)
