from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager,
)
from django.utils import timezone


# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password, **data):
        if not email:
            raise ValueError("Email field is required!")
        email = self.normalize_email(email=email)
        user = self.model(email=email, **data)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **data):
        data.setdefault("is_staff", True)
        data.setdefault("is_superuser", True)
        return self.create_user(email, password, **data)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=150, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=11, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateField(default=timezone.now)

    objects = UserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email
