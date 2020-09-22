from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    ''' This will include Index page methods '''
    return render(request, 'pages/index.html')


def about(request):
    ''' This will include About page methods '''
    return render(request, 'pages/about.html')

