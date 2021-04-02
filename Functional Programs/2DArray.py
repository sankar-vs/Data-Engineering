'''
@Author: Sankar
@Date: 2021-04-01 09:06:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-02 12:16:09
@Title : 2DArray
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
            pattern = "^([1-9][0-9]{,8})$"
            result = re.match(pattern, num)
            if (result):
                return int(num)
        except:
            pass
        print("Only numerics greater than 0")

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
            pattern = "^([+-]?[0-9]{,9})$"
            result = re.match(pattern, num)
            if (result):
                return int(num)
        except:
            pass
        print("Only numeric integer")

def create_matrix(rows, columns):
    '''
    Description:
        Create a 2D array from the given rows and columns
    Parameter:
        rows (int)): A integer
        columns (int)): A integer
    Return:
        matrix (list[][]): matrix populated by the user
    '''
    matrix = []
    try:
        for i in range(rows):
            a = []
            for j in range(columns):
                a.append(num_regex_int("Enter element: "))
            matrix.append(a)    
        return matrix
    except:
        print("Check the values for rows and columns")  

def print_matrix(matrix):
    '''
    Description:
        Prints the given 2D array
    Parameter:
        matrix (list[][]): Integer elements array
    Return:
        None
    '''
    try:
        rows = len(matrix)
        columns = len(matrix[0])
        for i in range(rows):
            for j in range(columns):
                print(matrix[i][j], end = " ")
            print()
    except:
        print("Check the values for rows and columns")

row = num_regex("Enter number of rows: ")
column = num_regex("Enter number of columns: ")
array = create_matrix(row, column)  
print_matrix(array)