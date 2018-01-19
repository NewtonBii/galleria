from django.db import models

# Create your models here.
class Photos(models.Model):
    image = models.ImageField(upload_to = 'photos/')
    name = models.CharField(max_length=30)
    descripton = models.TextField()
    location_taken = models.ForeignKey(Location)
    category = models.ForeignKey(Category)

class Location(models.Model):
    name = models.CharField(max_length=50)

class Category(models.Model):
    name = models.CharField(max_length=50)
