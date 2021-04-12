'''
@Author: Sankar
@Date: 2021-04-08 14:33:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-08 14:38:09
@Title : Basic_Python-37
'''
'''
Write a Python program to empty a variable without destroying it.
Sample data: n=20
d = {"x":200}
Expected Output : 0
{}
'''

n = 20
d = {"x":200}
print("Value: {}".format(type(d)()))
print("Value: {}".format(type(n)()))