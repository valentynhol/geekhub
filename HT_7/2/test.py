with open('file.data', 'rt') as file:
    string = str(file.read())
    symbol_num = 3

    if len(string) >= 3 * symbol_num:
        start_block = string[0:symbol_num]
        end_block = string[len(string) - symbol_num:len(string)]
        center_block = string[int(0.5 * len(string) - 0.5 * symbol_num):int(0.5 * len(string) + 0.5 * symbol_num)]

print(start_block, center_block, end_block)