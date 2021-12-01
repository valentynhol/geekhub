"""
3. На основі попередньої функції створити наступний кусок кода:
   а) створити список із парами ім'я/пароль різноманітних видів (орієнтуйтесь по правилам своєї функції) - як валідні, так і ні;
   б) створити цикл, який пройдеться по цьому циклу і, користуючись валідатором, перевірить ці дані і надрукує для кожної пари значень відповідне повідомлення, наприклад:
      Name: vasya
      Password: wasd
      Status: password must have at least one digit
      -----
      Name: vasya
      Password: vasyapupkin2000
      Status: OK
   P.S. Не забудьте використати блок try/except ;)
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

    if len(username) < 3 or len(username) > 50:
        raise NameLenException
    elif len(password) < 8:
        raise PassLenException
    elif not digit:
        raise DigitPassException
    elif not upper or not lower:
        raise UpperLowerPassException
    else:
        print("Ім'я і пароль підходять")

users = iter([["admin", "Admin123"],
        ["hehe", "justnoth1n'"],
        ["userlol", "LoLoLoLo"],
        ["hacker", "qwerty143"],
        ["a", "aWda;lwKfaw%76"],
        ["blablablablablablablablablablablablablablablablabla", "1  OwO  1"],
        ["username", "password"]])

pos = 0

for pos, user in enumerate(users):
    print(pos+1,'-----------------------------------------------------------------')
    print('Name: ',user[0])
    print('Password: ',user[1])
    try:
        validation(user[0], user[1])
    except NameLenException:
        print("Status: Ім'я має бути не меншим від 3 і не більшим від 50 символів.")
    except PassLenException:
        print("Status: Пароль має бути не менше 8 символів.")
    except DigitPassException:
        print("Status: Пароль має бути хочаб з 1 цифрою.")
    except UpperLowerPassException:
        print("Status: Пароль має бути хочаб з 1 великою і 1 малою буквами.")
        
