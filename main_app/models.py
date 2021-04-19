from django.db import models

# Create your models here.
class todo(models.Model):
    task = models.TextField()

    def __str__(self):
        return str.task