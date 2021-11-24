HardcodedTupleList = [(10, 20, 40), (40, 50, 60, 70), (80, 90), (1000,)]
Change = input('Введіть величину, на яку замінити: ')
ChangedTupleList = []

for tupl in HardcodedTupleList:
    ChangedTupleList += [(tupl[:-1:] + (Change,))]

print(ChangedTupleList)
