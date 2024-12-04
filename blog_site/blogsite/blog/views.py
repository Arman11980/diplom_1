from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse

#функция запрашивает из базы данных все опубликованные статьи
def home(request):
    posts = Post.objects.all() # получаем все записи
    return render(request, 'home.html', {'posts': posts}) # возвращаем отображение их в шаблоне

#функция для создания поста
def new_post(request):
    if request.method == "POST": #форма была отправлена на сохранение
        form = PostForm(request.POST, files=request.FILES)
        if form.is_valid(): # проверка на валидацию
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('home')
    else:
        form = PostForm()
    return render(request, "new_post.html", {'form': form})

#функция для ввода комментариев к посту
def post_details(request, slug):
    post = Post.objects.get(slug=slug)
    comments = Comment.objects.order_by("-created_on")
    new_comment = None
    if request.method == "POST":
        form = CommentForm(request.POST or None)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return render(request, "add_comment.html")
    else:
        form = CommentForm()
    return render(request, "add_comment.html", {'form': form, 'post': post, 'comments': comments, 'new_comment': new_comment})

#функция для удаления записей в блоге
def delete_post(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == "POST":
        post.delete()
        return redirect("home")
    return render(request, 'delete.html', {'post': post})



