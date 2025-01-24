from django.shortcuts import render

# Create your views here.
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import ArticleForm


class CustomLoginView(LoginView):
    template_name = 'login.html'

# views.py
from django.shortcuts import render
from .models import Article

def home(request):
    articles = Article.objects.all()  # Fetch all articles from the database
    return render(request, 'home.html', {'articles': articles})


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ArticleForm

import logging
logger = logging.getLogger(__name__)

def create_article(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            logger.info(f"Creating article with author: {request.user}")
            article = form.save(commit=False)
            article.author = request.user
            article.save()
            return redirect('home')
        else:
            logger.error(f"Form errors: {form.errors}")
    else:
        form = ArticleForm()
    return render(request, 'create_article.html', {'form': form})




from django.shortcuts import render, get_object_or_404, redirect
from .models import Article
from .forms import ArticleForm

def edit_article(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ArticleForm(instance=article)
    return render(request, 'edit_article.html', {'form': form, 'article': article})
