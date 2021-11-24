DuplicatedDict = {1: ':)', 2: ':P', 3: ':/', 4: ':0', 5: ':D', 6: ':/', 7: ':)'}
NormalDict = {}
print('Початковий словник: ',DuplicatedDict)

for i in DuplicatedDict:
    if not DuplicatedDict[i] in NormalDict.values():
        NormalDict[i] = DuplicatedDict[i]

print('Кінцевий словник: ',NormalDict)
