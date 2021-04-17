from django.db import models

# Create your models here.
class Product(models.Model):
    objects = models.Manager() #https://stackoverflow.com/questions/45135263/class-has-no-objects-member
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    likes = models.PositiveIntegerField(default=0)

class User(models.Model):
    pass    