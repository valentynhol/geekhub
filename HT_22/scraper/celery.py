import django
import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scraper.settings')

django.setup()
app = Celery('scrape_stories', backend='rpc://', broker='amqp://')
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


