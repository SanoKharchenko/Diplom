from django.urls import path
from .views import post_edit, post_create, index

app_name = "posts"

urlpatterns = [
    path('', index, name='index'),
    path('post/', post_create, name='post_create'),
    path('post/edit/<int:pk>/', post_edit, name='post_edit'),
]

'''
Добавляем ссылки на шаблоны которые будем использовать
Импортируем логику из views 
'''