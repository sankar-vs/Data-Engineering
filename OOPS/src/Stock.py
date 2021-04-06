'''
@Author: Sankar
@Date: 2021-04-06 09:46:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-06 10:45:09
@Title : Stock Account Management
'''
import re
import os
import logging
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s')
class Stocks:
    '''
    Class:
        Stocks

    Description:
        Class to store the stocks name, number of stocks and price

    Functions:
        totalShare()
        get_total() -> str
        def getName() -> str

    Variable:
        None
    '''
    def __init__(self, name, numOfShare, price):
        self.name = name
        self.numOfShare = numOfShare
        self.price = price
        self.totalShare()

    def totalShare(self):
        self.total = self.numOfShare * self.price

    def get_total(self):
        return self.total

    def getName(self):
        return self.name

class Portfolio:
    '''
    Class:
        Portfolio

    Description:
        Portfolio maintains a report on the number of stocks

    Functions:
        add_stock(stock)
        read_file()
        print_file()
        printReport()
        get_entries() -> dict

    Variable:
        entries (dict)
    '''
    entries = {}

    def add_stock(self, stock):
        name = stock.getName()
        if name in self.entries:
            return "\nStock already present.\n"
        else:
            self.entries[name] = stock
            return "\nStock added successfully.\n"

    def read_file(self):
        if os.path.isfile("stock.csv"):
            with open("stock.csv") as f:
                csv_list = f.readlines()
                for line in csv_list:
                    data =  line.rstrip().split(",")
                    stock = Stocks(data[0],int(data[1]), int(data[2]))
                    self.entries[data[0]] = stock

    def print_file(self):
        with open("stock.csv", "w") as f:
            for i in self.entries:
                f.write(f"{self.entries[i].name},{self.entries[i].numOfShare},{self.entries[i].price},{self.entries[i].total}\n")

    def printReport(self):
        print("------------------------------")
        for i in self.entries:
            print("Stock Name: {}".format(self.entries[i].name))
            print("Number of Shares: {}".format(self.entries[i].numOfShare))
            print("Price: {}".format(self.entries[i].price))
            print("Total Value of Stocks: {}".format(self.entries[i].total))
        print("------------------------------")

    def get_entries(self):
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
            pattern = "^[A-Z]{4,}$"
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

def stockPortfolio():
    '''
    Description:
        Stock Portfolio Program, Start off by asking user to choose the features available in the Portfolio
        and perform those function accordingly
    Parameter:
        None
    Return:
        None
    '''
    try:
        print("Stock Account Management")
        port = Portfolio()

        user_input = ""

        while user_input != 'q':
            print("1 - Add Stock")
            print("2 - Print to File")
            print("3 - Read from File")
            print("4 - Print Report")
            print("q - Quit")
            user_input = input("Select Option: ")

            if user_input == "1":
                stockName = name_regex("Enter First Name: ")
                stockNumOfShare = num_regex("Enter Num of Shares: ")
                stockPrice = num_regex("Enter amount: ")
                port.add_stock(Stocks(stockName, stockNumOfShare, stockPrice))

            elif user_input == "2":
                port.print_file()

            elif user_input == "3":
                port.read_file()

            elif user_input == "4":
                port.printReport()

            elif user_input == "q":
                break
            
            else:
                print("Please choose properly")
    except:
        pass

stockPortfolio()