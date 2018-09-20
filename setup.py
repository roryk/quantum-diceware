#!/usr/bin/env python
from setuptools import setup
import os

PROJECT = 'quantum_diceware'
VERSION = '0.2'
URL = ''
AUTHOR = u'Rory Kirchner'
AUTHOR_EMAIL = u'rory.kirchner@gmail.com'
DESC = "diceware a quantum random number generator"

def read_file(file_name):
    file_path = os.path.join(
        os.path.dirname(__file__),
        file_name
        )
    return open(file_path).read()

setup(
    name='quantum_diceware',
    version=VERSION,
    description=DESC,
    long_description=read_file('README.md'),
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    url=URL,
    include_package_data=True,
    zip_safe=False,
    packages=['quantum_diceware'],
    install_requires=[
        'quantumrandom'
    ],
    package_data = {'quantum_diceware': ['wordlists/*.asc']},
    scripts=['scripts/quantum-diceware.py']
)
