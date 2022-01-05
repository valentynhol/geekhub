"""
6. Створіть клас в якому буде атребут який буде рахувати кількість створених екземплярів класів.
"""


class ObjCounter(object):
    count = 0

    def __init__(self):
        ObjCounter.count += 1


"""
object1 = ObjCounter()
print(object1.count)

object2 = ObjCounter()
print(object2.count)

object3 = ObjCounter()
print(object3.count)

object4 = ObjCounter()
print(object4.count)

object5 = ObjCounter()
print(object5.count)
"""
