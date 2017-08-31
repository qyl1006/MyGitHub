from django.contrib import admin

# Register your models here.

from pizzeria_s.models import Pizza, Topping

admin.site.register(Pizza)
admin.site.register(Topping)
