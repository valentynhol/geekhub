import requests


class HackerNews(object):
    @staticmethod
    def get_list(category, obj_list):
        ids = requests.get(f'https://hacker-news.firebaseio.com/v0/'
                           f'{category}.json').json()

        field_dicts = []
        scraped_count = 0
        for id_num in ids:
            if id_num not in obj_list:
                stories = HackerNews.__get_by_id(id_num)
                field_dicts.append(stories)
                scraped_count += 1

        return field_dicts, scraped_count

    @staticmethod
    def __get_by_id(stories_id):
        stories = requests.get(f'https://hacker-news.firebaseio.com'
                               f'/v0/item/{stories_id}.json').json()
        return stories
