from django.db import models


class users(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    age = models.IntegerField(null=False, blank=False)

# Create your models here.
