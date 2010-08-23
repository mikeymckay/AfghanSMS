#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from rapidsms.contrib.handlers.handlers.keyword import KeywordHandler
from django.utils.translation import ugettext as _
from afghansms_extensions.models import Report

class SearchServiceHandler(KeywordHandler):
    """
    Handle messages that start with the text "search service"
    Check the localization file for other translations
    """

    keyword = _("search service")

    def help(self):
        self.respond( _("To search for reports by service, send: SEARCH SERVICE <Agriculture/Land or Commerce or Education or Justice or Health or Transportation or Electricity or Water>"))

    def handle(self, text):
        try:
            last_report_for_service = Report.objects.filter(service__contains=text.lower()).order_by('-datetime')[0]
            self.respond( _("Last report for %(service)s: %(report)s") % {'service':text, 'report':last_report_for_service})
        except:
            self.respond( _("No result found for: %s") % text)
