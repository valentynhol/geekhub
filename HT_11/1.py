"""
Написати програму, яка буде робити наступне:
1. Робить запрос на https://jsonplaceholder.typicode.com/users і вертає коротку інформацію про користувачів (ID, ім'я, нікнейм)
2. Запропонувати обрати користувача (ввести ID)
3. Розробити наступну менюшку (із вкладеними пунктами):
   1. Повна інформація про користувача
   2. Пости:
      - перелік постів користувача (ID та заголовок)
      - інформація про конкретний пост (ID, заголовок, текст, кількість коментарів + перелік їхніх ID)
   3. ТУДУшка:
      - список невиконаних задач
      - список виконаних задач
   4. Вивести URL рандомної картинки
"""
import requests
from random import randint


def user_info(id, users):
    for user in users:
        if user['id'] == id:
            print('\n\nID:', user['id'])
            print("Ім'я:", user['name'])
            print('Нікнейм:', user['username'])
            print('Електронна пошта:', user['email'])
            print('Адреса:\n\t',
                  'Вулиця:', user['address']['street'], '\n\t',
                  user['address']['suite'], '\n\t',
                  'Місто:', user['address']['city'], '\n\t',
                  'Код:', user['address']['zipcode'], '\n\t',
                  'Геоадреса:', user['address']['geo'])
            print('Номер телефону:', user['phone'])
            print('Вебсайт:', user['website'])
            print('Компанія:\n\t', user['company']['name'], '\n\t',
                  user['company']['catchPhrase'], '\n\t',
                  user['company']['bs'], '\n\t',)
            print('\n')


def user_posts(user_id):
    posts = requests.get('https://jsonplaceholder.typicode.com/posts').json()

    for post in posts:
        if post['userId'] == user_id:
            print('\n\nID посту:', post['id'])
            print('Заголовок:', post['title'], '\n')
            print('Пост:', post['body'])
            comments = requests.get('https://jsonplaceholder.typicode.com/comments').json()
            print('\nКоментарі: ')
            print('\tID коментарів: ')
            comment_count = 0
            for comment in comments:
                if comment['postId'] == post['id']:
                    comment_count += 1
                    print('\t\t', comment['id'])
            print('\tК-ть:', comment_count)


def user_todos(user_id):
    todos = requests.get('https://jsonplaceholder.typicode.com/posts').json()

    for todo in todos:
        if todo['userId'] == user_id:
            print('ID:', todo['id'])
            print('Назва:', todo['title'])


def random_img():
    images = requests.get('https://jsonplaceholder.typicode.com/photos').json()

    image_id = randint(1, 5000)
    for image in images:
        if image['id'] == image_id:
            print('URL картинки:', image['url'])


users = requests.get('https://jsonplaceholder.typicode.com/users').json()

print("\n\nID     Ім'я                            Нікнейм\n")

for user in users:
    print(user['id'], ' '*(5 - len(str(user['id']))), user['name'], ' '*(30 - len(user['name'])), user['username'])
while True:
    current_user_id = int(input('\n\nВведіть ID користувача (число від 1 до 10): '))
    if not 1 <= current_user_id <= 10:
        print('Не існує такого користувача!')
        exit()

    mode = input('Виберіть режим:\n\t'
                 '(1)Повна інформація про користувача,\n\t'
                 '(2)Пости користувача,\n\t'
                 '(3)Задачі користувача,\n\t'
                 '(4)Рандомна картинка,\n\t'
                 '(0)Вихід\n')
    if mode == '1':
        user_info(current_user_id, users)
    elif mode == '2':
        user_posts(current_user_id)
    elif mode == '3':
        user_todos(current_user_id)
    elif mode == '4':
        random_img()
    else:
        print('До побачення!')
        exit()
    if input('Продовжити? y/n\n') == 'n':
        break
