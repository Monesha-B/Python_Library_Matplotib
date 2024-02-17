from matplotlib import colors
import matplotlib.pyplot as mat_plot
import numpy as numpy 

x = numpy.array([1,2,3,4,5])
y = numpy.array([2,3,4,5,6])
Rainbow_colors = numpy.array([1,3,5,7,8])
# mat_plot.plot(x, y)
mat_plot.scatter(x, y, c = Rainbow_colors, cmap = 'rainbow') 
mat_plot.colorbar()
mat_plot.show(block=True)
