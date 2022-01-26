"""
Використовуючи бібліотеку requests написати скрейпер для отримання статей / записів із АПІ
Документація на АПІ:
https://github.com/HackerNews/API
Скрипт повинен отримувати із командного рядка одну із наступних категорій:
askstories, showstories, newstories, jobstories
Якщо жодної категорії не указано - використовувати newstories.
Якщо категорія не входить в список - вивести попередження про це і завершити роботу.
Результати роботи зберегти в CSV файл. Зберігати всі доступні поля. Зверніть увагу -
 інстанси різних типів мають різний набір полів.
Код повинен притримуватися стандарту pep8.
Перевірити свій код можна з допомогою ресурсу http://pep8online.com/
Для тих, кому хочеться зробити щось "додаткове" - можете зробити наступне: другим параметром cкрипт може приймати
назву HTML тега і за допомогою регулярного виразу видаляти цей тег разом із усим його вмістом із значення атрибута
"text"(якщо він існує) отриманого запису.
"""
import csv
import sys

import requests


class Process(object):
    loading_dots_counter = 0
    stories_counter = 0

    @staticmethod
    def loading():
        sys.stdout.write('\r\033[1;36m' + 'Loading\033[0m' +
                         ' ' * (Process.loading_dots_counter % 10 + 1))
        sys.stdout.flush()

        Process.stories_counter += 1
        Process.loading_dots_counter += 1

    @staticmethod
    def done():
        sys.stdout.write(f'\r\033[0;42mDone! Found '
              f'{Process.stories_counter} stories.\033[0m\n\n')


class HackerNews(object):
    def get_list(self, category):
        ids = requests.get(f'https://hacker-news.firebaseio.com/v0/'
                           f'{category}.json').json()

        field_dicts = []
        field_names = []

        for id_num in ids:
            stories = self.get_by_id(id_num)
            field_dicts.append(stories)

            Process.loading()

            for field_name in stories.keys():
                if field_name not in field_names:
                    field_names.append(field_name)

        return field_dicts, field_names

    def get_category(self):
        if len(sys.argv) >= 2:
            category = sys.argv[1]
            if category in ['askstories',
                            'showstories',
                            'newstories',
                            'jobstories']:
                return category
            else:
                print('Категорія не входить в список!')
                exit()
        else:
            return 'newstories'

    def get_by_id(self, stories_id):
        stories = requests.get(f'https://hacker-news.firebaseio.com'
                               f'/v0/item/{stories_id}.json').json()
        return stories


hacker_news = HackerNews()
field_dicts, fieldnames = hacker_news.get_list(hacker_news.get_category())

with open('stories.csv', 'a') as f:
    f.truncate(0)
    dict_writer = csv.DictWriter(f, fieldnames=fieldnames)
    dict_writer.writeheader()

    for field_dict in field_dicts:
        dict_writer.writerow(field_dict)

Process.done()
