from django.shortcuts import render
from django.views import View
from .forms import WeatherForm
from django.conf import settings
import requests


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
        
    def get(self, request):
        form = self.form()
        return render(request, self.template_name, {'form': form})
    
    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            api_response = self.fetch_api_data(form.cleaned_data['city'])
        else:
            api_response = None
        return render(request, self.template_name, {'form': form, 'api_response': api_response})
