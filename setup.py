#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from djangocms_owl import __version__


INSTALL_REQUIRES = [
    'django-cms>=3.0',
]

CLASSIFIERS = [
    'Development Status :: 5 - Production/Stable',
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Communications',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: Message Boards',
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
]

setup(
    name='djangocms-owl',
    version=__version__,
    description='Plugin for django-cms to create beautiful responsive carousel sliders',
    author='Abhinav Jain',
    author_email='abhinavjain241@gmail.com',
    url='https://github.com/abhinavjain241/djangocms-owl',
    packages=['djangocms_wow', 'djangocms_wow.migrations', 'djangocms_wow.south_migrations'],
    install_requires=INSTALL_REQUIRES,
    license='LICENSE.txt',
    platforms=['OS Independent'],
    classifiers=CLASSIFIERS,
    long_description=open('README.rst').read() + open('CHANGELOG.rst').read(),
    include_package_data=True,
    keywords='django cms owl carousel',
    zip_safe=False,
    test_suite='test_settings.run',
)
