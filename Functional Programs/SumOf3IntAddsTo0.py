'''
@Author: Sankar
@Date: 2021-04-01 09:06:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-02 12:37:09
@Title : Sum of 3 Integer Adds to 0
'''
import re
def num_regex(x):
    '''
    Description:
        Get input from user, check whether the input is matching with the pattern
        expression, if True then return
    Parameter:
        x (str) : Statement to be printed to take the the inputs from user
    Return:
        num (int): input from user
    '''
    while True:
        try:
            num = input(x)
            pattern = "^([5-9][0-9]{,8})$"
            result = re.match(pattern, num)
            if (result):
                return int(num)
        except:
            pass
        print("Enter number greater that 4")

def num_regex_int(x):
    '''
    Description:
        Get input from user, check whether the input is matching with the pattern
        expression, if True then return
    Parameter:
        x (str) : Statement to be printed to take the the inputs from user
    Return:
        num (int): input from user
    '''
    while True:
        try:
            num = input(x)
            pattern = "^([+-]?[0-9]{,8})$"
            result = re.match(pattern, num)
            if (result):
                return int(num)
        except:
            pass
        print("Only numeric integer")

def get_array():
    '''
    Description:
        Get the length of the array and populate the elements in the array
    Parameter:
        None
    Return:
        array (list): returns the populated array
    '''
    try:
        length = num_regex("Enter the length of the array: ")      
        array = []
        for i in range(length):
            array.append(num_regex_int("Enter Element: "))
        print(array)
        return array
    except:
        pass
    
def find_triplets(array):
    '''
    Description:
        Finds the triplets where the sum of them is 0
    Parameter:
        array (list): Integer elements
    Return:
        None
    '''
    try:
        flag = 0
        for i in range(len(array)-2):
            for j in range(i+1, len(array)-1):
                for k in range(j+1, len(array)):
                    if ( (array[i]+array[j]+array[k]) == 0):
                        print("{}, {}, {}".format(array[i], array[j], array[k]))
                        flag = 1
        if flag == 0:
            print("Sum of Three integers adds to ZERO did not exists")
    except:
        pass

array = get_array()
find_triplets(array)