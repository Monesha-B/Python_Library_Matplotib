# Matplotlib basics - line plotting

# In order to do that need to install matplotlib using cmd(pip3 or pip install matplotlib)

#import relevant modules

import matplotlib.pyplot as mat_plot
import numpy as numpy

# creating an simple arrays(similar to lists)
# x = numpy.array([0,100])

# to see the output and type of x for self
# print(x)
# print(type(x))

# y = numpy.array([0,10])

# to plot
# mat_plot.plot(y,x) can be used to view vice versa. mat_plot.plot(y,y) mat_plot.plot(x,x)
# First argument x is x axis and second argument y is y axis
# mat_plot.plot(x,y)

# to show the graph matplolib_variable.show() needs to be used i.e.., mat_plot.show()
# mat_plot.show()

#Each numpy arrays should be in same length
# File "C:\Users\Hp\AppData\Roaming\Python\Python312\site-packages\matplotlib\axes\_base.py", line 499, in _plot_args
# raise ValueError(f"x and y must have same first dimension, but "
# ValueError: x and y must have same first dimension, but have shapes (7,) and (6,) """
# x = numpy.array([10,10,10,50,90,90,90])
# y = numpy.array([10,30,50,30,50,30])

x = numpy.array([10,10,10,50,90,90,90])
y = numpy.array([10,30,50,30,50,30,10])

# mat_plot.plot(x,y)
# mat_plot.show()

# to show scattered graph instead of a line graph
# method 1 
# 'go' green dots similarly 'bo', 'p' etc are markers, line styles, colors ---> https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html#matplotlib.axes.Axes.plot

# mat_plot.plot(x,y,'go')
# mat_plot.show()

mat_plot.scatter(x, y)
mat_plot.show()
