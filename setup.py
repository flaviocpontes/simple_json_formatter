from setuptools import setup, find_packages
from simple_json_logging_formatter import __version__, __author__,\
    __author_email__

setup(
    name='simple_json_logging_formatter',
    license='MIT',
    version=__version__,
    packages=find_packages(exclude=['tests']),
    url='https://github.com/flaviocpontes/simple_json_logging_formatter',
    author=__author__,
    author_email=__author_email__,
    python_requires='>=3.4',
    keywords='logging json log output formatter',
    classifiers=[
        'Development Status :: 5 - Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    test_suite='tests',
    tests_require=['freezegun', 'coverage', 'codecov'],
    extras_require={'dev': ['factory_boy==2.8.1', 'pathlib2==2.1.0',
                            'freezegun==0.3.9', 'coverage', 'codecov']}
)
