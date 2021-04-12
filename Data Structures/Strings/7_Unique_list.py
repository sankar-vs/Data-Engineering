'''
@Author: Sankar
@Date: 2021-04-12 07:41:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-12 07:47:09
@Title : Strings_Python-7
'''
'''
Write a Python program that accepts a comma separated sequence of words as input
and prints the unique words in sorted form (alphanumerically).
Sample Words : red, white, black, red, green, black
Expected Result : black, green, red, white,red
'''
words = "red,white,black,red,green,black"
item = [word for word in words.split(",")]
print(sorted(list(set(item))))