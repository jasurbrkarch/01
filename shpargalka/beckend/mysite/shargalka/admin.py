from django.contrib import admin
from .models import Shargalka  # "shargalka" ni "Shargalka" ga o'zgartiring

class ShargalkaAdmin(admin.ModelAdmin):
    list_display = ['savol', 'javob']

admin.site.register(Shargalka, ShargalkaAdmin)  # "shargalka" ni "Shargalka" ga o'zgartiring

