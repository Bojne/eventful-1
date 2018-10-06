from django.db import models
from django.utils import timezone

# Create your models here.
class Event(models.Model):
    #Name of the event
    name = models.CharField(max_length=128, null=True)
    #Description of the event
    description = models.CharField(max_length=128, null=True)
    #Date that the subscription was created
    date_created = models.DateTimeField(editable=False)
    #Date that the subscription was created
    date_modified = models.DateTimeField(editable=False)
    
    # Keeps track of whether the model was created or modified.
    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.date_created = timezone.now()
        self.date_modified = timezone.now()
        return super(Event, self).save(*args, **kwargs)