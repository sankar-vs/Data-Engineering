'''
@Author: Sankar
@Date: 2021-04-16 08:15:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-16 08:20:09
@Title : Matplotlib_Python-5
'''
'''
Write a Python program to plot two or more lines on same plot with suitable legends of each
line.
'''
from matplotlib import pyplot as plt

x1 = [1,2,3,4,5]
y1 = [2,5,4,7,6]
plt.plot(x1,y1,label='line1')

x2 = [1,2,3,4,5]
y2 = [4,6,9,8,10]
plt.plot(x2,y2,label='line2')

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Two or more line graphs on same Plot')
plt.legend()
plt.show()