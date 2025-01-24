from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
# Create your views here.

def say_hello(request):
    
    return render(request,'hello.html', {'name':'mohith'})

from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Comment
from django.contrib.auth.decorators import login_required



def home(request):
    articles = Article.objects.filter(is_published=True)
    return render(request, 'home.html', {'articles': articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = article.comments.all()
    return render(request, 'article_detail.html', {'article': article, 'comments': comments})


def add_article(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        Article.objects.create(title=title, content=content, author=request.user)
        return redirect('home')
    return render(request, 'add_article.html')
from django.shortcuts import render

def article_list(request):
    return render(request, 'playground/article_list.html')

def add_comment(request, article_id):
    if request.method == 'POST':
        article = get_object_or_404(Article, id=article_id)
        content = request.POST.get('content')
        if not content:
            return HttpResponseBadRequest("Comment content cannot be empty.")
        Comment.objects.create(article=article, content=content, author=request.user)
        return redirect('article_detail', pk=article_id)
    return HttpResponseBadRequest("Invalid request method.")
