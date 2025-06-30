from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import Farmer

class FarmerRegistrationForm(UserCreationForm):
    farm_name = forms.CharField(max_length=100, required=True)
    phone = forms.CharField(max_length=15, required=True)


    class Meta:
        model = Farmer
        fields = ("username", "farm_name", "phone", "password1", "password2")