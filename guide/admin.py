from django.contrib import admin
from .models import City, Monument, Restaurant, NationalPark, TouristAttraction

admin.site.register(City)
admin.site.register(Monument)
admin.site.register(Restaurant)
admin.site.register(NationalPark)
admin.site.register(TouristAttraction)
