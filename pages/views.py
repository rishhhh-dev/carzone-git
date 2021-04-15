from django.shortcuts import render
from .models import Team
from cars.models import cars
# Create your views here.

def Home(request):
    teams = Team.objects.all()
    featured_cars = cars.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = cars.objects.order_by('-created_date')
    data={
        'teams':teams,
        'featured_cars':featured_cars,
        'all_cars':all_cars,
    }
    return render(request,'templates/pages/home.html',data)


def About(request):
    teams = Team.objects.all()
    data = {
        'teams':teams,
    }
    return render(request,'templates/pages/about.html',data)


def services(request):
    return render(request,'templates/pages/services.html')

def contact(request):
    return render(request,'templates/pages/contact.html')
