from django.shortcuts import render
from .models import PredefinedCity
import requests

def get_weather_data(city, api_key):
    api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(api_url).json()
    if response.get('main'):
        return {
            'city': city,
            'temperature': response['main']['temp'],
            'description': response['weather'][0]['description'],
            'icon': response['weather'][0]['icon'],
        }
    return None

def index(request):
    weather_data = None
    error_message = None
    api_key = '####################'  # Replace with your OpenWeather API key

    # Fetch predefined cities from the database
    predefined_cities = PredefinedCity.objects.all()
    cities_weather = []

    # Fetch weather data for predefined cities
    for city in predefined_cities:
        data = get_weather_data(city.name, api_key)
        if data:
            cities_weather.append(data)

    if request.method == 'POST':
        city = request.POST.get('name')
        if city:
            weather_data = get_weather_data(city, api_key)
            if not weather_data:
                error_message = 'Could not retrieve weather data.'

    return render(request, 'index.html', {
        'weather_data': weather_data,
        'error': error_message,
        'cities_weather': cities_weather,
    })
