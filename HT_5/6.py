"""
6. Всі ви знаєте таку функцію як <range>. Напишіть свою реалізацію цієї функції.
   P.S. Повинен вертатись генератор.
   P.P.S. Для повного розуміння цієї функції - можна почитати документацію по ній: https://docs.python.org/3/library/stdtypes.html#range
"""
class MyRangeError(Exception):
        pass

def generator(start, stop, step):
        if step > 0:
                while True:  
                        if start < stop:
                                yield start
                        else:
                                break
                        start += step
        elif step < 0:
                while True:  
                        if start > stop:
                                yield start
                        else:
                                break
                        start += step


def my_range(*args):
        if len(args) == 1:
                start = 0
                stop = args[0]
                step = 1
        elif len(args) == 2:
                start = args[0]
                stop = args[1]
                step = 1
        elif len(args) == 3:
                start = args[0]
                stop = args[1]
                step = args[2]
        else:
                raise MyRangeError
        
        return generator(start, stop, step)

print([num for num in my_range(100, 17, -2)])
