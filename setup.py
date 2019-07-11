#!/usr/bin/env python

from setuptools import setup

__version__ = '1.2.7'


long_description = ''' pysga

        =====

        

        A python adaptation for matlab Search Group Algorithm code.


        The Search Group Algorithm (SGA) is a metaheuristic optimization method
        for nonlinear, nonconvex, nonsmooth, multimodal, bounded optimization
        problems. You may also find a tutorial in a pdf file, which is a step by
        step explanation about how to use the SGA code. The sections and
        equations cited in this file refer to the paper that presented the SGA:

        M.S. Gonçalves, R.H. Lopez, L.F.F. Miguel, Search group algorithm: A new
        metaheuristic method for the optimization of truss structures, Computers
        & Structures, 153:165-184, 2015. DOI: 0.1016/j.compstruc.2015.03.003

        This paper may also be download at Research Gate:

        https://www.researchgate.net/publication/274253521_Search_group_algorithm_A_new_metaheuristic_method_for_the_optimization_of_truss_structures

        or from science direct at:        

        http://www.sciencedirect.com/science/article/pii/S0045794915000851

        The m-files original codes is provide from:

        https://www.mathworks.com/matlabcentral/fileexchange/50598-search-group-algorithm-matlab-code

        Installation:

        -------------

        Actually is working in python 3.x. The following modules are necessary:

        \* numpy (all)
        \* kivy (for app only)

        Use pip to install. For only the function without GUI App:

        .. code:: bash
        
           pip install pysga

        This will install numpy if necessary.

        For GUI App:

        .. code:: bash
        
           pip install pysga[full]

        This will install the kivy module and dependencies. For any error,
        consult de kivy documentation.

        App example:

        ------------

        .. code:: python

           from pysga.sgaApp import SearchGroupAlgorithmApp

           from kivy.config import Config

           Config.set('graphics', 'width', '500')

           Config.set('graphics', 'height', '600')

           app = SearchGroupAlgorithmApp()

           app.run()

        Put a fobj_function.py file in current directory and define your
        objective function as fobj function.

        When run the app, choose the from file option and run the optimizer.

        Call SGA in python code:

        ------------------------

        See the github website.
'''
# if os.path.exists('README.md'):
#     try:
#         import pypandoc
#         long_description = pypandoc.convert('README.md', 'rst')
#     except(IOError, ImportError):
#         long_description = open('README.md', 'r', encoding='utf8').read()

setup(name='pysga',
      version=__version__,
      description='Search Group Algorithm metaheuristic optimization method python adaptation',
      long_description_content_type='text/markdown',
      long_description=long_description,
      author='André Ginklings',
      author_email='andre.ginklings@gmail.com',
      url='https://github.com/Ginklings/pysga',
      license='LICENSE.txt',
      keywords='metaheuristic optimization algorithm',
      platforms=['Windows', 'Unix'],
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
