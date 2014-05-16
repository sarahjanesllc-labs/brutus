""" app - application interface """

import os
import re
import sys
import logging
import tornado.web
from json import dumps, loads
from tornado.log import app_log
from tornado.escape import to_unicode


class Handler(tornado.web.RequestHandler):
    @property
    def cfg(self):
        return self.application.cfg

    def head(self, *args, **kwargs):
        self.get(*args, **kwargs)
        self.request.body = ''

    def is_argument_present(self, name):
        return not (self.request.arguments.get(name, None) == None)

    def get_current_user(self):
        return to_unicode(self.get_secure_cookie('userid'))

    def get_secure_cookie(self, name, if_none=""):
        cook = tornado.web.RequestHandler.get_secure_cookie(self, name)
        if cook == None:
            return if_none
        return cook

    def send_errmsg(self, errmsg):
        self.set_secure_cookie("errmsg", errmsg)

    def send_statmsg(self, statmsg):
        self.set_secure_cookie("statmsg", statmsg)

    def render(self, template_name, **kwargs):
        error = self.get_secure_cookie("errmsg")
        status = self.get_secure_cookie("statmsg")
        self.clear_cookie("errmsg")
        self.clear_cookie("statmsg")
        tornado.web.RequestHandler.render(self,
                                          template_name,
                                          errmsg=error,
                                          statmsg=status,
                                          **kwargs)

    # API render
    def render_json(self, content):
        self.set_header("Content-Type", "application/json")
        self.set_header("Access-Control-Allow-Origin", "*")
        self.write(dumps(content))
        self.finish()


class Application(tornado.web.Application):
    def __init__(self, opts, cfg):
        self.opts = opts
        self.cfg = cfg
        urls = [
            (r"/", "brutus.views.index"),
            (r"/about", "brutus.views.about"),
            (r"/login", "brutus.views.login"),
            (r"/logout", "brutus.views.logout"),
            # Consumer routes
            (r"/browse", "brutus.consumer.views.index"),
            # Vendor routes
            (r"/manage", "brutus.vendor.views.index"),
        ]
        settings = dict(
            template_path=os.path.join(self.cfg.app_path, "templates"),
            static_path=os.path.join(self.cfg.app_path, "public"),
            xsrf_cookies=False if self.opts.debug else True,
            cookie_secret="i love cookies!!@!#!@!",
            debug=self.opts.debug,
            ui_modules={},
            login_url="/login",
        )
        tornado.web.Application.__init__(self, urls, **settings)
