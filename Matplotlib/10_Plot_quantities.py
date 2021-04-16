'''
@Author: Sankar
@Date: 2021-04-16 09:33:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-16 09:45:09
@Title : Matplotlib_Python-10
'''
'''
Write a Python program to plot quantities which have an x and y position.
'''
from matplotlib import pyplot as plt

x1 = [1,2,3,4,5]
y1 = [2,5,4,7,6]
plt.plot(x1,y1,'b*',label='plot1')

x2 = [1,2,3,4,5]
y2 = [4,6,9,8,10]
plt.plot(x2,y2,'ro',label='plot2')
plt.axis([0,7,0,13])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Two or more line graphs on same Plot')
plt.legend()
plt.show()

print(plt.axis())