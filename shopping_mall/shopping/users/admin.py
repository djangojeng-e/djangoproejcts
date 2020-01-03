from django.contrib import admin

# Register your models here.

from .models import Users


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    pass