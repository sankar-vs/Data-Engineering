'''
@Author: Sankar
@Date: 2021-04-09 12:11:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-09 12:15:09
@Title : List_Python-4
'''
'''
Write a Python program to count the number of strings where the string length
is 2 or more and the first and last character are same from a given list of strings.
Sample List : ['abc', 'xyz', 'aba', '1221']
Expected Result : 2
'''
list = ['abc', 'xyz', 'aba', '1221']
count = 0
for i in list:
    if ((len(i) > 2) and (i[0] == i[-1])):
        count += 1

print("The count of strings where the string length is 2 or more and the first and last character are: ", count)