#!/usr/bin/env python

import os
from setuptools import setup

__version__ = '1.0'


long_description = ''
if os.path.exists('README.md'):
    with open('README.md', 'r') as f:
        long_description = f.read()


setup(name='pysga',
      version=__version__,
      description='Search Group Algorithm metaheuristic optimization method python adaptation',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='André Ginklings',
      author_email='andre.ginklings@gmail.com',
      url='https://github.com/Ginklings/pysga',
      keywords='metaheuristic optimization algorithm',
      classifiers=[
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Operating System :: OS Independent',
          'Topic :: Scientific/Engineering'],
      packages=['pysga'],
      install_requires=['numpy'],
      extras_require={'full': ['kivy']}
      )
