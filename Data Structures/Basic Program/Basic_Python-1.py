'''
@Author: Sankar
@Date: 2021-04-07 18:59:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-07 19:05:09
@Title : Basic_Python-1
'''
'''
Program which accepts the user's first and last name and print them in
reverse order with a space between them.
'''
first_name = input("Enter FirstName: ")
last_name = input("Enter LastName: ")
# Reverse the String
first_name = first_name[::-1]
last_name = last_name[::-1]

print("Reversed FirstName: {}".format(" ".join(first_name)))
print("Reversed LastName: {}".format(" ".join(last_name)))