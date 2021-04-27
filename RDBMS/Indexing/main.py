'''
@Author: Sankar
@Date: 2021-04-26 08:46:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-26 09:38:09
@Title : Main for Indexing in MySQL
'''
import Indexing as index
from log import logger

def features():
    '''
    Description:
        Performs features on indexing in MySQl
    Parameter:
        None
    Return:
        None
    '''
    try:
        logger.info("Program start")
        user_input = ""

        while user_input != 'q':
            print("Default csv and table selected people_info")
            print("1 - Create Indexing")
            print("2 - Drop Indexing")
            print("3 - Search By Name")
            print("q - Quit")
            user_input = input("Select Option: ")

            if (user_input == "1"):
                logger.info("Choosen to create index")
                index.create_indexing()

            elif (user_input == "2"):
                logger.info("Choosen to drop index")
                index.drop_indexing()
            
            elif (user_input == "3"):
                logger.info("Choosen to Search By Name")
                index.search_by_name()

            elif user_input == "q":
                logger.info("Choosen to quit")
                break

            else:
                print("Please Select Proper Option")

    except:
        raise Exception("Program Stopped")

features()