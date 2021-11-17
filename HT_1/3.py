"""
3. Write a script to sum of the first n positive integers.

"""


n = int(input('Число: '))

NumberSum = 0

for i in range(n):
    Number = i+1

    NumberSum += Number


print(NumberSum)
