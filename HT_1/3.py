"""
3. Write a script to sum of the first n positive integers.

"""
n = int(input('Кількість чисел: '))

NumberSum = 0

for i in range(n):
    Number = int(input('Число ' + str(i+1) + ': '))

    NumberSum += Number


print(NumberSum)
