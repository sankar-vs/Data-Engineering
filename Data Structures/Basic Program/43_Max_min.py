'''
@Author: Sankar
@Date: 2021-04-08 15:30:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-08 15:35:09
@Title : Basic_Python-43
'''
'''
Write a Python function to find the maximum and minimum numbers from a sequence of
numbers.
Note: Do not use built-in functions.
'''

list = [9,10,50,65,3,1,100,150,2,65,1]
max = list[0]
min  = list[0]
for i in list:
    if i > max:
        max = i
    else:
        min = i

print("Largest in list {} is: {}".format(list, max))
print("Largest in list {} is: {}".format(list, min))