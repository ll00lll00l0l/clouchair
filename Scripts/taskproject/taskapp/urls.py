
from django.urls import path
from . import views
from django.urls import path
from .views import add_to_cart,  cart
app_name = 'cart'

urlpatterns = [
    path('',views.enter,name='form'),
    path('login',views.login,name='login'),
    path('create',views.add,name='add'),
    path('index',views.index,name='index'),
    path('cart',views.cart,name='cart'),
    path('shop',views.shop,name='shop'),
 
    path('loginuser',views.loginuser,name='loginuser'),
    path('cart/', cart, name='cart'),
    path('add-to-cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('update_quantity/', views.update_quantity, name='update_quantity'),
    path('remove_item/', views.remove_item, name='remove_item'),
]