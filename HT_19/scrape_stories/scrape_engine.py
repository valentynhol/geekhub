import requests


class HackerNews(object):
    @staticmethod
    def get_list(category):
        ids = requests.get(f'https://hacker-news.firebaseio.com/v0/'
                           f'{category}.json').json()

        field_dicts = []

        for id_num in ids:
            stories = HackerNews.__get_by_id(id_num)
            field_dicts.append(stories)

        return field_dicts

    @staticmethod
    def __get_by_id(stories_id):
        stories = requests.get(f'https://hacker-news.firebaseio.com'
                               f'/v0/item/{stories_id}.json').json()
        return stories
