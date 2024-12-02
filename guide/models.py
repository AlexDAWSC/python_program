from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

class Monument(models.Model):
    name = models.CharField(max_length=100)
    location_city = models.CharField(max_length=100)
    location_state = models.CharField(max_length=100)
    description = models.TextField()

class Restaurant(models.Model):
    name = models.CharField(max_length=100)
    location_city = models.CharField(max_length=100)
    location_state = models.CharField(max_length=100)
    is_open = models.BooleanField(default=True)
    description = models.TextField()

class NationalPark(models.Model):
    name = models.CharField(max_length=100)
    location_city = models.CharField(max_length=100)
    location_state = models.CharField(max_length=100)
    description = models.TextField()

class TouristAttraction(models.Model):
    name = models.CharField(max_length=100)
    location_city = models.CharField(max_length=100)
    location_state = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    description = models.TextField()
