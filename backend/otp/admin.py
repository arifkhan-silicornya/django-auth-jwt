from django.contrib import admin

from .models import OtpModel


class OtpModelAdmin(admin.ModelAdmin):
    list_display = (
        "otp",
        "phone_number",
    )
    list_per_page = 25


admin.site.register(OtpModel, OtpModelAdmin)
