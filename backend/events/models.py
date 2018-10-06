from django.db import models
from django.utils import timezone
from rest_framework.decorators import api_view

from django_enumfield import enum

# Frequency of subscription billing
class Category(enum.Enum):
    PARTY = 0
    SPEAKER = 1
    CAMPUS = 2
    
    
# Default Event class for Stanford events
class Event(models.Model):
    #Name of the event
    name = models.CharField(max_length=128, null=True)
    #Description of the event
    description = models.CharField(max_length=128, null=True)
    #Date that the subscription was created
    date_created = models.DateTimeField(null=True, editable=False)
    #Date that the subscription was created
    date_modified = models.DateTimeField(null=True, editable=False)
    #Start time for the event
    date_start_time = models.DateTimeField(null=True, editable=False)
    #End time for the event
    date_end_time = models.DateTimeField(null=True, editable=False)
    #URL from where the event was found
    source = models.URLField(null=True, editable=True)
    #Category
    category = enum.EnumField(Category, default=Category.PARTY)
    #Location, place to meet
    location = models.CharField(max_length=128, null=True)
    
    
    # Keeps track of whether the model was created or modified.
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.date_created = timezone.now()
        self.date_modified = timezone.now()
        return super(Event, self).save(*args, **kwargs)