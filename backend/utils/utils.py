import random
from django.core.validators import RegexValidator

PHONE_REGEX = RegexValidator(
    regex=r"^01[13-9]\d{8}$",
    message="Phone number must be 11 digit & this format: '01*********'",
)

def generate_otp():
    return random.randint(1000, 9999)