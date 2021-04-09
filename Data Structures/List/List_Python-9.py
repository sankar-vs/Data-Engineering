'''
@Author: Sankar
@Date: 2021-04-09 12:43:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-09 12:50:09
@Title : List_Python-9
'''
'''
Write a Python function that takes two lists and returns True if they have at
least one common member.
'''

def equalList(list1, list2):
    '''
    Description:
        function that takes two lists and returns True if they have at
        least one common member.
    Parameter:
        list1 (list)
        list2 (list)
    Return
        boolean (True or False)
    '''
    for i in list1:
        for j in list2:
            if (i==j):
                return True
    return False

list1 = [1,2,3,4,5,6,7]
list2 = [0,1]
list3 = [9,10]
print("list1 {} and list2{} is common: {}".format(list1, list2, equalList(list1,list2)))
print("list1 {} and list3{} is common: {}".format(list1, list3, equalList(list1,list3)))