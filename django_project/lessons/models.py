from django.db import models
from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from sortedm2m.fields import SortedManyToManyField
from django.db.models.signals import post_save

# Create your models here.

class Page(models.Model):
    """Page is a catch-all model that encompasses plain text pages, 
       exercises, etc.
       For each content type, remember to connect it to Page via 
       post_save and create_page (see example below)"""
    content_type   = models.ForeignKey(ContentType)
    object_id      = models.PositiveIntegerField()
    content_object = generic.GenericForeignKey('content_type', 'object_id')

    @property
    def title(self):
        return self.content_object.title
        
class Text(models.Model):
    """Simple text page composed with Markdown"""
    title = models.CharField(max_length=400)
    text  = models.TextField(blank=True)

class Lesson(models.Model):
    number = models.PositiveIntegerField(unique=True)
    objectives  = models.CharField(max_length=400) # comma-separated list of learning objectives
    draft  = models.BooleanField()
    pages  = SortedManyToManyField(Page)

def create_page(sender, **kwargs):
    if 'created' in kwargs:
        if kwargs['created']:
            instance = kwargs['instance']
            ctype = ContentType.objects.get_for_model(instance)
            page  = Page.objects.get_or_create(content_type=ctype,
                                                object_id=instance.id)
  
post_save.connect(create_page, sender=Text)

