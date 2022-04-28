from django.db import models
from django.db.models.fields import DateField
from datetime import datetime
from django.db.models import CharField, Model


# Create your models here
class Event(models.Model):
    title = models.CharField(max_length=40)
    start = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    end = models.DateTimeField(auto_now=False, auto_now_add=False, null=True, blank=True)

    def __unicode__(self):
        return self.title
        
class PeriodDate(models.Model):
    per_date = models.CharField(max_length=15)

    def __str__(self):
     return self.per_date 