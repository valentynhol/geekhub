from django.urls import path
from . import views


app_name = 'scraper'
urlpatterns = [
    path('', views.select, name='start'),
]
