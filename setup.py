#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='djde',
    version='1.0',
    description="",
    author="Deutscher Django-Verein e.V.",
    author_email='kontakt@django-de.org',
    url='',
    packages=find_packages(),
    package_data={'djde': ['static/*.*', 'templates/*.*']},
    scripts=['manage.py'],
)
