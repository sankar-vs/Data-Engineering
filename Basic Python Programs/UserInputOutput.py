'''
@Author: Sankar
@Date: 2021-03-31 19:06:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-02 10:02:09
@Title : UserInputOutput
'''
import re
def print_user_name_regex():
    '''
    Description:
        Get input from user, check whether the input is matching with the pattern
        expression, if True then print the greeting message
    Parameter:
        None
    Return:
        None
    '''
    while True:
        try:
            user_name = input("Enter User Name: ")
            pattern = "^[a-zA-Z]{3,}([\\s]?[a-zA-Z]+)*$"
            result = re.match(pattern, user_name)
            if (result):
                print("Hello {}, How are you?".format(user_name))
                break
        except:
            pass
        print("Only alphebets and spaces allowed, and the length has to be atleast 3 characters")    

print_user_name_regex()