from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class auth(models.Model):
    user = models.ForeignKey(User, null=False, on_delete=models.CASCADE)