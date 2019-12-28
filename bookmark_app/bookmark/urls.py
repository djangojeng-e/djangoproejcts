from django.contrib import admin
from django.urls import path, include
from .views import BookmarkListView, BookmarkCreateView


urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'),
    path('add/', BookmarkCreateView.as_view(), name='add'),

]