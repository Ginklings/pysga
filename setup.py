#!/usr/bin/env python

import os
from setuptools import setup

__version__ = '1.2.3'


long_description = ''
if os.path.exists('README.md'):
    try:
        import pypandoc
        long_description = pypandoc.convert('README.md', 'rst')
    except(IOError, ImportError):
        long_description = open('README.md', 'r', encoding='utf8').read()


setup(name='pysga',
      version=__version__,
      description='Search Group Algorithm metaheuristic optimization method python adaptation',
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
      include_package_data=True,
      install_requires=['numpy'],
      extras_require={'full': ['docutils',
                               'pygments',
                               'pypiwin32',
                               'kivy_deps.sdl2==0.1.22',
                               'kivy_deps.glew==0.1.12',
                               'kivy_deps.gstreamer==0.1.17',
                               'kivy_deps.angle==0.1.9',
                               'kivy']}
      )
