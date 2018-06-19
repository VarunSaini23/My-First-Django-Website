from django.db import models

# Create your models here.
class Signup(models.Model):
    name=models.CharField(max_length=128)
    username=models.CharField(max_length=128,unique=True)
    email=models.EmailField()
    password=models.CharField(max_length=128)
    def __str__(self):
        return self.username
