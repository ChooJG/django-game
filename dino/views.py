from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from datetime import datetime


#dino 게임 메인화면으로 이동
def index(request, name):
    # name 파라미터를 사용하여 로직 처리
    return render(request, 'dino/index.html', {'name': name})


#dino 게임화면으로 이동
def game(request):

    return render(request, 'dino/game.html')