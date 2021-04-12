'''
@Author: Sankar
@Date: 2021-04-08 15:20:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-08 15:27:09
@Title : Basic_Python-41
'''
'''
Write a Python program to convert an integer to binary keep leading zeros.
Sample data : 50
Expected output : 00001100, 0000001100
'''

decimal = 50
print("Convertion to binary from {} is: {:08b}".format(decimal, decimal))
print("Convertion to binary from {} is: {:010b}".format(decimal, decimal))
print("Convertion to binary from {} is: {:012b}".format(decimal, decimal))