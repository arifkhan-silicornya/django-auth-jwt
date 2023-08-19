import random
import jwt
from django.core.validators import RegexValidator
from jwt_auth.JWT_SETTINGS import JWT_SETTINGS

from rest_framework.authentication import get_authorization_header

PHONE_REGEX = RegexValidator(
    regex=r"^01[13-9]\d{8}$",
    message="Phone number must be 11 digit & this format: '01*********'",
)

def generate_otp():
    return random.randint(1000, 9999)

def tokenValidation(request):
    token_header = get_authorization_header(request).decode("utf-8")
    token_header_split = token_header.split()
    if token_header_split[0] == "Bearer":
        token = token_header_split[1]
        payload = jwt.decode(
            jwt=token, key=JWT_SETTINGS["SIGNING_KEY"], algorithms=["HS256"]
        )
        return payload
    else:
        return None
    