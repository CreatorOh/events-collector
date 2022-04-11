import logging.config

from flask import Flask
from flask_restx import Api

from collector_backend import event_log_helper, event

#
event_log_formatter = logging.Formatter('%(message)s')
event_log_handler = logging.handlers.RotatingFileHandler('/tmp/collector.log',
                                                         maxBytes=5 * 1024 * 1024,
                                                         backupCount=10)
event_log_handler.setFormatter(event_log_formatter)
event_logger = logging.getLogger('event_logger')
event_logger.addHandler(event_log_handler)
event_logger.setLevel(logging.INFO)


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.update(test_config)
    app.config.SWAGGER_UI_DOC_EXPANSION = 'full'

    api = Api(app, version='0.1', title='API Document', description='A simple REST endpoint to collect events', doc="/api-docs")
    api.add_namespace(event.ns, path='/event')

    return app
