from django import forms


class WeatherForm(forms.Form):
    city = forms.CharField(max_length=200, label='Enter your city: ')