"""
6. Маємо рядок --> 
"f98neroi4nr0c3n30irn03ien3c0rfekdno400wenwkowe00koijn35pijnp46ij7k5j78p3kj546p465jnpoj35po6j345" 
-> просто потицяв по клавi

   Створіть ф-цiю, яка буде отримувати рядки на зразок цього, яка оброблює наступні випадки:
-  якщо довжина рядка в діапазонi 30-50 -> прiнтує довжину, кiлькiсть букв та цифр
-  якщо довжина менше 30 -> прiнтує суму всiх чисел та окремо рядок без цифр (лише з буквами)
-  якщо довжина бульше 50 - > ваша фантазiя
"""

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
    