from django.urls import path, include
from . import views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'products', views.ProductViewSet, basename='products')


app_name = 'scraper'
urlpatterns = [
    path('logout/', views.user_logout, name='logout'),
    path('login/', views.user_login, name='login'),
    path('edit/<int:product_id>', views.edit_product, name='edit'),
    path('category/<str:category>', views.show_category, name='category'),
    path('product/<int:product_id>', views.product_page, name='product'),
    path('cart/', views.cart, name='cart'),
    path('', views.shop_site, name='shop'),
    path('api/', include(router.urls), name='api'),
]
