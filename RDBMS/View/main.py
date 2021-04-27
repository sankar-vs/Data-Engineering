'''
@Author: Sankar
@Date: 2021-04-26 08:46:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-26 11:38:09
@Title : Main for Viewing in MySQL
'''
import View as v
from log import logger

def features():
    '''
    Description:
        Performs features on types of JOINS in MySQL
    Parameter:
        None
    Return:
        None
    '''
    try:
        logger.info("Program start")
        user_input = ""

        while user_input != 'q':
            print("Default csv and table selected employee_details")
            print("1 - Create View")
            print("2 - Show View")
            print("3 - Drop View")
            print("4 - Alter View")
            print("q - Quit")
            user_input = input("Select Option: ")

            if (user_input == "1"):
                logger.info("Choosen Create view")
                v.create_view()

            elif (user_input == "2"):
                logger.info("Choosen Show View")
                v.show_view()
            
            elif (user_input == "3"):
                logger.info("Choosen Drop View")
                v.drop_view()

            elif (user_input == "4"):
                logger.info("Choosen Alter View")
                v.alter_view()

            elif user_input == "q":
                logger.info("Choosen to quit")
                break

            else:
                print("Please Select Proper Option")

    except:
        raise Exception("Program Stopped")

features()