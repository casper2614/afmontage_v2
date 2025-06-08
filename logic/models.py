from django.db import models

# Create your models here.
class Trailer(models.Model):
    id = models.CharField('ID', null=False, primary_key=True, unique=True, max_length=16)
    description = models.CharField('Beschrijving', max_length=256)

    def __str__(self):
        return self.id
    
class Action(models.Model):
    LOCATIONS = (
        ('T', 'Op de trailer'),
        ('P', 'In de restpuntenpallet'),
        ('N', 'Nvt.'),
    )

    trailer_id = models.ForeignKey(Trailer, on_delete=models.CASCADE, null=False)
    id = models.AutoField(primary_key=True)
    summary = models.CharField('Samenvatting', max_length=256)

    is_component_detached = models.BooleanField('Het gaat om een restpunt met los onderdeel', default=False)
    is_component_delivered = models.BooleanField('Het onderdeel is geleverd', default=False)
    is_component_correct_amount = models.BooleanField('Het onderdeel is beschikbaar in benodigde hoeveelheid', default=False)

    who_contacted = models.CharField('Wie is gecontacteerd?', max_length=64)
    result_contact = models.CharField('Resultaat van contact', max_length=256)
    expected_delivery_date = models.DateField('Verwachte leveringsdatum', null=True)

    location_component = models.CharField(choices=LOCATIONS, max_length=1)

    description_of_action = models.TextField('Beschrijving van handeling', null=False)
    reason_action = models.TextField('Reden waarom handeling in hal 4 plaats moet vinden', null=False)
    name_creator_action = models.CharField('Naam melder van restpunt', max_length=64, null=False)
    extra_info_action = models.TextField('Aanvullende informatie', null=False)

    def __str__(self):
        return self.summary