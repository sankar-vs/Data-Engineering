import sys
def test_lengthGreater_than_4(x):       # Ensure the length of the array is atleast 5
    if int(x) > 4:
        return int(x)
    else:
        sys.exit("Enter length of the array greater than 4")
# To get elements in the array
def get_Array():
    length = int(input("Enter the length of the array: "))
    array = []
    for i in range(length):
        array.append(int(input("Enter Element: ")))
    print(array)
    return array
# To find the triplets
def find_Triplets(array):
    flag = 0
    for i in range(len(array)-2):
        for j in range(i+1, len(array)-1):
            for k in range(j+1, len(array)):
                if ( (array[i]+array[j]+array[k]) == 0):
                    print("{}, {}, {}".format(array[i], array[j], array[k]))
                    flag = 1
    if flag == 0:
        print("Sum of Three integers adds to ZERO did not exists")

array = get_Array()
find_Triplets(array)