#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from rapidsms.contrib.handlers.handlers.keyword import KeywordHandler
from django.utils.translation import ugettext as _
from afghansms_extensions.models import Report

class SearchPlaceHandler(KeywordHandler):
    """
    Handle messages that start with the text "search place"
    Check the localization file for other translations
    """

    keyword = _("search place")

    def help(self):
        self.respond( _("To search for reports about a location, send: SEARCH PLACE <location name>"))

    def handle(self, text):
        try:
          last_report_for_location = Report.objects.filter(location__contains=text).order_by('-datetime')[0]
          self.respond( _("Last report for %(location)s: %(report)s") % {'location':text, 'report':last_report_for_location})
        except:
          self.respond( _("No result found for: %s") % text)
