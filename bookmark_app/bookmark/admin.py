from django.contrib import admin
from .models import Bookmark
# Register your models here.

@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    # fields = ('site_name', 'url')
    pass


