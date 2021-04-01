'''
@Author: Sankar
@Date: 2021-04-01 09:06:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-01 21:45:09
@Title : Sum of 3 Integer Adds to 0
'''
import re
def regex(x):
    '''
    Description:
        Check if it is a positive number by patter matching 
    Parameter:
        x (str)): String from input
    Return:
        x (int)): returns if it is a integer
    '''
    pattern = "^[0-9]+$"
    result = re.match(pattern, x)
    if (result):
        return int(x)
    else:
        print("Please a Enter Integer")  

def test_greater_than_4(x):
    '''
    Description:
        Check if the given number is greater than 4
    Parameter:
        x (int)): A integer
    Return:
        x (int)): returns if value is greater than 4
    '''    
    if int(x) > 4: 
        return int(x)  
    else:
        print("Enter number greater that 4")

def get_array():
    '''
    Description:
        Get the length of the array and populate the elements in the array
    Parameter:
        None
    Return:
        array (list): returns the populated array
    '''
    length = test_greater_than_4(regex(input("Enter the length of the array: ")))        
    array = []
    try:
        for i in range(length):
            array.append(int(input("Enter Element: ")))
        print(array)
        return array
    except (TypeError, ValueError):
        print("Enter Integers")
    
def find_triplets(array):
    '''
    Description:
        Finds the triplets where the sum of them is 0
    Parameter:
        array (list): Integer elements
    Return:
        None
    '''
    flag = 0
    try:
        for i in range(len(array)-2):
            for j in range(i+1, len(array)-1):
                for k in range(j+1, len(array)):
                    if ( (array[i]+array[j]+array[k]) == 0):
                        print("{}, {}, {}".format(array[i], array[j], array[k]))
                        flag = 1
        if flag == 0:
            print("Sum of Three integers adds to ZERO did not exists")
    except TypeError:
        pass

array = get_array()
find_triplets(array)