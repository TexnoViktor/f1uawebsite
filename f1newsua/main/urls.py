from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('drivers', views.drivers),
    path('teams', views.teams),
    path('schedule', views.schedule),
    path('standings', views.standings),
]