import re

def name_regex(name):
    '''
    Description:
        Get input from user, check whether the input is matching with the pattern
        expression, if True then return
        checks whether the entered phone number is valid or not. If valid it returns boolean
    Parameter:
        name (str): Statement to be asked
    Return:
        result (boolean)
    '''
    try:
        pattern = "^[A-Z]{1}[a-zA-Z]{2,}$"
        result = re.match(pattern, name)
        return bool(result)
    except:
        raise Exception("Input invalid")   

def phone_regex(phone):
    '''
    Description:
        Get input from user, check whether the input is matching with the pattern
        expression, if True then return
        checks whether the entered phone number is valid or not. If valid it returns boolean
    Parameter:
        x (str): Statement to be asked
    Return:
        result (boolean)
    '''
    try:
        pattern = "^[0-9]{2}\\s[7-9][0-9]{9}$"
        result = re.match(pattern, phone)
        return bool(result)
    except:
        raise Exception("Input invalid")  

def email_regex(email):
    '''
    Description:
        Get input from user, check whether the input is matching with the pattern
        expression, if True then return
        checks whether the entered email is valid or not. If valid it returns boolean
    Parameter:
        x (str): Statement to be asked
    Return:
        result (boolean)
    '''
    try:
        pattern = "^[a-z0-9]+(\\.[_a-z0-9]+)*(\\-[_a-z0-9]+)*(\\+[_a-z0-9]+)*[@]{1}[^.][a-z0-1]*[.]{1}[a-z]{3}(\\.[a-z]{2,4}){0,1}$"
        result = re.match(pattern, email)
        return bool(result)
    except:
        raise Exception("Input invalid")  

def password_regex(password):
    '''
    Description:
        Get input from user, check whether the input is matching with the pattern
        expression, if True then return
        checks whether the entered password is valid or not. If valid it returns boolean    
    Parameter:
        x (str): Statement to be asked
    Return:
        result (boolean)
    '''
    
    try:
        pattern = "^(?=.{8,}$)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])(?=.*?[!@#$%^&*])(?!.*[!@#$%^&*].*[!@#$%^&*]).*$"
        result = re.match(pattern, password)
        return bool(result)
    except:
        raise Exception("Input invalid")  

def login():
    try:
        firstName = input("Enter First Name: ")
        lastName = input("Enter Last Name: ")
        phone_number = input("Enter Phone Number: ")
        email = input("Enter your email: ")
        password = input("Set your Password: ")
        if (name_regex(firstName)):
            print("First Name: ",firstName)
        if (name_regex(lastName)):
            print("Last Name: ",lastName)
        if (phone_regex(phone_number)):
            print("Phone Number: ",phone_number)
        if (email_regex(email)):
            print("Email: ",email)
        if (password_regex(password)):
            print("Set Password: ",password)
    except:
        raise Exception("Program has stopped working")