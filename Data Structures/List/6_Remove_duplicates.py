'''
@Author: Sankar
@Date: 2021-04-09 12:26:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-09 12:34:09
@Title : List_Python-6
'''
'''
Write a Python program to remove duplicates from a list.
'''
list = [1,2,3,2,1,6,9,10,2,3,4,]
new_list = []
for num in list:
    if num not in new_list:
        new_list.append(num)

print("Removed Duplicates in list: {}".format(new_list))