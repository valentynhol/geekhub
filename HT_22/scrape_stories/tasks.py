import requests

from celery import shared_task
from .models import New, Job, Show, Ask


def __get_by_id(stories_id):
    stories = requests.get(f'https://hacker-news.firebaseio.com'
                           f'/v0/item/{stories_id}.json').json()
    return stories


def add_story(story, category):
    if category == 'newstories':
        model = New
    elif category == 'askstories':
        model = Ask
    elif category == 'jobstories':
        model = Job
    else:
        model = Show

    if category == 'jobstories':
        created = model.objects.get_or_create(by=story['by'] if 'by' in story.keys() else None,
                                              stories_id=story['id'],
                                              score=story['score'] if 'score' in story.keys() else None,
                                              time=story['time'] if 'time' in story.keys() else None,
                                              title=story['title'] if 'title' in story.keys() else None,
                                              type=story['type'] if 'type' in story.keys() else None,
                                              url=story['url'] if 'url' in story.keys() else None,
                                              text=story['text'] if 'text' in story.keys() else None)[1]
    elif category == 'newstories' or category == 'showstories':
        created = model.objects.get_or_create(by=story['by'] if 'by' in story.keys() else None,
                                              descendants=story['descendants'] if 'descendants' in story.keys() else None,
                                              stories_id=story['id'],
                                              score=story['score'] if 'score' in story.keys() else None,
                                              time=story['time'] if 'time' in story.keys() else None,
                                              title=story['title'] if 'title' in story.keys() else None,
                                              type=story['type'] if 'type' in story.keys() else None,
                                              url=story['url'] if 'url' in story.keys() else None,
                                              text=story['text'] if 'text' in story.keys() else None)[1]
    else:
        created = model.objects.get_or_create(by=story['by'] if 'by' in story.keys() else None,
                                              descendants=story['descendants'] if 'descendants' in story.keys() else None,
                                              stories_id=story['id'],
                                              score=story['score'] if 'score' in story.keys() else None,
                                              time=story['time'] if 'time' in story.keys() else None,
                                              title=story['title'] if 'title' in story.keys() else None,
                                              type=story['type'] if 'type' in story.keys() else None,
                                              text=story['text'] if 'text' in story.keys() else None)[1]

    return created


@shared_task
def get_list(category, obj_list):
    ids = requests.get(f'https://hacker-news.firebaseio.com/v0/'
                       f'{category}.json').json()

    for id_num in ids:
        if id_num not in obj_list:
            stories = __get_by_id(id_num)
            add_story(stories, category)
