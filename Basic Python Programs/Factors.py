import sys
def test_not_zero(x):       # Ensure it is a positive Integer
    if int(x) != 0:
        return int(x)  
    else:
        sys.exit("Enter number greater that zero")
num = test_not_zero(input("Enter a number: "))
print("Prime Factors of {} are: ".format(num), end = " ")
while num % 2 == 0:
    print(2, end = " ")
    num = int (num / 2)
for count in range(3, num+1, 2):
    while num % count == 0:
        print(count, end = " ")
        num = int(num / count)
if num > 2:
    print(num, end = " ")