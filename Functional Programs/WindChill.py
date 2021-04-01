import sys
def test_lesserThan_50(x):       # Ensure it is less than 50
    if (float(x) < 50): 
        return float(x)  
    else:
        sys.exit("Enter temperature less than 50")

def test_velocity_inRange(x):       # Ensure it is between 3 and 120
    if (float(x) < 120 and float(x) > 3): 
        return float(x)  
    else:
        sys.exit("Enter wind speed between 3 and 120")

t = test_lesserThan_50(input("Enter temperature (in Fahrenheit): "))
v = test_velocity_inRange(input("Enter wind speed (in miles/hour): "))
# w = 35.74+(0.6215*t)+(0.4275*t - 35.75)*(v**0.16)
windChill = 35.74 + (0.6215*t) + ((0.4275*t) - 35.75)*pow(v,0.16)
print("The effective Temperature for give t {}F and wind speed {}v is: {}".format(t,v,windChill))