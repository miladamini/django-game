from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.gameMode)
class gameAdmin(admin.ModelAdmin):
    list_display = ['title']


@admin.register(models.lDitaile)
class lDitaileAdmin(admin.ModelAdmin):
    list_display = ['title', 'category']
    search_fields = ['title', 'category']
    list_filter = ['category']
