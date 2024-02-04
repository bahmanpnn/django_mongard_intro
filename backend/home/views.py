from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Todo
from .forms import TodoCreateForm
from django.contrib import messages



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

def todos_delete(request,todo_id):
    todo=Todo.objects.get(id=todo_id).delete()
    messages.add_message(request,messages.WARNING ,'todo deleted succussfully !!')
    # messages.error(request,'todo deleted succussfully!!')

    return redirect('todo-page')
    
def todos_create(request):
    if request.method == "POST":
        todo_form=TodoCreateForm(request.POST)
        if todo_form.is_valid():
            cd=todo_form.cleaned_data
            Todo.objects.create(title=cd['title'],body=cd['body'],created_date=cd['created_date'])
            # messages.info/error/warning/debug(request,'Todo created successfully','success')
            messages.add_message(request,messages.SUCCESS ,"Todo created successfully")
            # messages.success(request,'Todo created successfully','success')
            
            return redirect('todo-page')
    else:
        todo_form=TodoCreateForm()

    return render(request,'todo_create.html',{'todo_form':todo_form})