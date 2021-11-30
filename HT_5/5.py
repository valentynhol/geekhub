"""
5. Запишіть в один рядок генератор списку (числа в діапазоні від 0 до 100), сума цифр кожного елемент якого буде дорівнювати 10.
"""

print([str(number)[0]+str(number)[1] for number in range(100) if number>=10 if int(str(number)[0])+int(str(number)[1])==10])
