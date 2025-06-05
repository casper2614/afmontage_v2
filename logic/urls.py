# Casper Janssen, Wessel Janssen © 2025
# Alle rechten voorbehouden.
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('trailer/<str:id>/', views.action_list, name='action_list'),
    path('action/<str:id>/', views.action, name='action'),
    path('create/action/', views.create_action, name='create_action')
]
