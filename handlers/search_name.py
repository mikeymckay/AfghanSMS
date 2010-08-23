#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from rapidsms.contrib.handlers.handlers.keyword import KeywordHandler
from django.utils.translation import ugettext as _
from afghansms_extensions.models import Report

class SearchNameHandler(KeywordHandler):
    """
    Handle messages that start with the text "search name"
    Check the localization file for other translations
    """

    keyword = _("search name")

    def help(self):
        self.respond( _("To search for reports by name, send: SEARCH NAME <name>"))

    def handle(self, text):
        try:
          last_report_for_name = Report.objects.filter(official_name__contains=text).order_by('-datetime')[0]
          self.respond( _("Last report for %(name)s: %(report)s") % {'name':text, 'report':last_report_for_name})
        except:
          self.respond( _("No result found for: %s") % text)
