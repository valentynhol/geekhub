from scraper import celery_app
from django.shortcuts import render
from .tasks import get_list
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

        try:
            task = globals()['task']
        except KeyError:
            globals()['task'] = get_list.delay(category, obj_list)

        success = False
        if globals()['task'].successful():
            del globals()['task']
            success = True

        return render(request, 'select/scrape_category.html', {'done': success,
                                                               'items': model.objects.all(),
                                                               'category': category})

    else:
        return render(request, 'select/scrape_category.html')
