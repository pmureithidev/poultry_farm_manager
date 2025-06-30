from django.contrib import admin
from .models import Farmer

# Register your models here.
admin.site.register (Farmer)
admin.site.site_header = "PoultryFarm Manager Administration"
admin.site.site_title = "PoultryFarm Admin Portal"
admin.site.index_title = "Farm Management System"

