'''
@Author: Sankar
@Date: 2021-04-12 08:23:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-12 08:27:09
@Title : Sets_Python-11
'''
'''
Write a Python program to use of frozensets.
'''
x = frozenset([1, 2, 3, 4, 5])
y = frozenset([3, 4, 5, 6, 7])

print(x.isdisjoint(y))
print(x.difference(y))
print(x.union(y))