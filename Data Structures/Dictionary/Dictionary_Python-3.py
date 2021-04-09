'''
@Author: Sankar
@Date: 2021-04-09 08:40:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-09 09:00:09
@Title : Dictionary_Python-3
'''
'''
Write a Python script to concatenate following dictionaries to create a new
one.
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
'''
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4 = {}

for d in (dic1, dic2, dic3):
    dic4.update(d)

print("Dictionary: ", dic4)