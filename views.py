#!/usr/bin/env python
#
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required, permission_required

from afghansms_extensions.models import *

#from StringIO import StringIO
#import csv

def reports(req):
    context_instance=RequestContext(req)
    return render_to_response("reports.html", context_instance)
