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


# выход из своей учетной записи
def logout_view(request):
    auth.logout(request)
    return redirect('users:login')
