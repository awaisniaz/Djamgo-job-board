from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse,JsonResponse
from django.db import DatabaseError,IntegrityError
from rest_framework.authtoken.models import Token
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.hashers import make_password
import json
from .models import User
@require_http_methods(["GET"])
def login(request):
   return render(request,'login.html',{})
@require_http_methods(["GET"])
def register(request):
   return render(request,'register.html',{})

@require_http_methods(["GET"])
def home(request):
   return render(request,'home.html',{})
@require_http_methods(["POST"])
def login_post(request):
   email =  request.POST.get("email")
   password = request.POST.get("psw")
   return redirect("/admin_side/homepage")
@require_http_methods(['POST','PATCH'])
def registerandUpdate(request):
   if request.method == 'POST':

      repeatPassword = request.POST.get("psw-repeat")
      email = request.POST.get("email")
      password = request.POST.get("psw")
      print(password)
      if(password != repeatPassword):
         return  JsonResponse({"response":"Sorry Your Password is not match"})
      hash = make_password(password)
      print(hash)
      user = User(email=email,first_name="awaisniaz",last_name="khan",username="awaiskianz")
      try:
         user.set_password(password)
         user.save()
         return JsonResponse({"message":"User register Successully"})
      except IntegrityError as e:
         print("I am Error")
         print(e)
         print(f"Caught exception: {e}")
         error_message = str(e)
         print(error_message)
         error_code = e.args[0] if e.args else None

         # Create a dictionary containing the error information
         error_data = {
            'error': {
               'message': error_message,
               'code': error_code,
            }
         }
         return JsonResponse(error_data)

   else:
      return JsonResponse({"msg":"I am Patch Request"})



def dashboard(request):
   return render(request, 'Dashboard.html', {})
