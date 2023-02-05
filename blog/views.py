from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Article
# Create your views here.


def article(request):
    articles = Article.objects.all()
    number = request.GET.get("page")
    print(number)
    paginator = Paginator(articles,1)
    object_list = paginator.get_page(number)
    return render(request, 'blog/article.html', {"articles":object_list})