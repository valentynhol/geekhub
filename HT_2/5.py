"""
5. Написати скрипт, який залишить в словнику тільки пари із унікальними значеннями (дублікати значень - видалити). 
Словник для роботи захардкодити свій.

                Приклад словника (не використовувати):
                {'a': 1, 'b': 3, 'c': 1, 'd': 5}
                Очікуваний результат:
                {'a': 1, 'b': 3, 'd': 5}
"""

DuplicatedDict = {1: ':)', 2: ':P', 3: ':/', 4: ':0', 5: ':D', 6: ':/', 7: ':)'}
NormalDict = {}
print('Початковий словник: ',DuplicatedDict)

for i in DuplicatedDict:
    if not DuplicatedDict[i] in NormalDict.values():
        NormalDict[i] = DuplicatedDict[i]

print('Кінцевий словник: ',NormalDict)
