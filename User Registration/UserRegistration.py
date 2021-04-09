import re
import logging

def name_regex(x):
    '''
    Description:
        Get input from user, check whether the input is matching with the pattern
        expression, if True then return
        checks whether the entered phone number is valid or not. If valid it returns the string
    Parameter:
        x (str): Statement to be asked
    Return:
        name (str): input from user
    '''
    while True:
        try:
            name = input(x)
            pattern = "^[A-Z]{1}[a-zA-Z]{2,}$"
            result = re.match(pattern, name)
            if (result):
                return str(name)
        except:
            pass
        logging.warning("Enter proper Name")

def phone_regex(x):
    '''
    Description:
        Get input from user, check whether the input is matching with the pattern
        expression, if True then return
        checks whether the entered phone number is valid or not. If valid it returns the string
    Parameter:
        x (str): Statement to be asked
    Return:
        phone (str): input from user
    '''
    while True:
        try:
            phone = input(x)
            pattern = "^[0-9]{2}\\s[0-9]{10}$"
            result = re.match(pattern, phone)
            if (result):
                return str(phone)
        except:
            pass
        logging.warning("Enter proper Number")

def email_regex(x):
    '''
    Description:
        Get input from user, check whether the input is matching with the pattern
        expression, if True then return
        checks whether the entered email is valid or not. If valid it returns the string
    Parameter:
        x (str): Statement to be asked
    Return:
        email (str): input from user
    '''
    while True:
        try:
            email = input(x)
            pattern = "^[a-z0-9]+(\\.[_a-z0-9]+)*(\\-[_a-z0-9]+)*(\\+[_a-z0-9]+)*[@]{1}[^.][a-z0-1]*[.]{1}[a-z]{3}(\\.[a-z]{2,4}){0,1}$"
            result = re.match(pattern, email)
            if (result):
                return str(email)
        except:
            pass
        logging.warning("Enter proper email")

def password_regex(x):
    '''
    Description:
        Get input from user, check whether the input is matching with the pattern
        expression, if True then return
        checks whether the entered password is valid or not. If valid it returns the string
        
        Rule:1 minimum 8 characters (?=.{8,}) or ^[A-Za-z0-9].{8,}$
        ^[A-Za-z0-9].{8,}$
        Rule:2 Should have atleast 1 Uppercase ^(?=.?[A-Z])
        ^(?=.?[A-Z])[A-Za-z0-9].{8,}$
        Rule:3 Should have atleast 1 numeric ^(?=.?[0-9]) or (?=.*\d)
        ^((?=.*[A-Z])(?=.*[0-9]))[A-Za-z0-9].{8,}$
        Rule:4 Should have atleast 1 special character (?=.?[@$!%*#?&])
        ^((?=.?[A-Z])(?=.?[0-9])(?=.?[@$!%*#?&]))[A-Za-z0-9].{8,}$
    Parameter:
        x (str): Statement to be asked
    Return:
        password (str): input from user
    '''
    while True:
        try:
            password = input(x)
            pattern = "^(?=.{8,}$)(?=.*?[a-z])(?=.*?[A-Z])(?=.*?[0-9])(?=.*?[!@#$%^&*])(?!.*[!@#$%^&*].*[!@#$%^&*]).*$"
            result = re.match(pattern, password)
            if (result):
                return str(password)
        except:
            pass
        logging.warning("Enter proper password")

def login():
    try:
        firstName = name_regex("Enter First Name: ")
        lastName = name_regex("Enter Last Name: ")
        phone_number = phone_regex("Enter Phone Number: ")
        email = email_regex("Enter your email: ")
        password = password_regex("Set your Password: ")

        print("The Details entered by you are: \nFirstName: {}\nLastName: {}\nPhone: {}\nEmail: {}\nPassword: {}".format(firstName, lastName, phone_number, email, password))

    except:
        raise Exception("Program has stopped working")

login()
