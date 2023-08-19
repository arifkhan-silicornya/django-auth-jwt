from django.urls import path

from user.views.user_signup import UserSignupView, UserAccountActivationView

urlpatterns = [
    # http://localhost:8000/user/sign-up/
    path(
        route="sign-up/",
        view=UserSignupView.as_view(),
        name="user-sign-up",
    ),
    
    # http://localhost:8000/user/account-activation/
    path(
        route="account-activation/",
        view=UserAccountActivationView.as_view(),
        name="user-account-activation",
    ),
]
