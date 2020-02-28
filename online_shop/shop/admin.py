from django.contrib import admin

# Register your models here.

from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}
    # prepopulated_fields equates to the name entered in admin.


admin.site.register(Category, CategoryAdmin)


