from django.db import models

from utils.models import TimeStamp
from utils.utils import PHONE_REGEX


class OtpModel(TimeStamp):
    otp = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=11, validators=[PHONE_REGEX])

    def __str__(self):
        return self.phone_number
    
    class Meta:
        verbose_name = "Otp"
        verbose_name_plural = "Otp"
        db_table = "otp"
