Simple Json Logging Formatter
=============================

|Build Status| |codecov| |Current version at PyPI|

This is a fork of ``simple_json_logger``, extracting the formatter into
it's own project.

It formats the Python logging.Record into a JSON suitable for indexing
engines like Logstash and AWS CloudWatch Logs.

Installation
------------

``pip install simple_json_log_formatter``

Usage
-----

Simply set the formatter in a log handler and add it to the current
logger.

For example, to print the JSON logs to the current stream, set up the
logger with the following:

.. code:: python

    import json, logging
    from simple_json_log_formatter import SimpleJsonFormatter
    handler = logging.StreamHandler()
    handler.setFormatter(SimpleJsonFormatter(json.dumps))
    logging.getLogger().addHandler(handler)
    logging.getLogger().setLevel(logging.INFO)

And then simply call ``logging.info('TEST')``. It should print something
like this:

``{"timestamp": "2017-09-08T17:01:26.408975", "line_number": 1, "function": "<module>", "module": "<input>", "level": "INFO", "path": "<input>", "msg": "TEST"}``

Testing
-------

``python setup.py test``

Compatibility
-------------

Python versions 2.7 and 3.4+ are supported.

.. |Build Status| image:: https://travis-ci.org/flaviocpontes/simple_json_log_formatter.svg?branch=master
   :target: https://travis-ci.org/flaviocpontes/simple_json_log_formatter
.. |codecov| image:: https://codecov.io/gh/flaviocpontes/simple_json_log_formatter/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/flaviocpontes/simple_json_log_formatter
.. |Current version at PyPI| image:: https://img.shields.io/pypi/v/simple_json_log_formatter.svg
   :target: https://pypi.python.org/pypi/simple_json_log_formatter
