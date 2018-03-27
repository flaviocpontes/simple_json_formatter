# -*- coding: utf-8 -*-
import logging
import sys
import json

import datetime
import traceback
from inspect import istraceback

PYTHON_MAJOR_VERSION = sys.version_info[0]

if PYTHON_MAJOR_VERSION == 2:
    str = unicode

CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0

_levelToName = {
    CRITICAL: 'CRITICAL',
    ERROR: 'ERROR',
    WARNING: 'WARNING',
    INFO: 'INFO',
    DEBUG: 'DEBUG',
    NOTSET: 'NOTSET',
}

DEFAULT_LOG_RECORD_FIELDS = {'name', 'msg', 'args', 'levelname', 'levelno',
                             'pathname', 'filename', 'module', 'exc_info',
                             'exc_class', 'exc_msg', 'exc_traceback',
                             'exc_text', 'stack_info', 'lineno', 'funcName',
                             'created', 'msecs', 'relativeCreated', 'thread',
                             'threadName', 'processName', 'process'}


class SimpleJsonFormatter(logging.Formatter):
    level_to_name_mapping = _levelToName

    def __init__(self, fmt=None, datefmt=None, style='%', serializer=json.dumps):
        super(SimpleJsonFormatter, self).__init__()
        self.serializer = serializer

    @staticmethod
    def _default_json_handler(obj):
        if isinstance(obj, (datetime.date, datetime.time)):
            return str(obj.isoformat())
        elif istraceback(obj):
            tb = u''.join(traceback.format_tb(obj))
            return tb.strip()
        elif isinstance(obj, Exception):
            return u"Exception: {}".format(str(obj))
        return str(obj)

    def format(self, record):
        msg = {
            'timestamp': str(datetime.datetime.now().isoformat()),
            'line_number': record.lineno,
            'function': str(record.funcName),
            'module': str(record.module),
            'level': str(self.level_to_name_mapping[record.levelno]),
            'path': str(record.pathname)
        }

        for field, value in record.__dict__.items():
            if field not in DEFAULT_LOG_RECORD_FIELDS:
                msg[field] = str(value)

        if isinstance(record.msg, dict):
            msg.update(record.msg)
        else:
            msg['msg'] = record.msg

        if record.exc_info:
            msg['exc_class'], msg['exc_msg'], msg['exc_traceback'] = record.exc_info

        return str(self.serializer(msg, default=self._default_json_handler))
