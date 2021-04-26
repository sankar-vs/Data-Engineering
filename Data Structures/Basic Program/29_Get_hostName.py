'''
@Author: Sankar
@Date: 2021-04-08 13:39:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-08 13:41:09
@Title : Basic_Python-29
'''
'''
Write a Python program to get the name of the host on which the routine is running.
'''
import socket
print("HostName: {}".format(socket.gethostname()))