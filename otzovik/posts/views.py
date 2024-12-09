from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from .forms import PostForm
from django.core.paginator import Paginator


# Create your views here.


# Новый пост
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = PostForm()
    context = {'form': form}
    return render(request, 'post_form.html', context)  # post_form.html - форма публикации и редактирования


'''
Функция для создания нового поста
Если все данные по форме "PostForm" введены верно, то сохраняем их и публикуем
'''


# Все посты главная страница. Ипользуем пагинацию для того чтобы на страницу отображалось по 3 поста
def index(request):
    posts = Post.objects.all().order_by('-date_create')
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'posts': posts,
               'page_obj': page_obj}
    return render(request, 'index.html', context)


'''
Функция для отображения всех постов которые у нас есть
и чтобы не было на одной страницы много данных, мы разбиваем их по страницам используя "Paginator"
На одной странице отбражается не более 3 постов и отображается от новых к более старым '-date_create'
'''


# Редактирование поста
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:index')
    else:
        form = PostForm(instance=post)
    context = {'form': form}
    return render(request, 'post_form.html', context)


'''
Если вдруг мы что-то ввели нре верно или хотели бы изменить свой пост, для этого используем эту функцию
Форму для редактирования мы используем "PostForm"
После редактирования перенаправляем на главную страницу со всеми постами 
'''