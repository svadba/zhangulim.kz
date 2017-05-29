from django.contrib import admin
from .models import StarFlavor


@admin.register(StarFlavor)
class AdminStarFlavor(admin.ModelAdmin):
    list_display = ["name"]

# Register your models here.
