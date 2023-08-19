from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser, 
    BaseUserManager, 
    PermissionsMixin,
)

from utils.utils import PHONE_REGEX


class UserManager(BaseUserManager):
    """Manager for users."""

    def create_user(self, phone_number, email, password=None, **extra_fields):
        """Create, save and return a new user"""

        if not phone_number:
            raise ValueError("Phone number is required!")
        
        user = self.model(
            phone_number=phone_number,
            email=self.normalize_email(email),
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)

        return user
    
    def create_superuser(self, phone_number, email, password):
        """Create and return a new superuser."""

        user = self.create_user(phone_number=phone_number, email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """User in the system."""

    phone_number = models.CharField(max_length=11, validators=[PHONE_REGEX], unique=True)
    email = models.EmailField(max_length=255)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)

    class Gender(models.TextChoices):
        male = "male"
        female = "female"
        others = "others"
    gender = models.CharField(max_length=10, choices=Gender.choices, default=None, null=True, blank=True)
    country = models.CharField(max_length=100, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        db_table = "user"
        