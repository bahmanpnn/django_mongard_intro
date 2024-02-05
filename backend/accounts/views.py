from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import RegisterUserForm


def register_user(request):
    if request.method == 'POST':
        register_form=RegisterUserForm(request.POST)
        if register_form.is_valid():
            
            cd=register_form.cleaned_data
            
            #way1
            # new_user=User(username=cd['username'],email=cd['email'])
            # new_user.set_password(cd['password'])
            # new_user.save()

            #way2
            user=User.objects.create_user(cd['username'],cd['email'],cd['password'])

            # remember that it does not need to save new user and it save auto.
            # if we want to add extra data like firstname after adding; we must save that
            
            user.first_name='user'
            user.save()

            # messages.info/error/warning/debug/success(request,'Todo created successfully','info/error/warning/debug/success')
            messages.add_message(request,messages.SUCCESS,'user created succussfully!!')
            return redirect('home-page')
            

    else:
        register_form=RegisterUserForm()
    return render(request,'accounts/register.html',{'register_form':register_form})
