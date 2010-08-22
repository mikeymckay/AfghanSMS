#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4
#
from django.db import models
from decisiontree.models import Session, Entry
from django.db.models.signals import post_save


# Create your models here.
#
class Report(models.Model):
    '''A question, which is just some text to be sent to the user,
       and an optional error message if the question is not answered
       properly'''
    datetime = models.DateTimeField()
    rating = models.IntegerField(null=True,blank=True)
    cost = models.TextField(null=True,blank=True)
    location = models.TextField(null=True,blank=True)
    official_name = models.TextField(null=True,blank=True)
    message = models.TextField(null=True,blank=True)
    session = models.ForeignKey(Session)
    
    def __unicode__(self):
        return self.message

def update_report(sender, **kwargs):
    entry = kwargs["instance"]
    reports = Report.objects.filter(session = entry.session)

    if not reports:
        report = Report(session = entry.session)
    else:
        report = Report.objects.filter(session = entry.session)[0]

    if entry.sequence_id == 1:
        report.official_name = entry.text
#    elif entry.sequence_id == 2:
    elif entry.sequence_id == 3:
        report.message = entry.text
    elif entry.sequence_id == 4:
        report.location = entry.text
#        elif entry.sequence_id == 5:
#        elif entry.sequence_id == 6:
    elif entry.sequence_id == 7:
        report.cost = entry.text
    elif entry.sequence_id == 8:
        report.rating = entry.text

    report.datetime = entry.time
    report.save()

post_save.connect(update_report, sender=Entry)
