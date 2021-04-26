'''
@Author: Sankar
@Date: 2021-04-07 21:44:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-07 21:52:09
@Title : Basic_Python-10
'''
'''
Write a Python program to print out a set containing all the colors from color_list_1 which
are not present in color_list_2.
Test Data :
color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])
'''

color_list_1 = set(["White", "Black", "Red"])
color_list_2 = set(["Red", "Green"])

color_list_3 = color_list_1.difference(color_list_2)
print(color_list_3)