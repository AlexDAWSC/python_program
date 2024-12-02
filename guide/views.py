from django.shortcuts import render
from .models import City, Monument, Restaurant, NationalPark, TouristAttraction, Route

def home(request):
    cities = City.objects.all()
    monuments = Monument.objects.all()
    restaurants = Restaurant.objects.all()
    national_parks = NationalPark.objects.all()
    tourist_attractions = TouristAttraction.objects.all()
    routes = Route.objects.all()
    
    return render(request, 'guide/home.html', {
        'cities': cities,
        'monuments': monuments,
        'restaurants': restaurants,
        'national_parks': national_parks,
        'tourist_attractions': tourist_attractions,
        'routes': routes
    })