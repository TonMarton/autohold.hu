from django import forms
from django.contrib import admin
from cars.models import Car

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = '__all__'
        widgets = {'image_locations': forms.HiddenInput()}
