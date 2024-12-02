from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.


class User(AbstractUser):
    age = models.IntegerField(null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    image = models.ImageField(upload_to='users_images', null=True, blank=True)

    def __str__(self):
        return self.username


'''
Создаем пользователя на основе AbstractUser с добавлением своих данных:
- возраст;
- город;
- фотография(картинка)
'''
