
from django.contrib import admin
from django.urls import path,include
from adminuser import views
urlpatterns = [
    path('login/', views.login, name="login"),
    path("signup/",views.register,name="signup"),
    path("home/",views.home,name="home")
]
