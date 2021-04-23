'''
@Author: Sankar
@Date: 2021-04-23 06:46:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-23 10:38:09
@Title : Feature Main to perform CRUD Operation
'''
from SQL_Connect import CRUD
from log import logger

def features():
    '''
    Description:
        Performs CRUD Operation on MySql
    Parameter:
        None
    Return:
        None
    '''
    try:
        logger.info("Program start")
        user_input = ""

        while user_input != 'q':
            print("Default table selected employee_table")
            print("1 - Create Table")
            print("2 - Drop Table")
            print("3 - Alter Table to add more fields")
            print("4 - Insert record to employee_table")
            print("5 - Retrieve records from employee_table")
            print("6 - Update record from employee_table")
            print("7 - Delete record from employee_table")
            print("q - Quit")
            user_input = input("Select Option: ")

            connect = CRUD()

            if (user_input == "1"):
                logger.info("Choosen to create a new table")
                connect.create_table()

            elif (user_input == "2"):
                logger.info("Choosen to drop table")
                connect.drop_table()

            elif (user_input == "3"):
                logger.info("Choosen to alter table")
                connect.alter_table()

            elif (user_input == "4"):
                logger.info("Choosen to insert record")
                connect.insert()

            elif (user_input == "5"):
                logger.info("Choosen to retrieve records")
                connect.retrieve()

            elif (user_input == "6"):
                logger.info("Choosen to update record")
                connect.update()

            elif (user_input == "7"):
                logger.info("Choosen to delete record")
                connect.delete()

            elif user_input == "q":
                logger.info("Choosen to quit")
                break

            else:
                print("Please Select Proper Option")

    except:
        raise Exception("Program Stopped")

features()