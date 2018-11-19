# django imports
from django.db import models

# Create your models here.


class Blog(models.Model):
    '''
        Model to save blog details
    '''
    section = models.IntegerField()
    title = models.CharField(max_length=225)
    description = models.CharField(max_length=1024)
    checkmark = models.BooleanField(default=False)