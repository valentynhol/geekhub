from django.urls import path
from . import views


app_name = 'scraper'
urlpatterns = [
    path('logout/', views.user_logout, name='logout'),
    path('login/', views.user_login, name='login'),
    path('edit/<int:product_id>', views.edit_product, name='edit'),
    path('category/<str:category>', views.show_category, name='category'),
    path('product/<int:product_id>', views.product_page, name='product'),
    path('cart/', views.cart, name='cart'),
    path('buy/', views.buy, name='buy'),
    path('', views.shop_site, name='shop'),
]
