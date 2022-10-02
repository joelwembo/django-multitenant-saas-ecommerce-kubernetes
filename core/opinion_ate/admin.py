from django.contrib import admin

# Register your models here.
from .models import Restaurant , Dish

admin.site.register(Restaurant)
admin.site.register(Dish)
