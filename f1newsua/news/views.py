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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = self.get_object()
        text_length = len(obj.full_text)
        half_length = text_length // 2
        first_half_text = obj.full_text[:half_length]
        second_half_text = obj.full_text[half_length:]
        context['first_half_text'] = first_half_text
        context['second_half_text'] = second_half_text
        return context