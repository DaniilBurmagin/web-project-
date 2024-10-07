from django.urls import path
from . import views
urlpatterns = [
    path('', views.index),
    path('HelloWorld', views.HelloWorld)
]