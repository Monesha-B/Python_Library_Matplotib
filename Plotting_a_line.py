# Matplotlib basics - line plotting

# In order to do that need to install matplotlib using cmd(pip3 or pip install matplotlib)

#import relevant modules

import matplotlib.pyplot as mat_plot
import numpy as numpy

# creating an simple arrays(similar to lists)
x = numpy.array([0,100])

# to see the output and type of x for self
print(x)
print(type(x))

y = numpy.array([0,10])

# to plot
# mat_plot.plot(y,x) can be used to view vice versa. mat_plot.plot(y,y) mat_plot.plot(x,x)
# First argument x is x axis and second argument y is y axis
mat_plot.plot(x,y)

# to show the graph matplolib_variable.show() needs to be used i.e.., mat_plot.show()

mat_plot.show()

