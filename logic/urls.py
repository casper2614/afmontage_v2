# Casper Janssen, Wessel Janssen © 2025
# Alle rechten voorbehouden.
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
