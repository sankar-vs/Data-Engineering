'''
@Author: Sankar
@Date: 2021-04-10 06:50:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-10 06:58:09
@Title : List_Python-10
'''
'''
Write a Python program to print a specified list after removing the 0th, 4th and
5th elements.
Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected Output : ['Green', 'White', 'Black']
'''
list = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
for i in (5,4,0):
    list.pop(i)

print("List {}".format(list))
