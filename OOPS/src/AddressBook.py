'''
@Author: Sankar
@Date: 2021-04-06 09:46:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-06 09:42:09
@Title : AddressBook
'''
import re
import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s')
class Contact:
    '''
    Class:
        Contact

    Description:
        Class to store the contacts firstName, lastName, phone number and email

    Functions:
        getFirstName() -> str
        setFirstName(newFirstName)
        setLastName(newLastName)
        setPhone(newPhone)
        setEmail(newEmail)

    Variable:
        None
    '''
    def __init__(self, firstName, lastName, phone, email):
        self.firstName = firstName
        self.lastName = lastName
        self.phone = phone
        self.email = email

    def __str__(self):
        return self.firstName + "," + self.lastName + "," + self.phone + "," + self.email

    def getFirstName(self):
        '''
        Description:
            Returns FirstName
        Parameter:
            None
        Return:
            firstName (str)
        '''
        return self.firstName

    def getLastName(self):
        '''
        Description:
            Returns LastName
        Parameter:
            None
        Return:
            firstName (str)
        '''
        return self.lastName
    
    def setFirstName(self, newFirstName):
        '''
        Description:
            sets FirstName when updating the contacts
        Parameter:
            newFirstName (str) : input from user
        Return:
            None
        '''
        self.firstName = newFirstName

    def setLastName(self, newLastName):
        '''
        Description:
            sets LastName when updating the contacts
        Parameter:
            newLastName (str) : input from user
        Return:
            None
        '''
        self.lastName = newLastName

    def setPhone(self, newPhone):
        '''
        Description:
            sets phone when updating the contacts
        Parameter:
            newPhone (str) : input from user
        Return:
            None
        '''
        self.phone = newPhone

    def setEmail(self, newEmail):
        '''
        Description:
            sets Email when updating the contacts
        Parameter:
            newEmail (str) : input from user
        Return:
            None
        '''
        self.email = newEmail

class AddressBook:
    entries = {}

    def add_entries(self, contact):
        '''
        Description:
            Adds entry in address Book
        Parameter:
            contact (Contact) : Contact class
        Return:
            returns the flow of the program
        '''
        name = contact.getFirstName()
        if name in self.entries:
            return "\nContact already present.\n"
        else:
            self.entries[name] = contact
            return "\nContact added successfully.\n"

    def search_entry(self, name):
        '''
        Description:
            Search entry in address Book by firstName
        Parameter:
            name(str) : input from user
        Return:
            returns the flow of the program
        '''
        if name in self.entries:    
            print(self.entries[name])
            return '\nContact Found.\n'
        else:
            return '\nName not found.\n'

    def display_entries(self):
        '''
        Description:
            Displays the entries in address Book
        Parameter:
            None
        Return:
            None
        '''
        for i in self.entries:
            print(self.entries[i])

    def remove_entry(self, name):
        '''
        Description:
            Removes the entry by matching firstName
        Parameter:
            name(str) : input from user
        Return:
            returns the flow of the program
        '''
        if name in self.entries:
            del self.entries[name]
            return '\nContact removed successfully.\n'
        else:
            return '\nName not found.\n'

    def update_entry(self, name, param, value):
        '''
        Description:
            Updates the entry by matching firstName, the user needs to enter which field 
            to be undated and its value
        Parameter:
            name(str) : input from user
            param(int) : input from user
            value(str) : input from user
        Return:
            returns the flow of the program
        '''
        if name in self.entries:
            k = self.entries[name]
            funcs = [k.setFirstName, k.setLastName, k.setPhone, k.setEmail]
            funcs[param-1](value)
            return '\nContact updated successfully.\n'
        else:
            return '\nName not found.\n'

    def get_entries(self):
        '''
        Description:
            Returns the entries
        Parameter:
            None
        Return:
            entries (dict)
        '''
        return self.entries

def name_regex(x):
    '''
    Description:
        Get input from user, check whether the input is matching with the pattern
        expression, if True then return
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

def book():
    '''
    Description:
        AddressBook Program, Start off by asking user to choose the features available in the addressbook
        and perform those function accordingly
    Parameter:
        None
    Return:
        None
    '''
    try:
        print("Welcome to Address Book Program")
        addressBook = AddressBook()

        user_input = ""

        while user_input != 'q':
            print("1 - Add a Contact")
            print("2 - Display Book")
            print("3 - Search Contact")
            print("4 - Remove Contact")
            print("5 - Update Contact")
            print("q - Quit")
            user_input = input("Select Option: ")

            if user_input == "1":
                firstName = name_regex("Enter First Name: ")
                lastName = name_regex("Enter Last Name: ")
                phone = phone_regex("Enter Phone Number: ")
                email = email_regex("Enter Email: ")
                addressBook.add_entries(Contact(firstName, lastName, phone, email))

            elif user_input == "2":
                addressBook.display_entries()

            elif user_input == "3":
                firstName = input("Enter First Name: ")
                addressBook.search_entry(firstName)

            elif user_input == "4":
                firstName = input("Enter First Name: ")
                addressBook.remove_entry(firstName)

            elif user_input == "5":
                firstName = input("Enter First Name: ")
                while True:
                    choice = int(input("Choose Field To Update: \n1. FirstName\n2. LastName\n3. Phone Number\n4.Email"))
                    if(choice == 1 | choice == 2):
                        value = name_regex("Update to: ")
                    elif (choice == 3):
                        value = phone_regex("Update to: ")
                    elif (choice == 4):
                        value = phone_regex("Update to: ")
                    else:
                        print("Please Choose properly")
                addressBook.update_entry(firstName, choice, value)

            elif user_input == "q":
                break

            else:
                print("Please Select Proper Option")

    except:
        pass


book()
