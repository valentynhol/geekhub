"""
2. Користувачем вводиться початковий і кінцевий рік. Створити цикл, 
який виведе всі високосні роки в цьому проміжку (границі включно).
"""

FirstPoint = int(input('Введіть початковий рік: '))
LastPoint = int(input('Введіть кінцевий рік: '))

for year in range(FirstPoint, LastPoint+1):
    if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0:
        print(year)
