#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: tabstop=4 expandtab shiftwidth=4 softtabstop=4

# pylint: disable=no-name-in-module
# pylint: disable=import-error

"""
Setup Script
"""

from setuptools import setup
from unittest_prettify import __title__, __version__, __description__, __author__, __author_email__, __license__

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()
REQUIRED = []

setup(name=__title__,
      version=__version__,
      description=__description__,
      author=__author__,
      author_email=__author_email__,
      license=__license__,
      url='https://github.com/jonathadv/unittest_prettify',
      packages=['unittest_prettify'],
      install_requires=REQUIRED,
      python_requires=">=3.5.*",
      long_description=LONG_DESCRIPTION,
      long_description_content_type="text/markdown",
      classifiers=[
          'Development Status :: 4 - Beta',
          'Intended Audience :: Developers',
          'Natural Language :: English',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: Implementation :: CPython',
      ]
)
