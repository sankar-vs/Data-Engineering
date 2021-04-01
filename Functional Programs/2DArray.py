'''
@Author: Sankar
@Date: 2021-04-01 09:06:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-01 20:34:09
@Title : 2DArray
'''
def test_positive_integer(x):
    '''
    Description:
        Check if the given number is greater than 0
    Parameter:
        x (int)): A integer
    Return:
        x (int)): returns if value is greater than 0
    '''    
    if int(x) > 0: 
        return int(x)  
    else:
        print("Enter number greater that zero")

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
                a.append(int(input("Enter element: ")))
            matrix.append(a)    
        return matrix
    except TypeError:
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
    except TypeError:
        print("Check the values for rows and columns")

while True:
    try:
        row = test_positive_integer(input("Enter number of rows: "))
        column = test_positive_integer(input("Enter number of columns: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

array = create_matrix(row, column)  
print_matrix(array)