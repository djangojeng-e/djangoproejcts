from django.conf.urls import url
from . import views

urlpaatterns = [

    url(r'^$', views.index, name="index")
]