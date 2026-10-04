from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import News
from .forms import RegisterForm, NewsForm

# Public Views
def news_list(request):
    articles = News.objects.all()
    return render(request, 'news/news_list.html', {'articles': articles})

def news_detail(request, pk):
    article = get_object_or_404(News, pk=pk)
    return render(request, 'news/news_detail.html', {'article': article})

# Auth Views
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('news_list')
    else:
        form = RegisterForm()
    return render(request, 'news/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('news_list')
    else:
        form = AuthenticationForm()
    return render(request, 'news/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('news_list')

# CRUD Views (Login Required)
@login_required
def news_create(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news = form.save(commit=False)
            news.author = request.user
            news.save()
            return redirect('news_list')
    else:
        form = NewsForm()
    return render(request, 'news/news_form.html', {'form': form, 'title': 'Create News Article'})

@login_required
def news_update(request, pk):
    article = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('news_detail', pk=article.pk)
    else:
        form = NewsForm(instance=article)
    return render(request, 'news/news_form.html', {'form': form, 'title': 'Edit Article'})





@login_required
def news_delete(request, pk):
    article = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('news_list')
    return render(request, 'news/news_confirm_delete.html', {'article': article})