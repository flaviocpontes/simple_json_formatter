from setuptools import setup, find_packages

VERSION = '0.2.0'

setup(
    name='simple_json_formatter',
    license='MIT',
    version=VERSION,
    packages=find_packages(exclude=['tests']),
    url='https://github.com/flaviocpontes/simple_json_formatter',
    author='Flávio Cardoso Ferreira Pontes',
    author_email='flaviocpontes@gmail.com',
    keywords='logging json log output formatter',
    classifiers=[
        'Development Status :: 4 - Beta',
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
