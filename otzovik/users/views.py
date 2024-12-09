from django.shortcuts import render, redirect
from django.contrib import auth
from .forms import UserRegistrationForm, UserProfileForm


# Create your views here.


# регистрация пользователя
def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth.login(request, user)
            return redirect('users:profile')
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'registration.html', context)


'''
Функция для регистрации пользователя
Форму для регистрацию используем которую прописали в UserRegistrationForm
Если все данные введены верно, то сохраняем пользователя и происходит вход в учетную запись "auth.login",
перенаправляем на страницу пользователя
'''


# вход пользователя
def login_view(request):
    error = {}
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('users:profile')
        else:
            error = 'Неверное имя пользователя или пароль'

    return render(request, 'login.html', {'error': error})


'''
Функция для входа пользователя
Получаем ответ вводимых данных методом 'POST'
Если пользователь с такими данными найден проходит аутентификация (auth.authenticate) данных и 
затем вход в учетную запись (auth.login). Перенапрявляем на страницу профиля если все верно
Если данные не верны, выдаем ошибку
'''


# профиль пользователя
def profile(request):
    user = request.user
    if request.method == 'POST':
        form = UserProfileForm(instance=user, data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('users:profile')
    else:
        form = UserProfileForm(instance=user, files=request.FILES)
    context = {'form': form}
    return render(request, 'profile.html', context)


'''
Функция страницы пользователя и редактирования в ней данных
Если пользователь найден, то по форме UserProfileForm открываем данные для редактирования
Когда данные будут введены верно, сохраняем их
'''


# выход из своей учетной записи
def logout_view(request):
    auth.logout(request)
    return redirect('users:login')


'''
Функция необходима для выхода из профиля
в auth.logout реализованы необходимый метод
'''
