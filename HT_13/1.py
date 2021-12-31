"""
1. Створити клас Calc, який буде мати атребут last_result та 4 методи. Методи повинні виконувати математичні операції з
2-ма числами, а саме додавання, віднімання, множення, ділення.
   - Якщо під час створення екземпляру класу звернутися до атребута last_result він повинен повернути пусте значення
   - Якщо використати один з методів - last_result повенен повернути результат виконання попереднього методу.
   - Додати документування в клас (можете почитати цю статтю: https://realpython.com/documenting-python-code/ )
"""


class Calc(object):
    last_result = None

    def addition(self, a, b):
        Calc.last_result = a + b
        return a + b
    addition.__doc__ = 'Проста функція додавання.'

    def subtraction(self, a, b):
        Calc.last_result = a - b
        return a - b
    subtraction.__doc__ = 'Проста функція віднімання.'

    def multiplication(self, a, b):
        Calc.last_result = a * b
        return a * b
    multiplication.__doc__ = 'Проста функція множення.'

    def division(self, a, b):
        Calc.last_result = a / b
        return a / b
    division.__doc__ = 'Проста функція ділення.'


help(Calc)

# calculator = Calc()

# print(calculator.division(9, 3))
# print(calculator.multiplication(9, 3))
# print(calculator.addition(9, 3))
# print(calculator.subtraction(9, 3))
