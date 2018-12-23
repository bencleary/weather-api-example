from django.urls import path
from .views import WeatherAPI

urlpatterns = [
    path('weather', WeatherAPI.as_view(), name="weather-api")
]