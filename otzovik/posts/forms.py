from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'image', 'name']


'''
Создаем форму при создания поста, наследуемую от нашей созданной модели
Название, содержание, картинка и имя кто выложил пост
'''
