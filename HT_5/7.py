"""
7. Реалізуйте генератор, який приймає на вхід будь-яку ітерабельну послідовність (рядок, список, кортеж) і повертає генератор, який буде вертати значення з цієї послідовності, при цьому, якщо було повернено останній елемент із послідовності - ітерація починається знову.
   Приклад (якщо запустили його у себе - натисніть Ctrl+C ;) ):
   >>>for elem in generator([1, 2, 3]):
   ...    print(elem)
   ...
   1
   2
   3
   1
   2
   3
   1
   .......
"""

def generator(iterable, *args):
	while True:
		for i in iterable:
			print(i)

select = input('Введіть тип(tuple/list/str)')

if select == "tuple":
	iterable = tuple(input("Введіть об'єкти через кому: ").split(', '))
elif select == 'list':
	iterable = list(input("Введіть об'єкти через кому: ").split(', '))
elif select == "str":
	iterable = input("Введіть рядок: ")

generator(iterable)
