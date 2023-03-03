from django.db import models
from base.constance import Role
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    '''user model '''
    username = models.CharField(max_length=150, blank=True, unique=False)
    email = models.EmailField(max_length=100, unique=True)
    role = models.CharField(max_length=10, choices=Role.choices())
    is_deleted = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def soft_delete(self):
        '''soft delete funcction'''
        self.is_deleted= True
        self.save()

class Manufacturer(models.Model):
    ''' manufacturer model '''
    name = models.CharField(max_length=100)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="creat")
    create_at = models.DateTimeField(auto_now_add=True)
    update_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="update_by")
    update_at = models.DateTimeField(auto_now=True)
    quantity = models.IntegerField()