import sys
def test_four_digit_number(x):       # Ensure it is a 4 digit number
    if (len(x) == 4 and int(x) > 0): 
        return int(x)  
    else:
        sys.exit("Enter 4 digit number")

year = test_four_digit_number(input("Enter year: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("{} is a leap year".format(year))
       else:
           print("{} is not a leap year".format(year))
   else:
       print("{} is a leap year".format(year))
else:
   print("{} is not a leap year".format(year))