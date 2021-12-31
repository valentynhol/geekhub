"""
3. Напишіть програму, де клас «геометричні фігури» (figure) містить властивість color з початковим значенням white і
метод для зміни кольору фігури, а його підкласи «овал» (oval) і «квадрат» (square) містять методи __init__ для
завдання початкових розмірів об'єктів при їх створенні.
"""


class Figure(object):
    color = 'White'


class Oval(Figure):
    def __init__(self, a=1, b=1):
        self.length = a
        self.width = b


class Square(Figure):
    def __init__(self, a=1, b=1):
        self.length = a
        self.width = b


# figure = Figure()
# oval = Oval(5, 8)
# square = Square(3)

# print(square.color, square.width, square.length)
# print(oval.color, oval.width, oval.length)
# print(figure.color)
