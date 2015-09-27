from django.db import models

class Room(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    house_have_room = models.ForeignKey('house.House', blank=True, null=True, default='')
    airbnb = models.URLField(verbose_name='Airbnb link', blank=True)
    bookingcom = models.URLField(verbose_name='Booking.com link', blank=True)
    tripsadvisor = models.URLField(verbose_name='Tripsadvisor link', blank=True)

    class Meta:
        ordering = ("-title",)
        verbose_name = u'Room'
        verbose_name_plural = u'Rooms'

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.title
