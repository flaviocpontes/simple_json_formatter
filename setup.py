# -*- coding: utf-8 -*-
from os import path
from setuptools import setup, find_packages
from simple_json_log_formatter import __version__, __author__,\
    __author_email__

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()

setup(
    name='simple_json_log_formatter',
    license='MIT',
    version=__version__,
    description='Simple log formatter for Logstash-compatible JSON output',
    long_description=long_description,
    packages=find_packages(exclude=['tests']),
    package_data={'': ['README.rst', ]},
    url='https://github.com/flaviocpontes/simple_json_log_formatter',
    download_url='https://github.com/flaviocpontes/simple_json_log_formatter/archive/{v}.tar.gz'.format(v=__version__),
    author=__author__,
    author_email=__author_email__,
    python_requires='>=2.7',
    keywords='logging json log output formatter',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    test_suite='tests',
    install_requires=['six', ],
    tests_require=['freezegun', 'coverage', 'codecov', 'six', ],
    extras_require={'dev': ['factory_boy==2.8.1', 'pathlib2==2.1.0',
                            'freezegun==0.3.9', 'coverage', 'codecov']}
)
