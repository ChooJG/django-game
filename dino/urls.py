from django.urls import path
from . import views

app_name = 'dino'

urlpatterns = [
   path('<str:name>/', views.index, name='main'),  # <str:name> 파라미터 받음
   path('<str:name>/game/', views.game, name="game")
]