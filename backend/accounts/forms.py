from django import forms
# from django.contrib.auth.models import User

class RegisterUserForm(forms.Form):
    username=forms.CharField(max_length=100)
    email=forms.EmailField()
    password=forms.CharField()

# class RegisterUserModelForm(forms.ModelForm):
#     class Meta:
#         model=User
#         fields=('username','email','password')

class LoginUserForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()