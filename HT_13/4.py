"""
4. Видозмініть програму так, щоб метод __init__ мався в класі «геометричні фігури» та приймав кольор фігури при
створенні екземпляру, а методи __init__ підкласів доповнювали його та додавали початкові розміри.
"""


class Figure(object):
    color = 'White'

    def __init__(self, color='White'):
        self.color = color


class Oval(Figure):
    def __init__(self, a=1, b=1):
        self.length = a
        self.width = b


class Square(Figure):
    def __init__(self, a=1, b=1):
        self.length = a
        self.width = b


# figure = Figure("Blue")
# oval = Oval(5, 8)
# square = Square(3)

# print(square.color, square.width, square.length)
# print(oval.color, oval.width, oval.length)
# print(figure.color)
