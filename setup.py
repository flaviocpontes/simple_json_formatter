from setuptools import setup, find_packages

VERSION = '0.1.0'

setup(
    name='simple_json_formatter',
    license='MIT',
    version=VERSION,
    packages=find_packages(exclude=['*test*']),
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
    tests_require=['freezegun']
)
