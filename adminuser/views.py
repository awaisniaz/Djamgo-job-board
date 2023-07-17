from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import HttpResponse,JsonResponse
import json
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
   return JsonResponse({"email":email,"password":password})
@require_http_methods(['POST','PATCH'])
def registerandUpdate(request):
   if request.method == 'POST':
      repeatPassword = request.POST.get("psw-repeat")
      return JsonResponse({"msg":repeatPassword})
   else:
      return JsonResponse({"msg":"I am Patch Request"})

