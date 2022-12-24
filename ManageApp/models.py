from django.db import models


# Create your models here.
class DB(models.Model):
    key = models.CharField(max_length=1024, null=False, blank=False,primary_key=True, unique=True)
    value = models.CharField(max_length=1024, null=False, blank=False)
