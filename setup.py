#!/usr/bin/env python
from distutils.core import setup
from glob import glob

from setuptools import setup, find_packages

setup(name='Py Katas',
      version='1.0',
      description='Python Code Katas',
      author='Albert Luganga',
      packages=find_packages('src'),
      package_dir={'': 'src'},
     )