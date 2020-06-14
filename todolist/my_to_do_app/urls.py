from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('createTodo/', views.CreateTodo, name='CreateTodo'),
    path('deleteTodo/', views.doneTodo, name='deleteTodo'),
]