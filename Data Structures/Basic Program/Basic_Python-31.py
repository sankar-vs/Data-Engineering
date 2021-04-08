'''
@Author: Sankar
@Date: 2021-04-08 13:49:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-08 13:58:09
@Title : Basic_Python-31
'''
'''
Write a Python program to get system command output.
'''
import subprocess
import os

cmd = "git --version"
returned_value = os.system(cmd)
print('returned value:', returned_value)

cmd = "git --version"
returned_value = subprocess.call(cmd, shell=True)
print('returned value:', returned_value)

returned_value = subprocess.check_output("dir", shell=True, universal_newlines=True)
print(returned_value)