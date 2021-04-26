'''
@Author: Sankar
@Date: 2021-04-09 12:36:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-09 12:42:09
@Title : List_Python-8
'''
'''
Write a Python program to find the list of words that are longer than n from a
given list of words.
'''
n  =  3
list = ['Hi','Sankar','How','are','you',"brotha"]
def countWord(n, list):
    '''
    Description:
        To find the list of words that are longer than n from a
        given list of words.
    Parameter:
        n (int)
        list (list)
    Return
        count (int)
    '''
    count = 0
    for i in list:
        if (len(i)>n):
            count += 1
    return count
    
print("From list {} the words that are greater than {} is: {}".format(list, n, countWord(n, list)))