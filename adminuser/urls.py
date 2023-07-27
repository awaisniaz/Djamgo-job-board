
from django.contrib import admin
from django.urls import path,include
from adminuser import views
urlpatterns = [
    path('login/', views.login, name="login"),
    path("signup/",views.register,name="signup"),
    path("homepage/",views.home,name="home"),
    path("login_post/",views.login_post,name="login_post"),
    path("register/",views.registerandUpdate,name="register"),
path("dashboard/",views.dashboard,name="dashboard")
]
