'''
@Author: Sankar
@Date: 2021-04-16 11:11:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-16 11:20:09
@Title : Matplotlib_Python-15
'''
'''
Write a Python program to create multiple plots.
'''
from matplotlib import pyplot as plt

x = [1, 2, 3]
y = [0, 1, 0]
z = [1, 0, 1]

# X = [ (2,3,1), (2,3,2), (2,3,3), (2,1,(2,4))]
# for nrows, ncols, plot_number in X:
#     fig, ax = plt.subplot(nrows, ncols, plot_number)
fig = plt.figure()

ax1 = fig.add_subplot(2,3,1)
ax2 = fig.add_subplot(2,3,2)
ax3 = fig.add_subplot(2,3,3)
ax4 = fig.add_subplot(2,1,(2,4))

ax1.plot(x,y)
ax2.plot(x,z)
ax3.plot(x,y)
ax4.plot(x,z)
plt.show()