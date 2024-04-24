from django.db import models


class users(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    age = models.IntegerField()

# Create your models here.
