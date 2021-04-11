'''
@Author: Sankar
@Date: 2021-04-11 12:38:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-11 12:45:09
@Title : Strings_Python-4
'''
'''
Write a Python program to add 'ing' at the end of a given string (length should be at
least 3). If the given string already ends with 'ing' then add 'ly' instead. If the string length of the

given string is less than 3, leave it unchanged.
Sample String : 'abc'
Expected Result : 'abcing'
Sample String : 'string'
Expected Result : 'stringly'
'''
string1 = "abc"
string2 = "string"

def checkString(string):
    check = "ing"
    if(len(string)>2):
        if(string[-3:] == check):
            return string + "ly"
        else:
            return string + "ing"
    else:
        return string

print("{} : {}".format(string1, checkString(string1)))
print("{} : {}".format(string2, checkString(string2)))