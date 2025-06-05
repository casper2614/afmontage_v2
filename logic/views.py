# Casper Janssen, Wessel Janssen © 2025
# Alle rechten voorbehouden.
from django.shortcuts import render, get_object_or_404

# Create your views here.
from . import models

def index(request):
    context = {'trailer_list': models.Trailer.objects.all()}
    return render(request, 'index.html', context)

def action_list(request, id):
    context = {'trailer': get_object_or_404(models.Trailer, id=id),'action_list': models.Action.objects.filter(id=id)}
    return render(request, 'actions.html', context)

# Create page
def action(request, id):
    context = {'action': get_object_or_404(models.Action, id=id)}
    return render(request, 'index.html', context)

#Create page
def create_action(request):
    return render(request, 'index.html')

# To add a function to recieve form data