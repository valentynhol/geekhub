"""
8. Написати функцію, яка буде реалізувати логіку 
циклічного зсуву елементів в списку. 
Тобто, функція приймає два аргументи: список і величину зсуву 
(якщо ця величина додатня - пересуваємо з кінця на початок, 
якщо від'ємна - навпаки - пересуваємо елементи 
з початку списку в його кінець).

   Наприклад:
       fnc([1, 2, 3, 4, 5], shift=1) --> [5, 1, 2, 3, 4]
       fnc([1, 2, 3, 4, 5], shift=-2) --> [3, 4, 5, 1, 2]
"""

def cycler(input_list, shift, *args):
    cycled_list = input_list * 3
    output_list = []

    for i in range(shift, len(input_list) + shift):
        output_list += [cycled_list[i % len(input_list)]]

    return output_list

input_list = [1, 2, 3, 4, 5]
shift = int(input('Введіть розмір відхилення: '))

print(cycler(input_list, shift*(-1)))
