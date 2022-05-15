from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import views


app_name = 'bank'
urlpatterns = [
    path('', views.home, name='home'),
    path('exchange_rate/', views.exchange_rate, name='exchange-rate'),
    path('period_exchange_rate/', views.period_exchange_rate, name='period-er'),
    #path('history/', views.history, name='history'),
    #path('settings/', views.settings, name='settings'),

    # Transactions
    path('transactions/<int:transaction_id>', views.transaction_page, name='transaction-page'),
    path('transactions', views.all_transactions, name='all-transactions'),

    # Account
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.user_signup, name='signup'),

    # Bank accounts
    path('bank_accounts/create', views.create_ba, name='create-bank-account'),
    path('bank_accounts/<int:ba_id>', views.ba_page, name='ba-page'),
    path('bank_accounts/edit/<int:ba_id>', views.edit_ba, name='edit-ba'),
    path('bank_accounts/add_money/<int:ba_id>', views.add_money, name='add-money'),
    path('bank_accounts/withdraw_money/<int:ba_id>', views.withdraw_money, name='withdraw-money'),

    # Cards
    path('cards/create', views.create_card, name='create card'),
    path('cards/<int:card_id>', views.card_page, name='card page'),
    path('cards/edit/<int:card_id>', views.edit_card, name='edit card'),
    path('cards/transfer_money/<int:card_id>', views.transfer_money, name='transfer money'),
]

urlpatterns += staticfiles_urlpatterns()
