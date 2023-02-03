from django import views
from django.urls import path,include
from .views import *
urlpatterns = [
    path('',home,name="home"),
    path('login',login,name="login"),
    path('register',register,name="register"),
    path('about',about,name="about"),
    path('kinesin',kinesin,name="kinesin"),
    path('kinesir',kinesir,name="kinesir"),
    path('kinesit',kinesit,name="kinesit"),
    path('mdp',mdp,name="mdp"),

]