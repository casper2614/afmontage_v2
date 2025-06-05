# Casper Janssen, Wessel Janssen © 2025
# Alle rechten voorbehouden.
from django.db import models

# Create your models here.
class Trailer(models.Model):
    id = models.CharField('ID', unique=True, primary_key=True, null=False, max_length=16)
    description = models.CharField('Description', max_length=256)

    def __str__(self):
        return self.id