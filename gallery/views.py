from django.shortcuts import render
from .models import Photos

# Create your views here.
def my_gallery(request):
    photos = Photos.objects.all()
    return render(request, 'gallery.html', {'photos':photos})
