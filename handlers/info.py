#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from rapidsms.contrib.handlers.handlers.keyword import KeywordHandler
from django.utils.translation import ugettext as _

class InfoHandler(KeywordHandler):
    """
    Handle any message prefixed ECHO, responding with the remainder of
    the text. Useful for remotely checking that the router is running.
    """

    keyword = "info"

    def help(self):
        self.respond(_("Welcome to the Afghan Governance application. Text this number a brief description of your experience with a government official or government facility. To see what others have reported, text 'search NAME'. For more information call 12345678, or visit www.afghanpoll.af"))

    def handle(self, text):
        self.respond(text)
