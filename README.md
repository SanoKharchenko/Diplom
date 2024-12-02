# Diplom
Сайт для отзывов на Django
# Сайт для отзывов создан на Django
Место где вы можите оставить свой отзыв о том или ином будь-то товар или услуга
## Описание
Сайт на котором можно оставить,если вы зарегистрированы, отзыв и прочитать отзывы могут все желающие

### Главная страница
На ней отображается последние три отзыва от пользователей. А так же возможность зарегистрироваться на сайтк или войти в свой аккаунт

![glavnaya_str](\Users\Александр\Downloads\2024-12-02_17-39-52.png) 

### Страница регистрации учетной записи
![registration](\Users\Александр\Downloads\2024-12-02_17-41-55.png)
Необходимо указать данные:
* Имя пользователя
* Имя
* Фамилию
* Пароль 
* Возраст

### Страница входа в учетную запись
![login](\Users\Александр\Downloads\2024-12-02_17-45-49.png)

Для входа указываем:
* Имя пользователя
* Пароль

### Страница пользователя
![profil](\Users\Александр\Downloads\2024-12-02_17-46-55.png)

### Страница слдя создания нового отзыва
![new_post](\Users\Александр\Downloads\2024-12-02_18-55-52.png)

## Установка
1. Клонировать репозиторий:

```
git clone https://github.com/SanoKharchenko/Diplom
cd otzovik
```

2. Открыть проект в редакторе
3. Установить библиотеки:
 ```
 pip install -r requirements.txt
  ```

4. При желании создать суперпользователя для администрирования
```
 python manage.py createsuperuser
 ```
5. Запустить сервер:
```
 python manage.py runserver
 ```
 6. Открыть браузер и перейти по адресу:
 http://127.0.0.1:8000/
 Запустится локальный сервер

 ## Структура проекта
 ```
 otzovik
 |-media
 |  |-posts_images
 |  |-users_images
 |-otzovik
 |  |-__init__.py
 |  |-asgi.py
 |  |-settings.py
 |  |-urls.py
 |  |-wsgi.py
 |-posts
 |  |-templates
 |  |  |-base.html
 |  |  |-index.html
 |  |  |-post_form.html
 |  |-__init__.py
 |  |-admin.py
 |  |-apps.py
 |  |-forms.py
 |  |-models.py
 |  |-tests.py
 |  |-urls.py
 |  |-views.py
 |-static
 |  |-css
 |  |  |-style.css
 |  |-media
 |  |  |-no_image.png
 |  |  |-user-icon.png
 |-users
 |  |-templates
 |  |  |-login.html
 |  |  |-profile.html
 |  |  |-registration.html
 |  |-admin.py
 |  |-apps.py
 |  |-forms.py
 |  |-models.py
 |  |-tests.py
 |  |-urls.py
 |  |-views.py
 |-db.sqlite3
 |-manage.py
 |-requirements.txt
 ```
 ## Ссылки
 * http://127.0.0.1:8000/ - Главная страница
 * http://127.0.0.1:8000/users/registration/ -Страница регистрации
 * http://127.0.0.1:8000/users/login/ - Вход в профиль
 * http://127.0.0.1:8000/users/profile/ - Страница профиля
 * http://127.0.0.1:8000/post/ - Страница для создания нового отзыва
 * http://127.0.0.1:8000/post/edit/ - Страница редактирования отзыва
 * http://127.0.0.1:8000/admin/ - Страница администратора
 ___
 ### Спасибо за внимание!