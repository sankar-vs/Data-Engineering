import sys
def test_not_zero(x):       # Ensure it is a positive Integer
    if int(x) != 0: 
        return int(x)  
    else:
        sys.exit("Enter number greater that zero")
num = test_not_zero(input("Enter a number: "))
harmonic = 0
for count in range(1, num+1, 1):
    div = (1/count)
    harmonic += div
print("The {}th Harmonic number: {}".format(num, harmonic))