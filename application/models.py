# coding: utf-8
from django.db import models

class DayAndTime(models.Model):
    start_time = models.TimeField(verbose_name=u'Start time')
    end_time = models.TimeField(verbose_name=u'End time')
    sun =models.BooleanField(default=False,verbose_name=u'Sunday')
    mon =models.BooleanField(default=False,verbose_name=u'Monday')
    tue =models.BooleanField(default=False,verbose_name=u'Tuesday')
    wed =models.BooleanField(default=False,verbose_name=u'Wednesday')
    thu =models.BooleanField(default=False,verbose_name=u'Thursday')
    fri =models.BooleanField(default=False,verbose_name=u'Friday')
    sat =models.BooleanField(default=False,verbose_name=u'Saturday')

    def __unicode__(self):
        return '%s ' % self.id

    class Meta:
        verbose_name_plural = "Day and time"
        verbose_name = "instance of Day and time"
