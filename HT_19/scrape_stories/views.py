from django.shortcuts import render
from .forms import CategorySelector
from .scrape_engine import HackerNews
from django.http import HttpResponseRedirect
from .models import Ask, New, Job, Show
from django.core.exceptions import ObjectDoesNotExist


def select(request):
    if request.method == 'POST':
        category = request.POST['category_dropdown']

        items = HackerNews.get_list(category)

        if category == 'newstories':
            model = New
        elif category == 'askstories':
            model = Ask
        elif category == 'jobstories':
            model = Job
        else:
            model = Show

        for item in items:
            try:
                model.objects.get(stories_id=item['id'])
            except ObjectDoesNotExist:
                model.objects.create(by=item['by'] if 'by' in item.keys() else None,
                                     stories_id=item['id'],
                                     score=item['score'] if 'score' in item.keys() else None,
                                     time=item['time'] if 'time' in item.keys() else None,
                                     title=item['title'] if 'title' in item.keys() else None,
                                     type=item['type'] if 'type' in item.keys() else None,
                                     url=item['url'] if 'url' in item.keys() else None,
                                     text=item['text'] if 'text' in item.keys() else None)

        return render(request, 'done.html', {'count': len(items)})

    else:
        done = False
        dropdown = CategorySelector()
        return render(request, 'select/scrape_category.html', {'dropdown': dropdown})
