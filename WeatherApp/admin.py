from django.contrib import admin
from .models import PredefinedCity

@admin.register(PredefinedCity)
class PredefinedCityAdmin(admin.ModelAdmin):
    list_display = ('name',)
