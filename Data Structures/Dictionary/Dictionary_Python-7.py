'''
@Author: Sankar
@Date: 2021-04-09 09:17:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-09 09:28:09
@Title : Dictionary_Python-7
'''
'''
Write a Python program to print all unique values in a dictionary.
Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
{"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
'''
list = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
set = set(value for dict in list for value in dict.values())
print("Unique Values: ", set)