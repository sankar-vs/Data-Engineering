'''
@Author: Sankar
@Date: 2021-04-09 10:27:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-09 10:35:09
@Title : Dictionary_Python-13
'''
'''
Write a Python program to count number of items in a dictionary value
that is a list.
'''

dict = {'Days': ["Mon","Tue","wed","Thu"],'time': "2 pm",'Subjects':["Phy","Chem","Maths","Bio"]}
count = 0
for i in dict:
   if isinstance(dict[i], list):
      count += 1
print("In dict {} values having list count is: {}".format(dict, count))