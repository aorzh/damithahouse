from django.db import models


class SliderImage(models.Model):
    image = models.ImageField('Image', upload_to='slider')

    class Meta:
        ordering = ("-image",)
        verbose_name = u'Slider image'
        verbose_name_plural = u'Slider images'
