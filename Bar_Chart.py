# Matplotlib basics - line plotting

# In order to do that need to install matplotlib using cmd(pip3 or pip install matplotlib)

#import relevant modules
from turtle import color
import matplotlib.pyplot as mat_plot
import numpy as numpy

# creating an simple arrays(similar to lists)
Car_Brands = ['Mini_Cooper', 'BMW', 'Audi', 'Range_Rover', 'Tesla']
Number_available = [50, 10, 5, 20, 15]
colours1 = ['red', 'yellow','blue', 'green', 'orange']
# Section_out = ([0.2,0.2,0.2,0.2,0.2]) for pie chart to split and separate

# mat_plot.bar(Car_Brands, Number_available, color = colours1, width=0.5)
mat_plot.barh(Car_Brands, Number_available, color = colours1)
mat_plot.title(loc = 'center', label = 'Car_Showroom')
mat_plot.xlabel('Car_Brands')
mat_plot.ylabel('Number_Available')
mat_plot.show(block=True)

