from datetime import timedelta
from django.utils import timezone
from django.core.mail import send_mail

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from jwt_auth import settings

from user.models import User
from otp.models import OtpModel
from otp.serializers import OtpModelSerializer
from utils.utils import generate_otp


class UserForgotPasswordOtpView(APIView):
    """Send otp to user when they forgot password."""

    def post(self, request):
        email = request.data.get("email")
        phone_number = request.data.get("phone_number")
        user = get_object_or_404(User, phone_number=phone_number, email=email)
        if user:
            otp = generate_otp()
            send_mail(
                "Forgot Password",
                f"Your OTP: {otp}",
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False
            )
            otp_info = {
                "otp": otp,
                "phone_number": phone_number
            }
            serializer = OtpModelSerializer(data=otp_info)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({"detail": "Otp send successfully"})
        

class UserResetPasswordView(APIView):
    """User can reset their password."""

    def patch(self, request):
        otp = request.data.get("otp")
        phone_number = request.data.get("phone_number")
        new_password = request.data.get("new_password")

        user_otp_info = get_object_or_404(OtpModel, otp=otp, phone_number=phone_number)
        
        if user_otp_info:
            otp_created_at_after_two_minuites = user_otp_info.created_at+timedelta(minutes=2)
            present_time = timezone.now()
            if otp_created_at_after_two_minuites > present_time: 
                user = get_object_or_404(User, phone_number=phone_number)
                user.set_password(new_password)
                user.save()
                user_otp_info.delete()
                return Response({"detail": "password change successfully"})
            else:
                return Response({"detail": "Timeout"})
            