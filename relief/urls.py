from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('distribute_aid/', views.distribute_aid, name='distribute_aid'),
]
