#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from rapidsms.contrib.handlers.handlers.keyword import KeywordHandler
from django.utils.translation import ugettext as _
from afghansms_extensions.models import Report

class ReportCountHandler(KeywordHandler):
    """
    Handle messages that contain just the text "report count"
    Check the localization file for other translations
    """

    keyword = _("report count")

    def help(self):
        self.respond( _("%s reports submitted so far") % Report.count_all() )

#    def handle(self, text):
#        self.respond(text)
