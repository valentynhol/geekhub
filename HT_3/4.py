def plus(a, b):
    return a + b

def minus(a, b):
    return a - b

def maximum(a, b):
    return max(a, b)

def caller(a, b):
    print('Сума: ', plus(a, b))
    print('Різниця: ', minus(a, b))
    print('Найбільше число: ', maximum(a, b))

a, b = map(int, input('Введіть через кому два числа: ').split(', '))

caller(a, b)
