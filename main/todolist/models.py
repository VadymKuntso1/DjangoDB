from django.db import models
from datetime import datetime, timedelta


class priority(models.Model):
    id = id = models.IntegerField('id', primary_key=True, auto_created=True)
    title = models.CharField('title', max_length=150)


class task(models.Model):
    id = models.IntegerField('id', primary_key=True, auto_created=True)
    title = models.CharField('title',max_length=150)
    description = models.CharField('description',max_length=200)
    startdate = models.DateField('startdate', default=datetime.utcnow)
    priority = models.ForeignKey(priority,on_delete=models.CASCADE)
    days = models.IntegerField(null=False,blank=10)



class applied(models.Model):
    id = models.IntegerField('id', primary_key=True, auto_created=True)
    title = models.CharField('title', max_length=150)
    description = models.CharField('description', max_length=200)
    days = models.IntegerField(null=False, blank=10)

