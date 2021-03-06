# pysga
A python adaptation to matlab Search Group Algorithm code

The Search Group Algorithm (SGA) is a metaheuristic optimization method for nonlinear, nonconvex, nonsmooth, multimodal, bounded optimization problems. You may also find a tutorial in a pdf file, which is a step by step explanation about how to use the SGA code.
The sections and equations cited in this file refer to the paper that presented the SGA:
M.S. Gonçalves, R.H. Lopez, L.F.F. Miguel, “Search group algorithm: A new metaheuristic method for the optimization of truss structures”, Computers & Structures, 153:165-184, 2015. DOI: 0.1016/j.compstruc.2015.03.003
This paper may also be download at Research Gate:

https://www.researchgate.net/publication/274253521_Search_group_algorithm_A_new_metaheuristic_method_for_the_optimization_of_truss_structures

or from science direct at:

http://www.sciencedirect.com/science/article/pii/S0045794915000851

The m-files original codes is provide from https://www.mathworks.com/matlabcentral/fileexchange/50598-search-group-algorithm-matlab-code

## Installation:

### Requeriments:
Actually is working in python 3.x. The following modules are necessary:
* numpy (all)
* kivy (for app only)

### Install
Use pip to install. For only the function without GUI App:
```bash
pip install pysga
```

This will install numpy if necessary.

For GUI App:
```bash
pip install pysga[full]
```

This will install the kivy module and dependencies. For any error, consult de kivy documentation.

## App example:
```python
from pysga.sgaApp import SearchGroupAlgorithmApp
from kivy.config import Config
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '600')
app = SearchGroupAlgorithmApp()
app.run()
```

Put a "fobj_function.py" file in current directory and define your objective function as "fobj" function. Example:

```python
import numpy as np


# Example function
def fobj(x):
    y = np.zeros((x.shape[0], 1))
    s1 = np.zeros(x.shape[0])
    s2 = np.zeros(x.shape[0])
    for i in range(5):
        n = i + 1
        s1 = s1 + n * np.cos((n + 1) * x[:, 0] + n)
        s2 = s2 + n * np.cos((n + 1) * x[:, 1] + n)
    y[:, 0] = s1 * s2
    return y
```

The "x" variable is entry for the objective function with shape (SearchSize, n).
SearchSize is the size of the optimization algorithm search group and n is the objective function dimension.

When run the app, choose the "from file" option and run the optimizer.

![Alt text](OptimizationParams.png?raw=true "Pameters of SGA optimizer")

![Alt text](FunctionParams.png?raw=true "Function configuration")

## Call SGA in python code:

It is really simple. Just import the module and then configure the SGA parameters, the function and run:

```python
import pysga


# Define your fobj function:
def my_fobj(x):
    pass


# define the objective function class with your lower and upper bounds:
# inf and sup should be a numpy array
f = pysga.ObjectiveFunc(inf=my_inf, sup=mysup)

# overwrite evaluate with your objective function:
f.evaluate = my_fobj

# set the sga parameters, without setting the defaults values will be used
sga_params = pysga.ParamsSGA()

# run the SGA optimization:
x, y = pysga.run(sga=sga_params, fobj=f)

# with SGA's defaults parameters you can hide the sga class:
# x, y = pysga.run(fobj=f)

print('The minimun value of the function is %s at point %s' % (y, x))
```
