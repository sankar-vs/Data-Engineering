'''
@Author: Sankar
@Date: 2021-04-09 12:17:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-09 12:25:09
@Title : List_Python-5
'''
'''
Write a Python program to get a list, sorted in increasing order by the last
element in each tuple from a given list of non-empty tuples.
Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
'''
list = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
list.sort(key = lambda x : x[1])
print("Sorted list: {}".format(list))