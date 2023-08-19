from rest_framework.serializers import ModelSerializer

from user.models import User


class UserSignupSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = [
            "phone_number",
            "email",
            "first_name",
            "last_name",
            "gender",
            "country",
            "password",
        ]
        