import sys
def test_range_int(x):       # Ensure it is a positive Integer
    if (int(x) > 0): 
        return int(x)  
    else:
        sys.exit("Enter Positive Integer")
# To get the elements in the array
def create_array(rows, columns):
    array = [[0 for i in range(rows)] for j in range(columns)]
    for i in range(rows):
        for j in range(columns):
            array[i][j] = int(input("Enter element: "))
    return array
# To print the array
def print_array(array):
    rows = len(array)
    columns = len(array[0])
    for i in range(rows):
        for j in range(columns):
            print(array[i][j], end = " ")
        print()

row = test_range_int(input("Enter number of rows: "))
column = test_range_int(input("Enter number of columns: "))
array = create_array(row, column)  
print_array(array)