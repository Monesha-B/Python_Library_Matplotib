# Matplotlib basics - line plotting

# In order to do that need to install matplotlib using cmd(pip3 or pip install matplotlib)

#import relevant modules

import matplotlib.pyplot as mat_plot
import numpy as numpy

# creating an simple arrays(similar to lists)
a = numpy.array([0, 10, 5, 20, 15, 30, 25, 40, 35, 50, 100])

# to plot
# mat_plot.plot(y,x) can be used to view vice versa. mat_plot.plot(y,y) mat_plot.plot(x,x)
# First argument x is x axis and second argument y is y axis


# here for x axis it takes 0,1,2...and so on depends on the length of the array listed(considered as y axis as default) above
mat_plot.plot(a, marker = 's')

# to show the graph matplolib_variable.show() needs to be used i.e.., mat_plot.show()

mat_plot.show()





