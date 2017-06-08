import unittest
import logging
import json
import inspect
from datetime import datetime
from io import StringIO
from sys import stdout
try:
    from unittest.mock import Mock, call, patch
except ImportError:
    # python 2.7
    from mock import Mock, call, patch

from simple_json_formatter import JsonFormatter
from freezegun import freeze_time


class LoggerTests(unittest.TestCase):
    def setUp(self):
        self.buffer = StringIO()
        handler = logging.StreamHandler(stream=self.buffer)
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(JsonFormatter(json.dumps))
        logging.getLogger().addHandler(handler)

    def test_it_logs_valid_json_string_if_message_is_json_serializeable(self):
        message = {
            'info': 'Se tem permissao, tamo dando sarrada',
            'msg': {
                'foo': 'bar',
                'baz': 'blu'
            }
        }

        logging.error(message)

        logged_content = self.buffer.getvalue()
        json_log = json.loads(logged_content)

        self.assertDictEqual(json_log['msg'], message)

    def test_it_logs_valid_json_string_if_message_isnt_json_serializeable(self):
        class FooJsonUnserializeable:
            pass

        obj = FooJsonUnserializeable()
        message = {'info': obj}
        logging.error(message)

        logged_content = self.buffer.getvalue()
        json_log = json.loads(logged_content)

        self.assertDictEqual(json_log['msg'], {'info': str(obj)})

    def test_it_escapes_strings(self):
        message = """"Aaaalgma coisa"paando `bem por'/\t \\" \" \' \n "aaa """

        logging.error(message)

        logged_content = self.buffer.getvalue()
        json_log = json.loads(logged_content)

        self.assertEqual(json_log['msg'], message)

    @freeze_time("2017-03-31 04:20:00")
    def test_it_logs_current_log_time(self):
        now = datetime.now().isoformat()

        logging.error("Batemos tambores, eles panela.")

        logged_content = self.buffer.getvalue()
        json_log = json.loads(logged_content)

        self.assertEqual(json_log['logged_at'], now)

    def test_it_logs_exceptions_tracebacks(self):
        exception_message = "Carros importados pra garantir os translados"

        try:
            raise Exception(exception_message)
        except Exception:
            logging.exception("Aqui nao eh GTA, eh pior, eh Grajau")

        logged_content = self.buffer.getvalue()
        json_log = json.loads(logged_content)

        exc_class, exc_message, exc_traceback = json_log['exc_info']
        self.assertIn(member=exception_message,
                      container=exc_message)

        current_func_name = inspect.currentframe().f_code.co_name
        self.assertIn(member=current_func_name,
                      container=exc_traceback)

    @freeze_time("2017-03-31 04:20:00")
    def test_it_logs_datetime_objects(self):
        message = {
            'date': datetime.now().date(),
            'time': datetime.now().time(),
            'datetime': datetime.now()
        }

        logging.error(message)

        logged_content = self.buffer.getvalue()
        json_log = json.loads(logged_content)

        expected_output = {
            'date': message['date'].isoformat(),
            'time': message['time'].isoformat(),
            'datetime': message['datetime'].isoformat()
        }
        self.assertDictEqual(json_log['msg'], expected_output)