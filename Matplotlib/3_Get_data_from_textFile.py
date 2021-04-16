'''
@Author: Sankar
@Date: 2021-04-16 07:49:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-16 07:55:09
@Title : Matplotlib_Python-3
'''
'''
Write a Python program to draw a line using given axis values taken from a text file, with
suitable label in the x axis, y axis and a title.
Test Data:
test.txt
1 2
2 4
3 1
'''
from matplotlib import pyplot as plt
import csv

x = []
y = []
with open('Matplotlib/resurces/test.txt', 'r') as f:
    data = csv.reader(f, delimiter = ' ')
    for i in data:
        x.append(i[0])
        y.append(i[1])   

print(data)


plt.plot(x,y)
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.title('Line Graph')
plt.show()