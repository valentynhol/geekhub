def x_bigger(x, y):
    print('x більше ніж у на',x - y)

def y_bigger(x, y):
    print('y більше ніж x на',y - x)

def equal(x, y):
    print('x дорівнює у')

def check(x, y):
    if x > y:
        x_bigger(x, y)
    elif x < y:
        y_bigger(x, y)
    else:
        equal(x, y)

x, y = map(int, input('Введіть Х і Y через кому: ').split(', '))

check(x, y)
