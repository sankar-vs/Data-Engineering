# Function to calculate the Euclidean distance
def calculate_Euclidean_Dsitance():
    x = int(input("Enter x co-ordinate: "))
    y = int(input("Enter y co-ordinate: "))
    distance = pow(x,x)+pow(y,y)
    print("Euclidean distance from the point ({}, {}) to the origin (0, 0) is: {}".format(x, y, distance))

calculate_Euclidean_Dsitance()