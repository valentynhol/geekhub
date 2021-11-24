dict_1 = {1:10, 2:20}
dict_2 = {3:30, 4:40}
dict_3 = {5:50, 6:60}

for a in dict_2:
    dict_1[a] = dict_2[a]
for b in dict_3:
    dict_1[b] = dict_3[b]

print('dict_1='dict_1)
