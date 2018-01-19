from django.contrib import admin
from .models import Photos, Location, categories

# Register your models here.
admin.site.register(Photos)
admin.site.register(Location)
admin.site.register(categories)
