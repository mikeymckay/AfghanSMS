#!/usr/bin/env python
#
from rapidsms.contrib.handlers.handlers.keyword import KeywordHandler

class PingHandler(KeywordHandler):
    keyword = "ping"

    def help(self):
        self.respond("Pong")

    def handle(self, text):
        self.respond("You said: %s." % text)

