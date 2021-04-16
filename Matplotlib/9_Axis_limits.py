'''
@Author: Sankar
@Date: 2021-04-16 09:14:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-16 09:18:09
@Title : Matplotlib_Python-9
'''
'''
Write a Python program to display the current axis limits values and set new axis values.
'''
from matplotlib import pyplot as plt

x1 = [1,2,3,4,5]
y1 = [2,5,4,7,6]
plt.plot(x1,y1,color='green',linewidth=3,label='line1',linestyle='dotted',marker='o', markerfacecolor='blue',markersize=10)

x2 = [1,2,3,4,5]
y2 = [4,6,9,8,10]
plt.plot(x2,y2,color='red',linewidth=2,label='line2',linestyle='dashdot',marker='x', markerfacecolor='blue',markersize=12)
plt.axis([0,7,0,13])
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Two or more line graphs on same Plot')
plt.legend()
plt.show()

print(plt.axis())