from django.shortcuts import render
from django.http import HttpResponse

from django.template import loader
from datetime import datetime


def index(request):
    now = datetime.now()

    context = {
        'current_time' : now
    }
    return render(request, 'main/index.html', context)