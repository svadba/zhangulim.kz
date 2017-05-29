from django.contrib import admin
from .models import Flavor


@admin.register(Flavor)
class AdminFlavor(admin.ModelAdmin):
    list_display = ["title", "price"]
