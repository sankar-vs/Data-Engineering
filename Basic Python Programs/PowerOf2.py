import sys
def test_range_int(x): 
    '''
    Description:
        Check if the given number is greater than 0 and less than 31
    Parameter:
        x (str): Input from User
    Return:
        x (int)): returns if value is greater than 0 and less than 31
    '''
    if (int(x) > 0 and int(x) < 31): 
        return int(x)  
    else:
        print("Enter number in range between 1 and 30")
num = test_range_int(input("Enter a number: "))
for count in range(1, pow(2, num)+1,1):
    table = count * 2
    if( table > pow(2, num)):
        break
    else:
        print("2 * {} = {}".format(count, table))