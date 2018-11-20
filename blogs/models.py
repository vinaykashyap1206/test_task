# django imports
from django.db import models

# Create your models here.


class Blog(models.Model):
    '''
        Model to save blog details
    '''
    section_id = models.IntegerField()
    section_name = models.CharField(max_length=225, null=True, blank=True)
    title = models.CharField(max_length=225)
    description = models.CharField(max_length=1024)
    checkmark = models.BooleanField(default=False)
    topic_name = models.CharField(max_length=225, null=True, blank=True)
    blog_category_name = models.CharField(max_length=225, null=True, blank=True)
