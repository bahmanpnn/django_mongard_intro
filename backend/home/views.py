from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def home(request):
#     return HttpResponse('this is home page :))')

def home(request):
    return render(request,'home.html')

def hello(request):
    return HttpResponse('hello user :)))')


def hello_user(request):
    person={'name':'bahman','last_name':'pournazari'}

    # return render(request,'hello.html',{'name':'bahman','last_name':'pournazari'})
    # return render(request,'hello.html',person)
    return render(request,'hello.html',context=person)