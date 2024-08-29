from django.urls import path
from cart import views

app_name = 'cart'

urlpatterns = [
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('remove/<int:product_id>/', views.remove_from_cart, name='cart_remove'),
    path('', views.cart_detail, name='cart_detail')
]