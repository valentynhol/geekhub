"""
4. Write a script to concatenate N strings.

"""

N = int(input('Введіть кількість фраз: '))


FinalStr = ''

for i in range(N):
    String = str(input('Фраза: '))
    FinalStr += String


print(FinalStr)
