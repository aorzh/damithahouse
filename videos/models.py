from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=200)
    url = models.URLField()

    class Meta:
        ordering = ("-title", "url")
        verbose_name = u'Video'
        verbose_name_plural = u'Videos'

    def __unicode__(self):
        return self.title
