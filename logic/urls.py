from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('trailer/<str:trailer_id>/', views.action_list, name='action_list'),
    path('trailer/<str:trailer_id>/restpunt/<str:action_id>', views.action, name='action'),
    path('maak/restpunt/', views.create_action, name='create_action'),
    path('maak/trailer/', views.create_trailer, name='create_trailer'),
]
