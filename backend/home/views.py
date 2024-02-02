from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('this is home page :))')

def hello(request):
    return HttpResponse('hello user :)))')