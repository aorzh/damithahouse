from django.db import models
from image_cropping import ImageRatioField
from ckeditor.fields import RichTextField


class Room(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
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


class RoomImage(models.Model):
    image = models.ImageField('Image', upload_to='houses')
    cropping = ImageRatioField('image', '215x180', free_crop=True)
    obj = models.ForeignKey(Room)

    class Meta:
        ordering = ("-image",)
        verbose_name = u'Room image'
        verbose_name_plural = u'Room images'
