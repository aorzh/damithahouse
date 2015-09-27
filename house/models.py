from django.db import models
from room.models import Room

class House(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    rooms = models.ManyToManyField(Room)

    class Meta:
        ordering = ("-title",)
        verbose_name = u'House'
        verbose_name_plural = u'Houses'

    def __unicode__(self):
        return self.title
