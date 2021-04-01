'''
@Author: Sankar
@Date: 2021-04-01 09:06:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-01 21:59:49
@Title : WindChill
'''
def test_less_than_50(x):
    '''
    Description:
        Check if the given number is less than 50
    Parameter:
        x (str): Input from User
    Return:
        x (float): returns if it is less than 50
    '''
    if (float(x) < 50): 
        return float(x)  
    else:
        print("Enter temperature less than 50")

def test_velocity_in_range(x):
    '''
    Description:
        Check if the given number is greater than 3 and less than 120
    Parameter:
        x (str): Input from User
    Return:
        x (float): returns if the condition is true
    '''
    if (float(x) < 120 and float(x) > 3): 
        return float(x)  
    else:
        print("Enter wind speed between 3 and 120")

def calculate_windchill():
    '''
    Description:
        Calculates the WindChill from the temprature (in Fahrenheit) and
        wind speed(in miles/hour) by the given formula
        w = 35.74+(0.6215*t)+(0.4275*t - 35.75)*(v**0.16)
        and prints the output
    Parameter:
        None
    Return:
        None
    '''
    while True:
        try:
            t = test_less_than_50(input("Enter temperature (in Fahrenheit): "))
            v = test_velocity_in_range(input("Enter wind speed (in miles/hour): "))
            break
        except ValueError:
            print("Oops!  That was no valid number.  Try again...") 
    try:
        windChill = 35.74 + (0.6215*t) + ((0.4275*t) - 35.75)*pow(v,0.16)
        print("The effective Temperature for give t {}F and wind speed {}v is: {}".format(t,v,windChill))
    except TypeError:
        print("Check temperature and wind speed values")    

calculate_windchill()