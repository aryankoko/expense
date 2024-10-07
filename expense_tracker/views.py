from rest_framework.decorators import api_view
from rest_framework.response import Response
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# from rest_framework import status
from .serializers import RegisterSerializer

@api_view(['POST'])
def register_view(req):
    newUser = RegisterSerializer(data=req.data)
    if newUser.is_valid():
        newUser.save()
        return Response({'msg':'user created'}, status=200)
    return Response(newUser.errors, status=400)

@api_view(['POST'])
def login_view(req):
    username = req.data.get('username')
    password = req.data.get('password')

    user = authenticate(username=username,password=password)
    if user:
        login(req, user)
        return Response({"message": "Login successful."})
    return Response({"error": "Invalid credentials"}, status=400)

@api_view(['POST'])
def logout_view(request):
    logout(request)
    return Response({"message": "Logged out successfully."})