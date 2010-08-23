#!/usr/bin/env python
#
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required, permission_required
from django.views.decorators.http import require_GET, require_POST

from afghansms_extensions.models import *
from afghansms_extensions.forms import *

import datetime

#from StringIO import StringIO
#import csv

def reports(req):
    context_instance=RequestContext(req)
    context_instance['reports'] =  Report.objects.order_by('-datetime')
    return render_to_response("reports.html", context_instance)

def dashboard(req):
    today = datetime.date.today()
    context_instance=RequestContext(req)
    context_instance['todays_report_count'] = Report.objects.filter(datetime__gte = today).count()
    context_instance['weeks_report_count'] = Report.objects.filter(datetime__gte = (today - datetime.timedelta(weeks=1))).count()
    context_instance['total_report_count'] = Report.count_all()
    context_instance['latest_report'] = Report.objects.all()[0].message
    return render_to_response("afghan_dashboard.html", context_instance)

def search(req):
    context_instance=RequestContext(req)
    if req.method == "POST":
        form = SearchForm(req.POST)
        if form.is_valid():
            form.cleaned_data
            context_instance['official_results'] = Report.objects.filter(official_name__contains = form.cleaned_data['search'])
            context_instance['official_results_length'] = len(context_instance['official_results'])
            context_instance['location_results'] = Report.objects.filter(location__contains = form.cleaned_data['search'])
            context_instance['location_results_length'] = len(context_instance['location_results'])
            context_instance['message_results'] = Report.objects.filter(message__contains = form.cleaned_data['search'])
            context_instance['message_results_length'] = len(context_instance['message_results'])
 
    else:
        form = SearchForm()
        context_instance['new_search'] = True
    
    context_instance['search_form'] = form

    return render_to_response("search.html", context_instance)
