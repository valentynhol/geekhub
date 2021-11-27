"""
5. Написати функцію < fibonacci >, яка приймає один аргумент і 
виводить всі числа Фібоначчі, що не перевищують його.
"""

def fibonacci(end, *args):
    number = 0
    prev_num = 0
    prev_prev_num = 1
    fibonacci_number_list = []

    while number <= end:
        fibonacci_number_list += [number]
        number = prev_num + prev_prev_num
        prev_prev_num = prev_num
        prev_num = number
        

    return fibonacci_number_list

end_num = int(input('Введіть кінцеве число: '))

print(fibonacci(end_num))
