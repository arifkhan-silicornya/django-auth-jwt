from rest_framework.serializers import ModelSerializer

from otp.models import OtpModel


class OtpModelSerializer(ModelSerializer):
    class Meta:
        model = OtpModel
        fields = [
            "otp",
            "phone_number",
        ]
        