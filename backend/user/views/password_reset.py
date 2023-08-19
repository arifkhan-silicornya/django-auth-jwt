from django.shortcuts import get_object_or_404

from user.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from utils.utils import tokenValidation


class UserPasswordResetView(APIView):
    """User can reset their password."""

    def patch(self, request):
        payload = tokenValidation(request)
        phone_number = payload["phone_number"]

        new_password = request.data.get("new_password")

        user = get_object_or_404(User, phone_number=phone_number)
        user.set_password(new_password)
        user.save()
        return Response({"detail": "password reset successfully"}, status=status.HTTP_200_OK)
    