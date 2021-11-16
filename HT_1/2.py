"""
2. Write a script to print out a set containing all the colours from
color_list_1 which are not present in color_list_2.

"""

ListOfColours1 = set(input('Введіть дані 1 списку: ').split(', '))
ListOfColours2 = set(input('Введіть дані 2 списку: ').split(', '))

FinalList = set()

for colour1 in ListOfColours1:
    for colour2 in ListOfColours2:
        if not colour1 == colour2:
            FinalList.add(colour1)

print(FinalList)
