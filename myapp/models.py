from django.db import models

# Create your models here.


class Book(models.Model):

    objects = None
    name = models.CharField(max_length=24)
    age = models.CharField(max_length=24)

    def __str__(self):
        return self.name