"""
2. Створити клас Person, в якому буде присутнім метод __init__ який буде приймати * аргументів, які зберігатиме в відповідні змінні. Методи, які повинні бути в класі Person - show_age, print_name, show_all_information.
   - Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атребут profession.
"""


class Person(object):
    def __init__(self, **kwargs):
        for kwarg in kwargs:
            exec('self.' + kwarg + " = '" + str(kwargs[kwarg]) + "'")
        self.all_information = kwargs

    def show_age(self):
        try:
            return self.age
        except AttributeError:
            print(None)

    def print_name(self):
        try:
            print(self.name, self.surname)
        except AttributeError:
            return None

    def show_all_information(self):
        return self.all_information


person1 = Person(profession='Firefighter')
person2 = Person()
person2.profession = 'Programmer'

print(person1.profession, person2.profession)

# print(person1.show_age())
# person1.print_name()
# print(person1.show_all_information())
