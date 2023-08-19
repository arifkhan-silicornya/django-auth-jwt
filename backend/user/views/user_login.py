from rest_framework_simplejwt.views import TokenObtainPairView

from user.serializer.user_login import UserLoginSerializer


class UserLoginView(TokenObtainPairView):

    serializer_class = UserLoginSerializer