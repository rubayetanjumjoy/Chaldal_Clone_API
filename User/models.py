from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone


class UserManager(BaseUserManager):

    def _create_user(self, email, password, is_staff, is_superuser, **extra_fields):

        now = timezone.now()

        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password,phone_numbner, **extra_fields):
        return self._create_user(email, password,phone_numbner, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        user = self._create_user(email, password, True, True, **extra_fields)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=254,null=True, unique=True,blank=True)
    name = models.CharField(max_length=254, null=True, blank=True)
    phone_number=models.CharField(max_length=14, null=True, unique=True,blank=True)
    Gender_Choice = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Other'),

    )
    date_of_birth= models.CharField(max_length=254, null=True, blank=True)
    gender = models.CharField(max_length=6, choices=Gender_Choice, default='',blank=True)
    otp=models.CharField(max_length=14,blank=True)
    is_otp_verified=models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    last_login = models.DateTimeField(null=True, blank=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    password = models.CharField( max_length=128, blank=True, null=True)
    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return str(self.name)

class Address(models.Model):
    address=models.ForeignKey(User,on_delete=models.CASCADE)
    street_address=models.CharField(max_length=200,null=True,blank=True)
    floor_no=models.IntegerField(null=True,blank=True)
    apartment_no=models.CharField(max_length=200,null=True,blank=True)
    def __str__(self):
        return str(self.street_address)





