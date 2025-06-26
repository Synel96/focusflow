from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings

class UserProfileManager(BaseUserManager):
    

    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)
        user = self.model(email=email, user_name=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        return self.create_user(email, username, password, **extra_fields)
        


class Users(AbstractBaseUser,PermissionsMixin):
    id = models.BigAutoField(primary_key=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(unique=True, max_length=255)
    username = models.CharField(unique=True, max_length=255)
    is_staff = models.BooleanField(blank=True, default=False)
    is_superuser = models.BooleanField(blank=True, default=False)
    is_active = models.BooleanField(blank=True, default=True)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    

    class Meta:
        managed = False
        db_table = 'users'



class Categories(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    user = models.ForeignKey(Users, models.SET_NULL, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'categories'


class Todos(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    is_done = models.IntegerField(blank=True, null=True)
    category = models.ForeignKey(Categories, models.SET_NULL, blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    priority = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, related_name='todos', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'todos'