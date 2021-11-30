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
        print("Status: Ім'я має бути не меншим від 3 і не більшим від 50 символів.")
    elif len(password) < 8:
        print("Status: Пароль має бути не менше 8 символів.")
    elif not digit:
        print("Status: Пароль має бути хоча б з 1 цифрою.")
    elif not upper or not lower:
        print("Status: Пароль має бути хоча б з 1 великою і 1 малою буквами.")
    else:
        print("Status: Ім'я і пароль підходять")

users = iter([["admin", "Admin123"],
        ["hehe", "justnoth1n'"],
        ["userlol", "LoLoLoLo"],
        ["hacker", "qwerty143"],
        ["a", "aWda;lwKfaw%76"],
        ["blablablablablablablablablablablablablablablablabla", "1  OwO  1"],
        ["username", "password"]])

pos = 0

while True:
    try:
        user = next(users)
    except StopIteration:
        break

    pos+=1
    print(pos,'-----------------------------------------------------------------')
    print('Name: ',user[0])
    print('Password: ',user[1])
    validation(user[0], user[1])
