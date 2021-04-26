'''
@Author: Sankar
@Date: 2021-04-26 08:46:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-26 09:38:09
@Title : Main for Indexing in MySQL
'''
import Join as j
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
            print("Default csv and table selected people_info")
            print("1 - Inner Join")
            print("2 - Left Outer Join")
            print("3 - Right Outer Join")
            print("4 - Cross Join")
            print("5 - Self Join")
            print("q - Quit")
            user_input = input("Select Option: ")

            if (user_input == "1"):
                logger.info("Choosen Inner Join")
                j.inner_join()

            elif (user_input == "2"):
                logger.info("Choosen Left Outer Join")
                j.outer_left_join()
            
            elif (user_input == "3"):
                logger.info("Choosen Right Outer Join")
                j.right_outer_join()

            elif (user_input == "4"):
                logger.info("Choosen Cross Join")
                j.cross_join()

            elif (user_input == "5"):
                logger.info("Choosen Self Join")
                j.self_join()

            elif user_input == "q":
                logger.info("Choosen to quit")
                break

            else:
                print("Please Select Proper Option")

    except:
        raise Exception("Program Stopped")

features()