'''
@Author: Sankar
@Date: 2021-04-08 07:42:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-08 07:50:09
@Title : Basic_Python-17
'''
'''
Write a program to get execution time for a Python method.
'''
import time
start_time = time.time()
for i in range(1000000):
    continue
end_time = time.time()
print('Duration: {}'.format(end_time - start_time))