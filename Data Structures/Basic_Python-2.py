'''
@Author: Sankar
@Date: 2021-04-07 18:59:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-07 19:05:09
@Title : Basic_Python-2
'''
'''
Python program which accepts a sequence of comma-separated numbers from user
and generate a list and a tuple with those numbers.
'''

values = input("Comma Seperated numbers: ")
list = values.split(",")
tuple = tuple(list)

print("List :{}".format(list))
print("Tuple :{}1,2,3,".format(tuple))