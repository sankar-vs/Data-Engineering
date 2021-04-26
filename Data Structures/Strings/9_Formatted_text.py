'''
@Author: Sankar
@Date: 2021-04-12 07:53:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-12 07:57:09
@Title : Strings_Python-9
'''
'''
Write a Python program to display formatted text (width=50) as output.
'''
import textwrap
sample_text = '''
  Python is a widely used high-level, general-purpose, interpreted,
  dynamic programming language. Its design philosophy emphasizes
  code readability, and its syntax allows programmers to express
  concepts in fewer lines of code than possible in languages such
  as C++ or Java.
  '''
print(textwrap.fill(sample_text, width=50))