"""
1. Програма-світлофор.
   Створити програму-емулятор світлофора для авто і пішоходів.
   Після запуска програми на екран виводиться в лівій половині - колір автомобільного, а в правій - пішохідного світлофора.
   Кожну секунду виводиться поточні кольори. Через декілька ітерацій - відбувається зміна кольорів - логіка така сама як і в звичайних світлофорах.
   Приблизний результат роботи наступний:
      Red        Green
      Red        Green
      Red        Green
      Red        Green
      Yellow     Green
      Yellow     Green
      Green      Red
      Green      Red
      Green      Red
      Green      Red
      Yellow     Red
      Yellow     Red
      Red        Green
      .......
"""

from time import sleep

light_cars = ['Red', 'Red', 'Red', 'Red', 'Yellow', 'Yellow', 'Green', 'Green', 'Green', 'Green', 'Yellow', 'Yellow']
light_people = ['Green', 'Green', 'Green', 'Green', 'Green', 'Green', 'Red', 'Red', 'Red', 'Red', 'Red', 'Red' ]

while True:
    for i in range(len(light_cars)):
        sleep(1)
        if light_cars[i] == 'Yellow' and light_people[i] == 'Green':
            print(light_cars[i],'   ',light_people[i])
        elif light_cars[i] == 'Green' and light_people[i] == 'Green':
            print(light_cars[i],'       ',light_people[i])
        elif light_cars[i] == 'Yellow' and light_people[i] == 'Red':
            print(light_cars[i],'   ',light_people[i])
        elif light_cars[i] == 'Green' and light_people[i] == 'Red':
            print(light_cars[i],'    ',light_people[i])
        elif light_cars[i] == 'Red' and light_people[i] == 'Green':
            print(light_cars[i],'      ',light_people[i])
