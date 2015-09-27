from django.db import models

class Room(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    class Meta:
        ordering = ("-title",)
        verbose_name = u'Room'
        verbose_name_plural = u'Rooms'

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.title


class House(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    # rooms = models.ManyToOneRel(Room)

    class Meta:
        ordering = ("-title",)
        verbose_name = u'House'
        verbose_name_plural = u'Houses'

    def __unicode__(self):
        return self.title
