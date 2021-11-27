"""
3. Написати функцию < is_prime >, яка прийматиме 1 аргумент - 
число від 0 до 1000, и яка вертатиме True, 
якщо це число просте, и False - якщо ні.
"""

def is_prime(number, *args):
    prime = True

    for i in range(2, number//2+1):
        if (number % i) == 0:
            prime = False
            break

    return prime

number = (int(input('Введіть число: ')))

if (number <= 1):
    print(False)
else:
    print(is_prime(number))
