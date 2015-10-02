from django.db import models
from image_cropping import ImageRatioField


class Category(models.Model):
    title = models.CharField(max_length=200)
    gallery_name = models.ManyToManyField('gallery.Gallery', blank=True)

    class Meta:
        ordering = ("-title",)
        verbose_name = u'Category'
        verbose_name_plural = u'Categories'

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.title


class Gallery(models.Model):
    title = models.CharField(max_length=200)
    category_name = models.ForeignKey('gallery.Category', blank=True, null=True, default='',)

    class Meta:
            ordering = ("-title",)
            verbose_name = u'Gallery'
            verbose_name_plural = u'Galleries'

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.title


class GalleryImage(models.Model):
    image = models.ImageField('Image', upload_to='gallery')
    cropping = ImageRatioField('image', '215x180', free_crop=True)
    gallery = models.ForeignKey('gallery.Gallery', blank=True, null=True, default='')

    class Meta:
        ordering = ("-image",)
        verbose_name = u'Image'
        verbose_name_plural = u'Images'
