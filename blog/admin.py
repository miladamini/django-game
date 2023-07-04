from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.blogMolde)
class blogAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
