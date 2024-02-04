from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home-page'),
    path('hello/',views.hello,name='hello'),
    path('hello_user/',views.hello_user,name='hello-user'),
    path('todos/',views.todos,name='todo-page'),
    path('todos/detail/<int:todo_id>',views.todos_detail,name='todo-detail-page'),
    path('todos/detail/delete/<int:todo_id>',views.todos_delete,name='todo-delete'),

]
