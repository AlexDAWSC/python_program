from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    description = models.TextField()
    latitude = models.FloatField()
    longitude = models.FloatField()

class Monument(models.Model):
    name = models.CharField(max_length=200)
    location_city = models.CharField(max_length=100, blank=True, null=True)
    location_state = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField(blank=True, null=True)

class Restaurant(models.Model):
    name = models.CharField(max_length=200)
    location_city = models.CharField(max_length=100, blank=True, null=True)
    location_state = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField(blank=True, null=True)
    is_open = models.BooleanField(default=True)

class NationalPark(models.Model):
    name = models.CharField(max_length=200)
    location_city = models.CharField(max_length=100, blank=True, null=True)
    location_state = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    description = models.TextField(blank=True, null=True)

class TouristAttraction(models.Model):
    name = models.CharField(max_length=200)
    location_city = models.CharField(max_length=100)
    location_state = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()
    type = models.CharField(max_length=100)
    description = models.TextField()

class Route(models.Model):
    name = models.CharField(max_length=100)
    latitude = models.FloatField()
    longitude = models.FloatField()