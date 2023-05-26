from django.shortcuts import render
# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def drivers(request):
    return render(request, 'main/drivers.html')


def schedule(request):
    return render(request, 'main/schedule.html')


def standings(request):
    return render(request, 'main/standings.html')


def teams(request):
    return render(request, 'main/teams.html')
