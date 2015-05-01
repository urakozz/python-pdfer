__author__ = 'yury'
from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    # return HttpResponse('Hello !')
    greetings = [{'when': "ta"}, {"when": "da"}]
    return render(request, 'index.html', {'greetings': greetings})