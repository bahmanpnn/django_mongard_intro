from django.urls import path
from . import views


urlpatterns = [
    path('register/',views.register_user,name='register-page'),
    path('login/',views.login_user,name='login-page'),
    path('logout/',views.logout_user,name='logout'),

]
