""" cli - brutus commands """

import os
import re
import sys
import yaml
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

cfg = os.path.expanduser("~/.brutus.yml")
cfg_stub = dict(name='Brutus',
                description="farmers market meet internets.",
                theme='cornfield',
                version='0.0.1',
                app_path=os.path.join(os.getenv("HOME",
                                                "/usr/local/share"),
                                      "brutus"))

define("port", default=9000, help="port", type=int)
define("debug", default=False, help="run in debug mode", type=bool)
define("config", default=cfg,
       help="config", type=str)

def main():
    """ entry """
    parse_command_line()

    if options.debug:
        app_log.setLevel(logging.DEBUG)

    if not options.debug:
        fork_processes(None)
    options.port += task_id() or 0

    if not os.path.exists(options.config):
        with open(options.config, 'w') as f:
            f.write(yaml.dump(cfg_stub, default_flow_style=False))
    with open(options.config, 'r') as f:
        cfg = ObjectDict(yaml.load(f.read()))

    if not os.path.isdir(cfg.app_path):
        app_log.critical("{p} isn't accessible, maybe create it?".format(p=cfg.app_path))
        raise SystemExit()
    app_log.debug("Starting {name} on port {port}".format(name=cfg.name,
                                                          port=options.port))
    # initialize the application
    tornado.httpserver.HTTPServer(Application(options,
                                              cfg)).listen(options.port, '0.0.0.0')
    ioloop = tornado.ioloop.IOLoop.instance()
    if options.debug:
        tornado.autoreload.start(ioloop)
    # enter the Tornado IO loop
    ioloop.start()
