from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import login,logout,authenticate
from user.serializer import User_Serilalizerr

# Create your views here.

@api_view(['POST'])
def register(request):
    serializer = User_Serilalizerr(data=request.data)
    if(serializer.is_valid()):
        user = serializer.save()
        token = Token.objects.create(user=user)
        return  Response({"token":token.key},status = status.HTTP_201_CREATED)
    return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def user_login(request):
    username = request.data.get('username')
    password = request.data.get('password')
    print(username)
    print(password)
    user = authenticate(request,email = username,password=password)
    print(user)
    if user is None:
        try:
          login(request,user)
          request.session.modified = True
          token, _ = Token.objects.get_or_create(user=user)
          return Response({'token': token.key})
        except:
          return Response("Something went wrong",status=status.HTTP_401_UNAUTHORIZED)

    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
def user_logout(request):
    logout(request)
    return Response('You logout Successfully',status=status.HTTP_200_OK)
