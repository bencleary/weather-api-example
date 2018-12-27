from django.shortcuts import render, HttpResponse
from django.views import View
from .forms import WeatherForm
from django.conf import settings
import requests
import json
from .decorators import say_hi


class WeatherAPI(View):

    template_name = "app.html"
    form = WeatherForm

    def fetch_api_data(self, city):
        # personally i would use ajax to make this call
        try:
            response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&APPID={settings.API_KEY}")
            response.raise_for_status()
            return response.json()
        except Exception as e:
            return e
    
    @say_hi
    def get(self, request):
        form = self.form()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        if request.body != None:
            api_response = self.fetch_api_data(json.loads(request.body).get('city', 'London,UK'))
            return HttpResponse(json.dumps(api_response))
