'''
@Author: Sankar
@Date: 2021-04-06 09:46:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-06 12:15:09
@Title : Commercial Data Processing
'''
import os, re
import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s')
class StockAccount:
    '''
    Class:
        StockAccount

    Description:
        Helps us in manage the stocks fro each account in a file

    Functions:
        buy(symbol, amount)
        sell(symbol, amount)
        save(file)
        valueOf()
        printReport()
        get_entries() -> dict

    Variable:
        entries (dict)
    '''
    entries = {}

    def __init__(self, file):
        with open(file + ".csv", "r") as f:
            csv_list = f.readlines()
            for line in csv_list:
                data =  line.rstrip().split(",")
                self.entries[data[0]] = [data[0], int(data[1])]

    def buy(self, symbol, amount):
        '''
        Description:
            Adds entry in stock account if it is not present, if the stock has already
            been bought add the amount.
        Parameter:
            symbol (str) : user input
            amount (int): user input
        Return:
            None
        '''
        if symbol in self.entries:
            data = self.entries[symbol]
            self.entries[symbol] = [data[0], (int(data[1]) + amount )]
        else:
            self.entries[symbol] = [symbol, amount]

    def sell(self, symbol, amount):
        '''
        Description:
            Adds entry in stock account if it is not present, if the stock has already
            been bought subtract the amount.
        Parameter:
            symbol (str) : user input
            amount (int): user input
        Return:
            None
        '''
        if symbol in self.entries:
            data = self.entries[symbol]
            self.entries[symbol] = [data[0], (int(data[1]) - amount )]
        else:
            self.entries[symbol] = [symbol, amount]

    def save(self, file):
        '''
        Description:
            Saves entry in stock account to a file
        Parameter:
            file (str) : user input
        Return:
            None
        '''
        with open(file + ".csv", "w") as f:
            for i in self.entries:
                data = self.entries[i]
                f.write(f"{data[0]},{data[1]}\n")

    def valueOf(self):
        '''
        Description:
            Calculates the total value of the account
        Parameter:
            None
        Return:
            total (int): summation of all the buy and sell amount
        '''
        total = 0
        for i in self.entries:
            data = self.entries[i]
            total += int(data[1])
        return total

    def printReport(self):
        '''
        Description:
            Prints the report to console
        Parameter:
            None
        Return:
            None
        '''
        print("-------------------------------------")
        for i in self.entries:
            data = self.entries[i]
            print("Symbol: {}".format(data[0]), end=", ")
            print("Amount: {}".format(data[1]), end=", ")
        print("TotalValue: {}".format(self.valueOf()))
        print("-------------------------------------")

    def get_entries(self):
        return self.entries

def symbol_regex(x):
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
            pattern = "^[A-Z]{4,}$"
            result = re.match(pattern, name)
            if (result):
                return str(name)
        except:
            pass
        logging.warning("Enter proper Name")

def amt_regex(x):
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
            num = input(x)
            pattern = "^([1-9][0-9]{,8})$"
            result = re.match(pattern, num)
            if (result):
                return int(num)
        except:
            pass
        logging.warning("Enter positive Integer")


def process():
    '''
    Description:
        Stock Account Program, Start off by asking user to choose the features available
        and perform those function accordingly
    Parameter:
        None
    Return:
        None
    '''
    try:
        print("Welcome to Commercial Data Processing")

        user_input = ""
        com = StockAccount("account")
        while user_input != 'q':
            print("1 - Buy")
            print("2 - Sell")
            print("3 - Save")
            print("4 - PrintReport")
            print("q - Quit")
            user_input = input("Select Option: ")

            if user_input == "1":
                symbol = symbol_regex("Enter Symbol: ")
                amt = amt_regex("enter amount: ")
                com.buy(symbol, amt)

            elif user_input == "2":
                symbol = symbol_regex("Enter Symbol: ")
                amt = amt_regex("enter amount: ")
                com.sell(symbol, amt)

            elif user_input == "3":
                com.save("account")
                
            elif user_input == "4":
                com.printReport()

            elif user_input == 'q':
                break

            else:
                print("Please choose properly")

    except:
        pass

process()