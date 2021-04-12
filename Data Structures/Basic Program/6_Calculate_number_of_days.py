'''
@Author: Sankar
@Date: 2021-04-07 19:35:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-07 19:50:09
@Title : Basic_Python-6
'''
'''
Write a Python program to calculate number of days between two dates.
Sample dates : (2014, 7, 2), (2014, 7, 11)
Expected output : 9 days
'''
from datetime import date, datetime
firstDate = input("Enter first Date (YYYY,MM,dd): ")
lastDate = input("Enter last Date (YYYY,MM,dd): ")
firstDate = datetime.strptime(firstDate, "%Y,%m,%d").date()
lastDate = datetime.strptime(lastDate, "%Y,%m,%d").date()
difference = lastDate - firstDate
print("Number of Days: {}".format(difference))