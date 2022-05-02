from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views


app_name = 'bank'
urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.user_signup, name='signup'),
    path('cards/create', views.create_card, name='create card'),
    path('bank_accounts/create', views.create_ba, name='create bank account'),
    path('bank_accounts/<int:ba_id>', views.ba_page, name='ba page'),
    path('cards/<int:card_id>', views.card_page, name='card page'),
    path('cards/edit/<int:card_id>', views.edit_card, name='edit card'),
    #path('history/', views.history, name='history'),
    #path('settings/', views.settings, name='settings'),
]

urlpatterns += staticfiles_urlpatterns()
