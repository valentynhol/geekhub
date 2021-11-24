a, sign, b = input('Напишіть вираз у формі a (+,-,*,/) b: ').split() 

if sign == '+':
	result = int(a) + int(b)
elif sign == '-':
	result = int(a) - int(b)
elif sign == '*':
	result = int(a) * int(b)
elif sign == '/':
	result = int(a) / int(b)

print(result)
