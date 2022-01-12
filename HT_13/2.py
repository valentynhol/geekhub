"""
2. Створити клас Person, в якому буде присутнім метод __init__ який буде приймати * аргументів, які зберігатиме в відповідні змінні. Методи, які повинні бути в класі Person - show_age, print_name, show_all_information.
   - Створіть 2 екземпляри класу Person та в кожному з екземплярів створіть атребут profession.
"""


class Person(object):
    """
    Usage:
        person = Person('name' --> str, 'surname' --> str, 'profession' --> str, 'age' --> int, 'sex'(M or F) --> str)

    Attributes
    ----------------
    name --> str(default: None):
        Represents person's name

    surname --> str(default: None):
        Represents person's surname

    profession --> str(default: None):
        Represents people's profession

    age --> int(default: None):
        Represents people's name

    sex --> str(default: None, 'M' or 'F'):
        Represents people's sex

    all_information --> dict(default: {}):
        Contains all info about people

    Methods
    ----------------
    show_age(self):
        Returns self's age

    print_name(self):
        Prints self's name

    show_all_information(self):
        Shows all info about self
    """
    name = None
    surname = None
    age = None
    sex = None
    all_information = {}

    def __init__(self, *args):
        for arg in args:
            if arg == 'M' or arg == 'F' and not self.sex:
                self.sex = arg
                self.all_information['sex'] = arg
            elif isinstance(arg, int):
                self.age = arg
                self.all_information['age'] = arg
            elif isinstance(arg, str) and not self.name:
                self.name = arg
                self.all_information['name'] = arg
            elif isinstance(arg, str) and self.name and not self.surname:
                self.surname = arg
                self.all_information['surname'] = arg

    def show_age(self):
        return self.age

    def print_name(self):
        print(self.name, self.surname)

    def show_all_information(self):
        return self.all_information


person1 = Person('Vasya', 'Petiov')
person1.profession = 'Firefighter'
person2 = Person()
person2.profession = 'Programmer'

print(person1.profession, person2.profession)

# print(person1.show_age())
# person1.print_name()
# print(person1.show_all_information())
