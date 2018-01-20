from django.shortcuts import render, Http404
from .models import Photos

# Create your views here.
def my_gallery(request):
    photos = Photos.objects.all()
    return render(request, 'gallery.html', {'photos':photos})

def single_photo(request, photo_id):
    photo = Photos.objects.get(id=photo_id)
    return render(request, 'photo.html', {'photo':photo})

def search_results(request):
    if 'photos' in request.GET and request.GET['photos']:
        search_term = request.GET.get('photos')
        searched_photo = Photos.search_by_title(search_term)
        message = f"{search_term}"
        return render(request, 'search.html', {"message":message, "photos":searched_photo})
    else:
        message = 'You haven\'t searched for any photos.'
        return render(request, 'search.html', {"message":message})
