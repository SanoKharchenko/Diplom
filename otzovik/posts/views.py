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


# Все посты главная страница. Ипользуем пагинацию для того чтобы на страницу отображалось по 3 поста
def index(request):
    posts = Post.objects.all().order_by('-date_create')
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'posts': posts,
               'page_obj': page_obj}
    return render(request, 'index.html', context)


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
