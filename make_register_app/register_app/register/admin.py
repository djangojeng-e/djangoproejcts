from django.contrib import admin
from .models import Django_user

# Register your models here.

class Django_userAdmin(admin.ModelAdmin):
    pass

admin.site.register(Django_user, Django_userAdmin)
