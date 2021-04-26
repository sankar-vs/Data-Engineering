'''
@Author: Sankar
@Date: 2021-04-09 09:13:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-09 09:17:09
@Title : Dictionary_Python-6
'''
'''
Write a Python program to remove a key from a dictionary.
'''
dict = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
for i in dict.keys():
    if i == 2:
        del dict[i]
        break

dict.pop(4)
print("Dictionary: ", dict)