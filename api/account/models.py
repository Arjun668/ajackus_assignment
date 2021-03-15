import uuid

from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.core.validators import RegexValidator

from django.db import models


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):

        # Creates and saves a User with the given email and password.
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        # Create User method called at user registration.
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        # Create superuser method called at superuser creation.
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    # Phone validate - Accept only 10 digit Phone number and its error message
    phone_regex = RegexValidator(
        regex=r'^\+?1?\d{10}$', message=(
            'Phone number should be 10 digit only'
        )
    )

    # Pin code validate - Accept only 6 digit pin code and its error message
    pin_code_regex = RegexValidator(
        regex=r'^\+?1?\d{6}$', message=(
            'Pin code should be 6 digit only'
        )
    )

    # Full name validate - First Name Last Name
    full_name_regex = RegexValidator(
        regex=r'^[a-zA-Z]+ [a-zA-Z]+$', message=(
            'Please enter full name'
        )
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    full_name = models.CharField(max_length=100, validators=[full_name_regex], blank=True)
    email = models.EmailField(max_length=100, unique=True)
    phone = models.CharField(max_length=10, validators=[phone_regex], null=True, blank=True)
    address = models.CharField(max_length=500, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    pin_code = models.CharField(max_length=6, validators=[pin_code_regex])
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    objects = UserManager()

    # Set email is a primary field which is used for login instead of username.
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
