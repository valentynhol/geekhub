"""
1. Створити клас Calc, який буде мати атребут last_result та 4 методи. Методи повинні виконувати математичні операції з
2-ма числами, а саме додавання, віднімання, множення, ділення.
   - Якщо під час створення екземпляру класу звернутися до атребута last_result він повинен повернути пусте значення
   - Якщо використати один з методів - last_result повенен повернути результат виконання попереднього методу.
   - Додати документування в клас (можете почитати цю статтю: https://realpython.com/documenting-python-code/ )
"""


class Calc(object):
    """
        A class that used to calculate simple expressions

        ...

        Attributes
        ----------------------------------------------------------
        last_result: int or float
            Shows last expression result

        Methods
        ----------------------------------------------------------
        addition(a, b):
            Adds a and b and sets this result to last_result

        substraction(a, b):
            Substracts b from a and sets this result to last_result

        multiplication(a, b):
            Multiplies a by b and sets this result to last_result

        division(a, b):
            Divides a by b and sets this result to last_result

        ----------------------------------------------------------
    """

    last_result = None

    def addition(self, a, b):
        Calc.last_result = a + b
        return a + b

    def subtraction(self, a, b):
        Calc.last_result = a - b
        return a - b

    def multiplication(self, a, b):
        Calc.last_result = a * b
        return a * b

    def division(self, a, b):
        if b == 0:
            Calc.last_result = None
            return 'Ділення на нуль неможливе'
        else:
            Calc.last_result = a / b
            return a / b


help(Calc)

# calculator = Calc()

# print(calculator.division(0, 1))
# print(calculator.multiplication(9, 3))
# print(calculator.addition(9, 3))
# print(calculator.subtraction(9, 3))
