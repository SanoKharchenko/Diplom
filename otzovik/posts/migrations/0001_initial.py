# Generated by Django 5.1.3 on 2024-12-02 13:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Название:')),
                ('content', models.TextField(verbose_name='Содержание')),
                ('image', models.ImageField(blank=True, null=True, upload_to='posts_images', verbose_name='Фото\\Картинка:')),
                ('date_create', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]