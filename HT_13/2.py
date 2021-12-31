"""
2. Створити клас Person, в якому буде присутнім метод __init__ який буде приймати * аргументів, які зберігатиме в відповідні змінні. Методи, які повинні бути в класі Person - show_age, print_name, show_all_information.
   - Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атребут profession.
"""


class Person(object):
    def __init__(self, name, surname, age, sex=None):
        self.name = name
        self.surname = surname
        self.age = age
        self.sex = sex

    def show_age(self):
        return self.age
    show_age.__doc__ = "Функція, яка повертає вік"

    def print_name(self):
        print(self.name, self.surname)
    print_name.__doc__ = "Функція, яка прінтує ім'я і прізвище"

    def show_all_information(self):
        return {'name': self.name, 'surname': self.surname, 'age': self.age, 'sex': self.sex}
    show_all_information.__doc__ = "Функція, яка повертає повну інформацію"


help(Person)

# person = Person('Вася', 'Хехехов', 21, 'Ч')

# print(person.show_age())
# person.print_name()
# print(person.show_all_information())
