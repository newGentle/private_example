from django.db import models

# Create your models here.

class upload_file(models.Model):
    file = models.FileField(upload_to='files/')
    word = models.CharField(max_length=64)