dict_1 = {1:10, 2:20}
dict_2 = {3:30, 4:40}
dict_3 = {5:50, 6:60}
big_dict = {}

for a in dict_1:
    big_dict[a] = dict_1[a]
for b in dict_2:
    big_dict[b] = dict_2[b]
for c in dict_3:
    big_dict[c] = dict_3[c]

print(big_dict)
