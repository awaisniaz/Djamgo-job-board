
from django.contrib import admin
from django.urls import path
from user import views

urlpatterns = [
    path('signup/',views.register,name="signup"),
    path('login/',views.user_login,name="login"),
    path('logout/',views.logout,name="logout")
]
