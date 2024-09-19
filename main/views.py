from django.http import HttpResponse

from django.template import loader
from datetime import datetime

from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import User


#메인화면으로 이동
def index(request):
    now = datetime.now()

    context = {
        'current_time' : now
    }
    return render(request, 'main/index.html', context)







