from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def sayhello(request, name) :
    html = '<h1>Hello, {}!</h1>'.format(name)
    return HttpResponse(html)