# Matplotlib basics - line plotting

# In order to do that need to install matplotlib using cmd(pip3 or pip install matplotlib)

#import relevant modules
import matplotlib.pyplot as mat_plot
import numpy as numpy

# creating an simple arrays(similar to lists)
Car_Brands = ['Mini_Cooper', 'BMW', 'Audi', 'Range_Rover', 'Tesla']
Number_available = [50, 10, 5, 20, 15]
Colours1 = ['red', 'yellow', 'blue','purple', 'green'] 

Section_out = ([0.2,0.2,0.2,0.2,0.2])

mat_plot.pie(Number_available, labels = Car_Brands, shadow = True, colors = Colours1, startangle = 90, 
             explode = Section_out)
mat_plot.legend(loc = 'upper left', bbox_to_anchor = (1.15,1.15), title = "Car_Showroom")
mat_plot.show()

