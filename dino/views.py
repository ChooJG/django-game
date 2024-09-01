from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from datetime import datetime


#dino 게임 메인화면으로 이동
def index(request):
    now = datetime.now()

    context = {
        'current_time' : now
    }
    return render(request, 'dino/index.html', context)


#dino 게임화면으로 이동
def game(request):

    return render(request, 'dino/game.html')