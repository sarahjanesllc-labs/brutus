""" app - application interface """

import os
import tornado.web
from json import dumps
from tornado.escape import to_unicode


class Handler(tornado.web.RequestHandler):
    @property
    def cfg(self):
        return self.application.cfg

    def head(self, *args, **kwargs):
        self.get(*args, **kwargs)
        self.request.body = ''

    def is_argument_present(self, name):
        return not (self.request.arguments.get(name, None) is None)

    def get_current_user(self):
        return to_unicode(self.get_secure_cookie('userid'))

    def get_secure_cookie(self, name, if_none=""):
        cook = tornado.web.RequestHandler.get_secure_cookie(self, name)
        if cook is None:
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
        urls = self.route_add()
        urls.append(
              (r"/(.*)", tornado.web.StaticFileHandler,
                  dict(path=os.path.join(self.cfg.app_path, "index.html"))))
        urls.append(
              (r"/css/(.*)", tornado.web.StaticFileHandler,
                  dict(path=os.path.join(self.cfg.app_path, "css"))))
        urls.append(
              (r"/fonts/(.*)", tornado.web.StaticFileHandler,
                  dict(path=os.path.join(self.cfg.app_path, "fonts"))))
        urls.append(
              (r"/js/(.*)", tornado.web.StaticFileHandler,
                  dict(path=os.path.join(self.cfg.app_path, "js"))))
        urls.append(
              (r"/images/(.*)", tornado.web.StaticFileHandler,
                  dict(path=os.path.join(self.cfg.app_path, "images"))))

        settings = dict(
            template_path=None,
            static_path=os.path.join(self.cfg.app_path),
            xsrf_cookies=False if self.opts.debug else True,
            cookie_secret="i love cookies!!@!#!@!",
            debug=self.opts.debug)
        tornado.web.Application.__init__(self, urls, **settings)

    def route_add(self):
        """ routes url to api endpoint """
        urls = []
        for segment, endpoint in self.cfg.routes:
            urls.append((r"/api/{v}/{s}".format(
                v=self.cfg.api_version,
                s=segment), "brutus.api.{v}.{e}".format(
                    v=self.cfg.api_version,
                    e=endpoint)))
        return urls
