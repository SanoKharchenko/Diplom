from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
from .models import User


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100, label='Введите имя пользователся')
    password = forms.CharField(min_length=8, label='Введите пароль')

    class Meta:
        model = User
        fields = ('username', 'password')


'''
Форма для заполнения при входе пользователя
Заполняется: Имя пользлвателя и пароль
За основу взята форма авторизации AuthenticationForm
В классе Meta указываем те данные которые нам необходимы для заполнеия
'''


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=100, label='Ваше имя:')
    last_name = forms.CharField(max_length=100, label='Ваша фамилия:')
    username = forms.CharField(max_length=100, label='Имя пользователя')
    email = forms.EmailField(label='Введите email')
    password1 = forms.CharField(min_length=8, label='Введите пароль')
    password2 = forms.CharField(min_length=8, label='Повторите пароль')
    age = forms.CharField(max_length=3, min_length=2, label='Ваш возраст')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email', 'password1', 'password2', 'age')


'''
Форма регистрации пользователя
Заполняются неоходимые поля: Имя, Фамилия, Имя пользователя, электронная почта, возраст и пароль
Наследуемся от UserCreationForm
В классе Meta берем данные для заполнения котторые нам необходимы

'''


class UserProfileForm(UserChangeForm):
    first_name = forms.CharField(max_length=100, label='Изменить имя:')
    last_name = forms.CharField(max_length=100, label='Изменить фамилию:')
    username = forms.CharField(max_length=100, label='Изменить имя пользователя:')
    image = forms.ImageField(label='Изменить аватар')
    email = forms.EmailField(label='Изменить почту:')
    age = forms.CharField(max_length=3, min_length=2, label='Изменить возраст:')
    city = forms.CharField(max_length=100, label='Изменить город:')

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'image', 'email', 'age', 'city')


'''
Создаем форму профиля
Будут отбражаться и изменяться данные пользователя
Можно изменить Имя, Фамилию, Имя пользователя, изменить фотографию, возраст, город
Наследовались от UserChangeForm
'''