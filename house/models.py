from django.db import models
from room.models import Room
from image_cropping import ImageRatioField


class House(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    rooms = models.ManyToManyField(Room, blank=True)

    class Meta:
        ordering = ("-title",)
        verbose_name = u'House'
        verbose_name_plural = u'Houses'

    def __unicode__(self):
        return self.title


class HouseImage(models.Model):
    image = models.ImageField('Image', upload_to='houses')
    cropping = ImageRatioField('image', '215x180')
    obj = models.ForeignKey(House)

    class Meta:
        ordering = ("-image",)
        verbose_name = u'House image'
        verbose_name_plural = u'House images'
