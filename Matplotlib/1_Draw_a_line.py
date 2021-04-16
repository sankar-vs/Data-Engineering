'''
@Author: Sankar
@Date: 2021-04-16 07:43:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-16 07:47:09
@Title : Matplotlib_Python-1
'''
'''
Write a Python program to draw a line with suitable label in the x axis, y axis and a title
'''
from matplotlib import pyplot as plt
x = range(0,20)
y = [i*3 for i in x]
plt.plot(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Draw Line')
plt.show()