from django.urls import path

from user.views.user_signup import UserSignupView, UserAccountActivationView
from user.views.user_login import UserLoginView
from user.views.password_reset import UserPasswordResetView

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

    # http://localhost:8000/user/login/
    path(
        route="login/",
        view=UserLoginView.as_view(),
        name="user-login",
    ),

    # http://localhost:8000/user/password-reset/
    path(
        route="password-reset/",
        view=UserPasswordResetView.as_view(),
        name="user-password-reset",
    ),
]
