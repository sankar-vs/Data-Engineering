'''
@Author: Sankar
@Date: 2021-04-09 08:24:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-09 08:36:09
@Title : Dictionary_Python-1
'''
'''
Write a Python script to sort (ascending and descending) a dictionary by
value.
'''
import operator
dict = {"key1":5, "key2":10,"key3":1,"key4":6,"key5":4}
print("Sort dict by Ascending: {}".format(sorted(dict.items(), key = operator.itemgetter(1))))
print("Sort dict by Descending: {}".format(sorted(dict.items(), key = operator.itemgetter(1), reverse=True)))