'''
@Author: Sankar
@Date: 2021-04-09 09:06:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-09 09:11:09
@Title : Dictionary_Python-5
'''
'''
Write a Python script to generate and print a dictionary that contains a
number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
'''

n = 5
dict = {}
for i in range(1,n+1):
    dict.update({i:i*i})
print("Dictionary: {}".format(dict))