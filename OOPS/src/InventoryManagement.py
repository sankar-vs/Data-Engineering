'''
@Author: Sankar
@Date: 2021-04-06 21:10:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-06 21:15:09
@Title : Inventory Management
'''
import json
import os, re
import logging

class Management:
    '''
    Class:
        Management

    Description:
        Class to read inventory from JSON, calculate the total price, print out to JSON file
        add a new record to the file

    Functions:
        read_json_to_print()
        calculate_total_price()
        add_pulses(name, weight, price)
        write_to_json()

    Variable:
        entries (dict)
    '''
    entries = {}
    def __init__(self):
        if os.path.isfile("../src/resources/inventory.json"):
            with open("../src/resources/inventory.json", "r") as f:
                self.entries = json.load(f)
                print(self.entries)
                
    def read_json_to_print(self):
        '''
        Description:
            Prints the details from JSON file to console
        Parameter:
            None
        Return:
            None
        '''
        self.calculate_total_price()
        for i in self.entries:
            list = self.entries[i]
            for j in range(len(list)):
                dict = list[j]
                print("------------------------------------------")
                print("name: {}".format(dict['name']))
                print("weight: {}".format(dict['weight']))
                print("pricePerKG: {}".format(dict['pricePerKg']))
                print("totalPrice: {}".format(dict['total']))
                print("------------------------------------------")

    def calculate_total_price(self):
        '''
        Description:
            Calculates the total price for the pulse
        Parameter:
            None
        Return:
            None
        '''
        for i in self.entries:
            list = self.entries[i]
            for j in range(len(list)):
                dict = list[j]
                self.total = dict['weight'] * dict['pricePerKg']
                dict['total'] = self.total

    def add_pulses(self, name, weight, price):
        '''
        Description:
            Adds a new record of pulse
        Parameter:
            name (str): Name of the pulse
            weight (int): weight of the pulse
            price (int): Price Per Kg of the pulse
        Return:
            None
        '''
        for i in self.entries:
            list = self.entries[i]
            dict = {}
            dict['name'] = name
            dict['weight'] = weight
            dict['pricePerKg'] = price
            list.append(dict)
        self.calculate_total_price()
    
    def write_to_json(self):
        with open("../src/resources/inventory_updated.json", "w") as f:
                json.dump(self.entries, f, indent=4)

    def get_entries(self):
        '''
        Description:
            return entries
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

def num_regex(x):
    '''
    Description:
        Get input from user, check whether the input is matching with the pattern
        expression, if True then return
    Parameter:
        x (str): Statement to be asked
    Return:
        num (int): input from user
    '''
    while True:
        try:
            num = input(x)
            pattern = "^([1-9][0-9]{,8})$"
            result = re.match(pattern, num)
            if (result):
                return int(num)
        except:
            pass
        logging.warning("Enter positive Integer")


def inventory():
    '''
    Description:
        Gives choice to user to perform features available from Management class
    Parameter:
        None
    Return:
        None
    '''
    try:
        management = Management()

        user_input = ""

        while user_input != 'q':
            print("1 - Read from JSON")
            print("2 - Add Record")
            print("3 - Write to JSONt")
            print("q - Quit")
            user_input = input("Select Option: ")

            if(user_input == "1"):
                management.read_json_to_print()

            elif(user_input == "2"):
                name = name_regex("Enter pulse Name: ")
                weight = num_regex("Enter weight: ")
                price = num_regex("Enter pricePerKg: ")
                management.add_pulses(name, weight, price)

            elif(user_input == "3"):
                management.write_to_json()

            else:
                print("Please select proper choice")

    except:
        pass

inventory()