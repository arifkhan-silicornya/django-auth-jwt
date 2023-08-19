from django.urls import path

from user.views.user_signup import UserSignupView

urlpatterns = [
    path(
        route="sign-up/",
        view=UserSignupView.as_view(),
        name="user-sign-up",
    )
]
