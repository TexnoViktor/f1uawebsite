from django.shortcuts import render
from .models import Article
from django.views.generic import DetailView

def news(request):
    news_arr = Article.objects.all()

    return render(request, 'news/news.html', {'news_arr': news_arr})


class NewsDetailView(DetailView):
    model = Article
    template_name = 'news/example.html'
    context_object_name = 'article'