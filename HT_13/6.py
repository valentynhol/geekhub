"""
6. Створіть клас в якому буде атребут який буде рахувати кількість створених екземплярів класів.
"""


class ObjCounter(object):
    count = 0

    def __init__(self):
        ObjCounter.count += 1


"""
object1 = ObjCounter()
print(ObjCounter.count)

object2 = ObjCounter()
print(ObjCounter.count)

object3 = ObjCounter()
print(ObjCounter.count)

object4 = ObjCounter()
print(ObjCounter.count)

object5 = ObjCounter()
print(ObjCounter.count)
"""
