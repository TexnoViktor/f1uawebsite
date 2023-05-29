from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='home'),
    path('drivers', views.drivers, name='drivers'),
    path('teams', views.teams, name='teams'),
    path('schedule', views.schedule, name='schedule'),
    path('standings', views.standings, name='standings'),
]