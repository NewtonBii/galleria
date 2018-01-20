from django.db import models
import datetime as dt

# Create your models here.
class Location(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class categories(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Photos(models.Model):
    image = models.ImageField(upload_to = 'photos/', null = True)
    name = models.CharField(max_length=30)
    descripton = models.TextField()
    location_taken = models.ForeignKey(Location)
    category = models.ManyToManyField(categories)
    time_uloaded = models.DateTimeField(auto_now_add=True, null=True)

    @classmethod
    def search_by_title(cls, search_term):
        gallery = cls.objects.filter(descripton__icontains=search_term)
        return gallery
