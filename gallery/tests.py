from django.test import TestCase
import datetime as dt
# Create your tests here.
from .models import Photos, categories, Location

class LocationTestClass(TestCase):
    def setUp(self):
        self.location = Location(name = 'Ngong')

    def test_instance(self):
        self.assertTrue(isinstance(self.location, Location))

    def test_save_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)>0)

    def test_delete_method(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.location.delete_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations)==0)


class CategoriesTestClass(TestCase):
    def setUp(self):
        self.category = categories(name='nature')

    def test_category_instance(self):
        self.assertTrue(isinstance(self.category, categories))

    def test_save_category_method(self):
        self.category.save_category()
        categories_object = categories.objects.all()
        self.assertTrue(len(categories_object)>0)
    def test_delete_category_method(self):
        self.category.save_category()
        categories_object = categories.objects.all()
        self.category.delete_category()
        categories_object = categories.objects.all()
        self.assertTrue(len(categories_object)==0)

class PhotosTestClass(TestCase):
    def setUp(self):
        self.photo = Photos(image='imageurl', name='nature', descripton='the beautiful nature')

    def test_photo_instance(self):
        self.assertTrue(isinstance(self.photo, Photos))

    def test_save_photo_method(self):
        self.photo.save_image()
        photos = Photos.objects.all()
        self.assertTrue(len(photos)>0)

    def test_delete_photo_method(self):
        self.photo.save_image()
        photos = Photos.objects.all()
        self.photo.delete_image()
        photos = Photos.objects.all()
        self.assertTrue(len(photos)==0)
