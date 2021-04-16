'''
@Author: Sankar
@Date: 2021-04-16 09:37:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-16 09:45:09
@Title : Matplotlib_Python-11
'''
'''
Write a Python program to plot quantities which have an x and y position.
'''
from matplotlib import pyplot as plt
import numpy as np

x = np.arange(0,5,0.2)
plt.plot(x,x,'g--',label="plot1")
plt.plot(x,x**2,'rs',label="plot2")
plt.plot(x,x**3,'y^',label="plot3")
plt.axis([0,6,0,130])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Line Graph')
plt.legend()
plt.show()
