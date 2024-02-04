from django.shortcuts import render
from django.http import HttpResponse,Http404
from .models import Todo



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

def todos(request):
    all_todos=Todo.objects.all()

    return render(request,'todo.html',{"todos":all_todos})

def todos_detail(request,todo_id):
    todo=Todo.objects.get(id=todo_id)
    
    return render(request,"todo_detail.html",{'todo':todo})