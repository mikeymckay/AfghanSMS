#!/usr/bin/env python
#
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_GET, require_POST


from afghansms_extensions.models import *
from . import forms

#from StringIO import StringIO
#import csv

def reports(req):
    context_instance=RequestContext(req)
    context_instance['reports'] =  Report.objects.order_by('-datetime')
    return render_to_response("reports.html", context_instance)

def dashboard(req):
    context_instance=RequestContext(req)
    #context_instance['todays_report_count'] = len(Report.objects.filter(datetime__starts_with = datetime.today())
    #context_instance['weeks_report_count'] = len(Report.objects.filter(datetime = datetime.today()))
    context_instance['total_report_count'] = len(Report.objects.all())
    context_instance['latest_report'] = Report.objects.all()[0].message
    return render_to_response("afghan_dashboard.html", context_instance)

def search(req):
    context_instance=RequestContext(req)
    if req.method == "POST":
        forms.SearchForm(req.POST)
        context_instance['official_results'] = None
        context_instance['location_results'] = None
        context_instance['report_results'] = None
    else:
        forms.SearchForm
    
    context_instance['search_form'] = forms.SearchForm

    return render_to_response("search.html", context_instance)
