from django.urls import path
from . import views


urlpatterns = [
   path('', views.index, name='dino-main'),
   path('game/', views.game, name="dino-game")
]