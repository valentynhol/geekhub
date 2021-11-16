"""
6. Write a script to check whether a specified value
is contained in a group of values.

"""


Value = input('Введіть значення: ')
ValList = list(input('Введіть список значень: ').split(', '))


Output = False

for i in ValList:
    if Value == i:
        Output = True


print(Output)
