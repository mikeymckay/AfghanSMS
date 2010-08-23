#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

import os
from django.conf.urls.defaults import *
import afghansms_extensions.views as views

urlpatterns = patterns('',
    (r'^reports$', views.reports),
    (r'^dashboard$', views.dashboard),
    (r'^$', views.dashboard),
    (r'^search$', views.search),
    
    # serve the static files for this TREE app
    # TODO: this should be automatic, via WEBUI
    (r'^static/afghansms_extensions/(?P<path>.*)$', "django.views.static.serve",
        {"document_root": os.path.dirname(__file__) + "/static"})
)
