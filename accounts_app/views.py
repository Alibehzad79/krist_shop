from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.hashers import get_random_string
from config import settings


from accounts_app.serializers import RegisterSerializer, EmailVerificationSerializer
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
            verification_code = get_random_string(4).upper()
            UserProfile.objects.create(
                user=user,
                first_name=request.data["first_name"],
                last_name=request.data["last_name"],
                phone_number="None",
                email_verification_code=verification_code,
            )
            send_mail(
                "Verify Account",
                f"{verification_code}",
                settings.DEFAULT_FROM_EMAIL,
                [user.email],
                fail_silently=False,
            )
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["POST"])
def email_verification(request):
    serializer = EmailVerificationSerializer(data=request.data)
    if serializer.is_valid():
        user = UserProfile.objects.get(user__email=request.data["email"])
        if user.email_verification_status:
            return Response(
                data={"msg": "Email already verified."},
                status=status.HTTP_208_ALREADY_REPORTED,
            )
        if user.email_verification_code == request.data["code"]:
            user.email_verification_status = True
            user.email_verification_code = "verifid"
            user.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(
            data={"msg": "Code Invalid."}, status=status.HTTP_400_BAD_REQUEST
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
