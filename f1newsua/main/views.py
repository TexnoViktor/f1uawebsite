from django.shortcuts import render
from news.models import Article
# Create your views here.


def index(request):
    news_arr = Article.objects.all()
    photo1 = Article.objects.get(id=1)
    photo2 = Article.objects.get(id=2)
    photo3 = Article.objects.get(id=3)
    photo4 = Article.objects.get(id=4)
    photo5 = Article.objects.get(id=5)
    return render(request, 'main/index.html', {'photo1': photo1, 'photo2': photo2, 'photo3': photo3, 'photo4': photo4, 'photo5': photo5})


def drivers(request):
    return render(request, 'main/drivers.html')


def schedule(request):
    return render(request, 'main/schedule.html')


def standings(request):
    return render(request, 'main/standings.html')


def teams(request):
    return render(request, 'main/teams.html')
