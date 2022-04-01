from django.db import models

# Create your models here.
class finance(models.Model):
    Id = models.IntegerField(primary_key=True,auto_created=False)
    UserId = models.IntegerField()
    title = models.TextField(max_length=200)
    body = models.TextField(max_length=200)