"""
6. Вводиться число. Якщо це число додатне, знайти його квадрат, 
якщо від'ємне, збільшити його на 100, якщо дорівнює 0, не змінювати.
"""

def num_changer(number, *args):
    if number > 0:
        number *= number
    elif number < 0:
        number += 100

    return number

number = int(input('Введіть число: '))

print(num_changer(number))
