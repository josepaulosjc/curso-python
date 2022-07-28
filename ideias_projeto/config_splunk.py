import os
import logging.config

def config_splunk(token_splunk):
    SPLUNK_TOKEN = token_splunk
    SPLUNK_HOST = os.getenv('SPLUNK_HOST')
    SPLUNK_PORT = os.getenv('SPLUNK_PORT', '8088')
    SPLUNK_INDEX = os.getenv('SPLUNK_INDEX')
    LOGGING_CONFIG = {
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'json': {
                '()': 'pythonjsonlogger.jsonlogger.JsonFormatter',
                'format': '%(asctime)s %(created)f %(exc_info)s '
                          '%(filename)s %(funcName)s %(levelname)s '
                          '%(levelno)s %(lineno)d %(module)s %(message)s '
                          '%(pathname)s %(process)d %(processName)s '
                          '%(relativeCreated)d %(thread)d %(threadName)s'
            }
        },
        'handlers': {
            'splunk': {
                'level': 'INFO',
                'class': 'splunk_handler.SplunkHandler',
                'formatter': 'json',
                'host': SPLUNK_HOST,
                'port': SPLUNK_PORT,
                'token': SPLUNK_TOKEN,
                'index': SPLUNK_INDEX,
                'source': 'json',
                'verify': False,
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
            }
    },
        'loggers': {
            '': {
                'handlers': ['console', 'splunk'],
                'level': 'DEBUG'
            }
        }
    }
    logging.config.dictConfig(LOGGING_CONFIG)

logger = logging.getLogger(__name__)
