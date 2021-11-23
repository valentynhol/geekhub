JustAString = input('Поклацайте по клаві) ')
OnlyLetters = []
NumberSum = 0
numbers = 0
letters = 0

for symbol in JustAString:
    if symbol.isdigit():
        NumberSum += int(symbol)
        numbers += 1

    elif symbol.isalpha():
        OnlyLetters += symbol
        letters += 1


if len(JustAString) > 30 and len(JustAString) < 50:
    print('Довжина: ',len(JustAString))
    print('Цифр: ',numbers)
    print('Букв: ',letters)

elif len(JustAString) < 30:
    print('Сума чисел: ',NumberSum)
    print('Рядок без чисел: ',''.join(OnlyLetters))

elif len(JustAString) > 50:
    print('Рядок навпаки: ',JustAString[::-1])
    