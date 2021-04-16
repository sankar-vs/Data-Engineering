'''
@Author: Sankar
@Date: 2021-04-16 09:08:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-16 09:12:09
@Title : Matplotlib_Python-8
'''
'''
Write a Python program to plot two or more lines and set the line markers.
'''
from matplotlib import pyplot as plt

x1 = [1,2,3,4,5]
y1 = [2,5,4,7,6]
plt.plot(x1,y1,color='green',linewidth=3,label='line1',linestyle='dotted',marker='o', markerfacecolor='blue',markersize=10)

x2 = [1,2,3,4,5]
y2 = [4,6,9,8,10]
plt.plot(x2,y2,color='red',linewidth=2,label='line2',linestyle='dashdot',marker='x', markerfacecolor='blue',markersize=12)

plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Two or more line graphs on same Plot')
plt.legend()
plt.show()