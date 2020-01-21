from django.contrib import admin

# Register your models here.

from .models import User


@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    """Custom User Admin"""
    list_display = ("username", "email", "gender", "language", "currency", "superhost")
    list_filter = ("language", "currency", "superhost")

