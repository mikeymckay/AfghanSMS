#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from rapidsms.contrib.handlers.handlers.keyword import KeywordHandler
from django.utils.translation import ugettext as _

class InfoHandler(KeywordHandler):
    """
    Handle messages that consist of the word "info"
    Check the localization file for other translations
    """

    keyword = _("info")

    def help(self):
        self.respond(_("Welcome to the Afghan Governance application. Text this number a brief description of your experience with a government official or government facility. To see what others have reported, text 'search NAME'. For more information call 12345678, or visit www.afghanpoll.af"))
