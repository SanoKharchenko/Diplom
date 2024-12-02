from django.urls import path
from .views import *

app_name = "users"

urlpatterns = [
    path('registration/', registration, name='registration'),
    path('login/', login_view, name='login'),
    path('profile/', profile, name='profile'),
    path('logout/', logout_view, name='logout'),
]


"""
добавляем страницы к которым будем использовать
"""