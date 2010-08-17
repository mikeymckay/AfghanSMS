
#!/usr/bin/env python
#
from rapidsms.contrib.handlers.handlers.keyword import KeywordHandler
from django.utils.translation import ugettext as _

class InfoHandler(KeywordHandler):
    keyword = _("info")

    def help(self):
        self.respond(_("Welcome to the Afghan Governance application. Text this number a brief description of your experience with a government official or government facility. To see what others have reported, text 'search NAME'. For more information call 12345678, or visit www.afghanpoll.af"))

    def handle(self, text):
        self.respond("You said: %s." % text)

