def season(month):
    if month >= 3 and month <= 5:
        result = 'Spring'
    elif month >= 6 and month <= 8:
        result = 'Summer'
    elif month >= 9 and month <= 11:
        result = 'Autumn'
    else:
        result = 'Winter'

    return result

month = int(input('Введіть номер місяця: '))

print(season(month))
