'''
@Author: Sankar
@Date: 2021-04-08 14:25:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-08 14:30:09
@Title : Basic_Python-35
'''
'''
Write a Python program to get numbers divisible by fifteen from a list using an anonymous
function.
'''

my_list = [45,150,98,75,95,65]
result = list(filter(lambda x: (x % 15 == 0), my_list))

print("Numbers divisible by 15 are: {}".format(result))