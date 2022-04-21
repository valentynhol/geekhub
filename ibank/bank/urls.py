from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views


app_name = 'bank'
urlpatterns = [
    path('', views.home, name='home'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.user_signup, name='signup'),
    #path('history/', views.history, name='history'),
    #path('settings/', views.settings, name='settings'),
]

urlpatterns += staticfiles_urlpatterns()
