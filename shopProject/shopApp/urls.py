from django.urls import path
from . import views


app_name="shopApp"

urlpatterns=[
    path('login/', views.user_login, name="user_login"),
    path('register/',views.register,name="register"),
    path('shop_creator/',views.shop_creator,name="shop_creator"),
]
