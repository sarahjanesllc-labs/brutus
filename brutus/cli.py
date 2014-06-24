""" cli - brutus commands """

import os
import sys
sys.path.append('.')
import logging
import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.autoreload
from brutus.app import Application
from tornado.process import fork_processes, task_id
from tornado.log import app_log
from tornado.options import define, options, parse_command_line
from tornado.util import ObjectDict

define("port", default=9000, help="port", type=int)
define("debug", default=False, help="run in debug mode", type=bool)


def main():
    """ entry """
    try:
        conf = __import__('conf')
    except ImportError as e:
        app_log.critical("Unable to load site config. ({})".format(e))
        raise SystemExit()
    parse_command_line()

    if options.debug:
        app_log.setLevel(logging.DEBUG)

    if not options.debug:
        fork_processes(None)
    options.port += task_id() or 0

    if not os.path.isdir(conf.app_path):
        app_log.critical("{p} isn't accessible, maybe "
                         "create it?".format(p=conf.app_path))
        raise SystemExit()
    app_log.debug("Starting {name} on port {port}".format(name=conf.name,
                                                          port=options.port))
    # initialize the application
    tornado.httpserver.HTTPServer(Application(options,
                                              conf)).listen(options.port,
                                                            '0.0.0.0')
    ioloop = tornado.ioloop.IOLoop.instance()
    if options.debug:
        tornado.autoreload.start(ioloop)
    # enter the Tornado IO loop
    ioloop.start()
