""" cli - brutus commands """

import os
import re
import sys
import logging
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.autoreload
from brutus.app import Application
from tornado.process import fork_processes, task_id
from tornado.log import app_log
from tornado.options import define, options, parse_command_line

define("port", default=9000, help="port", type=int)
define("debug", default=False, help="run in debug mode", type=bool)

def main():
    """ entry """
    parse_command_line()

    if options.debug:
        app_log.setLevel(logging.DEBUG)

    if not options.debug:
        fork_processes(None)
    options.port += task_id() or 0

    app_log.debug("Starting server on port {port}".format(port=options.port))
    # initialize the application
    tornado.httpserver.HTTPServer(Application(options)).listen(options.port, '0.0.0.0')
    ioloop = tornado.ioloop.IOLoop.instance()
    if options.debug:
        tornado.autoreload.start(ioloop)
    # enter the Tornado IO loop
    ioloop.start()
