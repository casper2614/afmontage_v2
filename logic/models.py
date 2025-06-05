# Casper Janssen, Wessel Janssen © 2025
# Alle rechten voorbehouden.
from django.db import models

# Create your models here.
class Trailer(models.Model):
    id = models.CharField('ID', null=False, primary_key=True, unique=True, max_length=16)
    description = models.CharField('Description', max_length=256)

    def __str__(self):
        return self.id
    
class Action(models.Model):
    id = models.ForeignKey(Trailer, on_delete=models.CASCADE, primary_key=True, null=False)
    description = models.CharField('Description', max_length=256, null=False)

    def __str__(self):
        return self.description