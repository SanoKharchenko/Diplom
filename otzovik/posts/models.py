from django.db import models
from users.models import User


# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=250, verbose_name='Название:')
    content = models.TextField(verbose_name='Содержание')
    image = models.ImageField(upload_to='posts_images', null=True, blank=True, verbose_name='Фото\Картинка:')
    name = models.ForeignKey(User, on_delete=models.CASCADE)
    date_create = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


'''
Создаем модель для поста
содержит в себе :
Название(title)
Описание(content)
Картинку или фотографию(image)
Имя,кто опубликовал статью(name)
Дата создания(data_create)
'''
