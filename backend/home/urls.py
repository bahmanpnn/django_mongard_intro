from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home-page'),
    path('hello/',views.hello,name='hello'),
    path('hello_user/',views.hello_user,name='hello-user'),

]
