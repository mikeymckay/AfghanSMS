#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from rapidsms.contrib.handlers.handlers.keyword import KeywordHandler
from django.utils.translation import ugettext as _
from afghansms_extensions.models import Report

class ReportLastHandler(KeywordHandler):
    """
    Handle messages that contain just the text "report last"
    Check the localization file for other translations
    """

    keyword = _("report last")

    def help(self):
        self.respond( _("Last reported incident: %s") % Report.most_recent() )
