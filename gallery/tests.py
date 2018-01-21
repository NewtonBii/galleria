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
