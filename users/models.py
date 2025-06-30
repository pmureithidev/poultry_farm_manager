from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Farmer(AbstractUser):
    # Remove unused default fields
    first_name = None
    last_name = None
    
    # Add farmer-specific fields
    farm_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    
    # Set as non-staff by default
    is_staff = models.BooleanField(default=False)
