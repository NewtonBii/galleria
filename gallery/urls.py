from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
 url(r'^$', views.my_gallery, name='myGallery'),
 url(r'^photo/(\d+)', views.single_photo, name = 'myPhoto'),
 url(r'^search/', views.search_results, name = 'search_results'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
