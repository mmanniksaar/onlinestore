from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from location_field.models.plain import PlainLocationField



class MyAccountManager(BaseUserManager):
    # Create normal user
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
        )

        user.set_password(password)
        user.save(using = self._db)
        return user

    # Create superuser
    def create_superuser(self, first_name, last_name, email, username,  password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using = self._db)
        return user

class Account(AbstractBaseUser):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=50)
 #   user_image = models.ImageField(upload_to='photos/user_img/', blank=True, verbose_name='User image')

    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)

    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    city = models.CharField(max_length=255, default= 'PORVOO')
    location = PlainLocationField(based_fields=['city'], zoom=7, default= '12')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = MyAccountManager()

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, add_label):
        return True


# from django import forms
# from django.contrib.gis.geos import Point
# 
# from location_field.forms.plain import PlainLocationField
# 
# 
# class Address(forms.Form):
#     city = forms.CharField()
#     location = LocationField(based_fields=['city'], initial=Point(-49.1607606, -22.2876834))