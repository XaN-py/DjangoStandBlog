from django.shortcuts import render
from blog.models import Article

# Create your views here.


def index(request):
    articles = Article.objects.all()
    return render(request,'home_app/index.html',{"articles":articles})