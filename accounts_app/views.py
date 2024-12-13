from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password

from accounts_app.serializers import RegisterSerializer
from accounts_app.models import UserProfile

# Create your views here.


@api_view(["POST"])
def register_api_view(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        email = request.data["email"]
        password = request.data["password"]
        hash_password = make_password(password=password)
        user = get_user_model().objects.create(
            username=email.lower(),
            email=email.lower(),
            password=hash_password,
            first_name=request.data["first_name"],
            last_name=request.data["last_name"],
        )
        if user is not None:
            UserProfile.objects.create(
                user=user,
                first_name=request.data["first_name"],
                last_name=request.data["last_name"],
                phone_number="None",
            )
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
