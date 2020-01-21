from django.contrib import admin
from . import models

# Create your models here.


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):
    pass


