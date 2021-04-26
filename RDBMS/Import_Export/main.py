'''
@Author: Sankar
@Date: 2021-04-26 08:46:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-26 09:38:09
@Title : Main for Import and Export a CSV File
'''
from ImportExport import ImportExport 
from log import logger

def features():
    '''
    Description:
        Performs Import and Export to CSV Operation in MySql
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
            print("1 - Import CSV")
            print("2 - Export CSV")
            print("q - Quit")
            user_input = input("Select Option: ")

            ie = ImportExport()

            if (user_input == "1"):
                logger.info("Choosen to import poeple.csv file")
                ie.import_csv()

            elif (user_input == "2"):
                logger.info("Choosen to export to output.csv file")
                ie.export_csv()

            elif user_input == "q":
                logger.info("Choosen to quit")
                break

            else:
                print("Please Select Proper Option")

    except:
        raise Exception("Program Stopped")

features()