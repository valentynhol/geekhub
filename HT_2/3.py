HardcodedList = [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
FullList = []

for item in HardcodedList:
    if item:
        FullList += [item]

print(FullList)
