from django.shortcuts import render
from .scrape_engine import HackerNews
from .models import Ask, New, Job, Show


def select(request):
    if request.method == 'POST':
        category = request.POST['category_dropdown']

        if category == 'newstories':
            model = New
        elif category == 'askstories':
            model = Ask
        elif category == 'jobstories':
            model = Job
        else:
            model = Show

        obj_list = []
        for i in model.objects.all():
            obj_list.append(i.stories_id)

        items, scraped_count = HackerNews.get_list(category, obj_list)

        created_count = 0
        for item in items:
            if category == 'jobstories':
                created = model.objects.get_or_create(by=item['by'] if 'by' in item.keys() else None,
                                                      stories_id=item['id'],
                                                      score=item['score'] if 'score' in item.keys() else None,
                                                      time=item['time'] if 'time' in item.keys() else None,
                                                      title=item['title'] if 'title' in item.keys() else None,
                                                      type=item['type'] if 'type' in item.keys() else None,
                                                      url=item['url'] if 'url' in item.keys() else None,
                                                      text=item['text'] if 'text' in item.keys() else None)[1]
            elif category == 'newstories' or category == 'showstories':
                created = model.objects.get_or_create(by=item['by'] if 'by' in item.keys() else None,
                                                      descendants=item['descendants'] if 'descendants' in item.keys() else None,
                                                      stories_id=item['id'],
                                                      score=item['score'] if 'score' in item.keys() else None,
                                                      time=item['time'] if 'time' in item.keys() else None,
                                                      title=item['title'] if 'title' in item.keys() else None,
                                                      type=item['type'] if 'type' in item.keys() else None,
                                                      url=item['url'] if 'url' in item.keys() else None,
                                                      text=item['text'] if 'text' in item.keys() else None)[1]
            else:
                created = model.objects.get_or_create(by=item['by'] if 'by' in item.keys() else None,
                                                      descendants=item['descendants'] if 'descendants' in item.keys() else None,
                                                      stories_id=item['id'],
                                                      score=item['score'] if 'score' in item.keys() else None,
                                                      time=item['time'] if 'time' in item.keys() else None,
                                                      title=item['title'] if 'title' in item.keys() else None,
                                                      type=item['type'] if 'type' in item.keys() else None,
                                                      text=item['text'] if 'text' in item.keys() else None)[1]

            if created:
                created_count += 1

        if items:
            last_item = items[len(items)-1]['id']
        else:
            last_item = None

        return render(request, 'done.html', {'count': len(items),
                                             'items': [created_item['id'] for created_item in items],
                                             'last_item': last_item})

    else:
        return render(request, 'select/scrape_category.html')
