from django.db import models
from .managers import PersonAdultManager


# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveSmallIntegerField(default=0)
    bio = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    gender = models.CharField(max_length=6)

    objects = models.Manager()
    people = PersonAdultManager()



    def __str__(self):
        return f'{self.name} {self.age}'
