'''
@Author: Sankar
@Date: 2021-04-07 19:18:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-07 19:35:09
@Title : Basic_Python-5
'''
'''
Write a Python program to print the calendar of a given month and year.
Note : Use 'calendar' module.
'''
import calendar
month = int(input("Enter month: "))
year = int(input("Enter year: "))
print(calendar.month(year, month))