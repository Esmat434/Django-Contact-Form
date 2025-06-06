from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    avatar = models.ImageField(upload_to='images')
    phone_number = models.CharField(max_length=100,blank=True)
    birth_date = models.DateField(blank=True,null=True)

    def __str__(self):
        return self.username