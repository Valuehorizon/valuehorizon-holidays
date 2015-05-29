from django.db import models, IntegrityError
from django.db.models import Manager
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType
from datetime import date, datetime, timedelta

from countries.models import Country


class Holiday(models.Model):
    """
    A business holiday
    """

    country = models.ForeignKey(Country, related_name="countryholiday")
    name = models.CharField(max_length=255)
    date = models.DateField()
    description = models.TextField(blank=True)
    
    HOLIDAY_TYPE_CHOICES = (
        (u'OF', u'Official'),
        (u'UN', u'Unofficial')
    )
    holiday_type = models.CharField(max_length = 2, choices = HOLIDAY_TYPE_CHOICES, default="OF")
    
    class Meta:
        verbose_name_plural = 'Holiday'
        verbose_name = 'Holiday'
        ordering = ['-date', 'country', ]
        unique_together = ("country", "date")
        
    def __unicode__(self):
        return u'%s, %s' % (unicode(self.name), unicode(self.date))

