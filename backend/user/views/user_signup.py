from django.core.mail import send_mail
from django.shortcuts import get_object_or_404
from jwt_auth import settings

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from user.serializer.user_signup import UserSignupSerializer
from otp.serializers import OtpModelSerializer
from utils.utils import generate_otp
from otp.models import OtpModel
from user.models import User


class UserSignupView(APIView):
    """User can sign-up for new account."""

    def post(self, request):
        phone_number = request.data.get("phone_number")
        email = request.data.get("email")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")
        gender = request.data.get("gender")
        country = request.data.get("country")
        password = request.data.get("password")

        user_info = {
            "phone_number": phone_number,
            "email": email,
            "first_name": first_name,
            "last_name": last_name,
            "gender": gender,
            "country": country,
            "password": password,
        }

        serializer = UserSignupSerializer(data=user_info)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        otp = generate_otp()
        otp_info = {
            "otp": otp,
            "phone_number": phone_number,
        }
        otp_serializer = OtpModelSerializer(data=otp_info)
        otp_serializer.is_valid(raise_exception=True)
        otp_serializer.save()

        send_mail(
                "Account Activation",
                f"Your OTP: {otp}",
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False
            )
        
        return Response({"detail": "Congrates! User successfully created"}, status=status.HTTP_201_CREATED)
    

class UserAccountActivationView(APIView):
    """User can activate their account."""

    def patch(self, request):
        otp = request.data.get("otp")
        phone_number = request.data.get("phone_number")

        otp_obj = get_object_or_404(OtpModel, otp=otp, phone_number=phone_number)
        
        if otp_obj:
            user = get_object_or_404(User, phone_number=phone_number)
            user.is_active = True
            user.save()
            return Response({"Account activation successfully!"}, status=status.HTTP_200_OK)
