'''
@Author: Sankar
@Date: 2021-04-09 10:06:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-09 10:12:09
@Title : Dictionary_Python-10
'''
'''
Write a Python program to count the values associated with key in a
dictionary.
Sample data: = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':
False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]
Expected result: Count of how many dictionaries have success as True
'''
list = [{'id': 1, 'success': True, 'name': 'Lary'}, {'id': 2, 'success':
False, 'name': 'Rabi'}, {'id': 3, 'success': True, 'name': 'Alex'}]

count = 0
for dict in list:
    if dict['success']:
        count += 1

print("Count of Success values being true: {}".format(count))