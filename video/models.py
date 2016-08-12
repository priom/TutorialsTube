from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


# Create your models here.
class Video(models.Model):
    title = models.CharField(max_length=200)
    upload_date = models.DateField(default=timezone.now)
    video_id = models.CharField(max_length=50)
    tags = models.CharField(max_length=200)

    # display title on admin panel
    def __unicode__(self):
        return '%s - %s - %s' % (self.id, self.title, self.upload_date)

    # make url discoverable 
    def get_absolute_url(self):
        return '/video/%s/' % self.id