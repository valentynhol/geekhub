"""
7. Написати функцію, яка приймає на вхід список і 
підраховує кількість однакових елементів у ньому.
"""

def copy_duplicate_remover(original_list, *args):
    filtered_list = []

    for element in original_list:
        if not element in filtered_list:
            filtered_list += [element]

    return filtered_list

def repeat_counter(original_list, filtered_list, *args):
    repeat_dict = {}

    for i in filtered_list:
        repeat = 0

        for k in original_list:
            if i == k:
                repeat += 1

        repeat_dict[i] = repeat

    return repeat_dict

original_list = list(input('Введіть елементи списку через кому: ').split(', '))
print(repeat_counter(original_list, copy_duplicate_remover(original_list)))
