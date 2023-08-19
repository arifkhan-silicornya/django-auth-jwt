from django.contrib import admin

from .models import User


class UserAdmin(admin.ModelAdmin):
    list_display = (
        "phone_number",
        "email",
        "first_name",
        "last_name",
        "gender",
        "country",
        "is_active",
    )
    list_display_links = (
        "phone_number",
        "email",
        "country",
    )
    search_fields = (
        "phone_number",
        "email",
        "country",
    )
    list_per_page = 25


admin.site.register(User, UserAdmin)
