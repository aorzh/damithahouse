from django.db import models
from ckeditor.fields import RichTextField


class Article(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextField()
    time = models.DateField()

    class Meta:
        ordering = ("-title", "time")
        verbose_name = u'Article'
        verbose_name_plural = u'Articles'

    # Override the __unicode__() method to return out something meaningful!
    def __unicode__(self):
        return self.title
