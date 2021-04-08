'''
@Author: Sankar
@Date: 2021-04-08 13:03:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-08 13:15:09
@Title : Basic_Python-22
'''
'''
Write a Python program to get the command-line arguments (name of the script, the number
of arguments, arguments) passed to a script.
'''
import sys

# Count the arguments
arguments = len(sys.argv) - 1

# Output argument-wise
position = 1
while (arguments >= position):
    print ("Parameter {}: {}".format(position, sys.argv[position]))
    position = position + 1