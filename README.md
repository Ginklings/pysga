# pysga
A python adaptation to matlab Search Group Algorithm code

The Search Group Algorithm (SGA) is a metaheuristic optimization method for nonlinear, nonconvex, nonsmooth, multimodal, bounded optimization problems. You may also find a tutorial in a pdf file, which is a step by step explanation about how to use the SGA code. The sections and equations cited in this file refer to the paper that presented the SGA: 
M.S. Gonçalves, R.H. Lopez, L.F.F. Miguel, “Search group algorithm: A new metaheuristic method for the optimization of truss structures”, Computers & Structures, 153:165-184, 2015. DOI: 0.1016/j.compstruc.2015.03.003 
This paper may also be download at Research Gate:

https://www.researchgate.net/publication/274253521_Search_group_algorithm_A_new_metaheuristic_method_for_the_optimization_of_truss_structures

or from science direct at:

http://www.sciencedirect.com/science/article/pii/S0045794915000851

The m-files original codes is provide from https://www.mathworks.com/matlabcentral/fileexchange/50598-search-group-algorithm-matlab-code

## Requeriments:
* numpy (all)
* kivy (for app only)

## App example:
```from pysga import SearchGroupAlgorithmApp
from kivy.config import Config
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '600')
app = SearchGroupAlgorithmApp()
app.run()
```
