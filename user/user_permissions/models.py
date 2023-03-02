from django.db import models
from base.constance import Role
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    '''user model '''
    username = models.CharField(max_length=150, blank=True, unique=False)
    email = models.EmailField(max_length=100, unique=True)
    role = models.CharField(max_length=10, choices=Role.choices())
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


class Manufacturer(models.Model):
    ''' manufacturer model '''
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    update_by = models.ForeignKey(User, on_delete=models.CASCADE)
    update_at = models.DateTimeField(auto_now_add=True)
    quantity = models.IntegerField()