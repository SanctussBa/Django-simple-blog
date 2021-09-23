from django.shortcuts import render, redirect
from .models import Article #import article class from models.py file from the same directory
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . import forms

def article_list(request):
    articles = Article.objects.all().order_by('date')
    return render(request, "articles/article_list.html", {'articles': articles})

def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article':article})

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)# says to not commit it yet because we want to do something first
            instance.author = request.user #it will take the author from request user
            instance.save() #now we can save in database, we grabbed and assigned author above

            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form':form})
