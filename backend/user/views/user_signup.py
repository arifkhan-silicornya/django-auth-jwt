from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from user.serializer.user_signup import UserSignupSerializer


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
        
        return Response({"detail": "Congrates! User successfully created"}, status=status.HTTP_201_CREATED)
    