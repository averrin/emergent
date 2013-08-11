#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
    name='Project Emergent',
    version='0.1',
    description='Coding anarchy',
    author='*',
    author_email='averrin@gmail.com',
    url='https://github.com/averrin/emergent/',
    packages=find_packages(),
    license='License :: MIT',

    test_suite='setuptest.setuptest.SetupTestSuite',
    tests_require=(
        'django-setuptest',
        'argparse'
    ),
)
