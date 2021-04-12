'''
@Author: Sankar
@Date: 2021-04-08 13:41:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-08 13:48:09
@Title : Basic_Python-30
'''
'''
Write a Python program to access and print a URL's content to the console.
'''
import requests as req

resp = req.get("https://www.programiz.com/python-programming/docstrings")
print(resp.text)

