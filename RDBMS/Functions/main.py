'''
@Author: Sankar
@Date: 2021-04-26 08:46:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-26 11:38:09
@Title : Main for Functions in MySQL
'''
from Functions import AggregateFunctions
from Functions import DateFunctions
from Functions import StringFunctions
from log import logger

def features():
    '''
    Description:
        Performs features on types of Functions in MySQL
    Parameter:
        None
    Return:
        None
    '''
    try:
        agg = AggregateFunctions()
        dt = DateFunctions()
        sr = StringFunctions()

        logger.info("Program start")
        user_input = ""

        while user_input != 'q':
            print("1 - Aggregate Count Function")
            print("2 - Aggregate Sum Function")
            print("3 - Aggregate Min Function")
            print("4 - Aggregate Max Function")
            print("5 - Aggregate Average Function")
            print("6 - DateTime timeStamp Function")
            print("7 - DateTime dateAdd Function")
            print("8 - DateTime dateSub Function")
            print("9 - DateTime date_format Function")
            print("10 - DateTime date Function")
            print("11 - DateTime date_diff Function")
            print("12 - String concat Function")
            print("13 - String field Function")
            print("14 - String insert Function")
            print("15 - String string_seperator Function")
            print("16 - String trim Function")
            print("q - Quit")
            user_input = input("Select Option: ")

            if (user_input == "1"):
                logger.info("Choosen count function")
                agg.count()

            elif (user_input == "2"):
                logger.info("Choosen sum function")
                agg.sum()
            
            elif (user_input == "3"):
                logger.info("Choosen min function")
                agg.min()

            elif (user_input == "4"):
                logger.info("Choosen max function")
                agg.max()

            elif (user_input == "5"):
                logger.info("Choosen average function")
                agg.average()

            elif (user_input == "6"):
                logger.info("Choosen timeStamp Function")
                dt.timeStamp()

            elif (user_input == "7"):
                logger.info("Choosen dateAdd Function")
                dt.dateAdd()

            elif (user_input == "8"):
                logger.info("Choosen dateSub Function")
                dt.dateSub()

            elif (user_input == "9"):
                logger.info("Choosen date_formatFunction")
                dt.date_format()
            
            elif (user_input == "10"):
                logger.info("Choosen dateFunction")
                dt.get_date()

            elif (user_input == "11"):
                logger.info("Choosen date_diff Function")
                dt.time_stamp_diff()

            elif (user_input == "12"):
                logger.info("Choosen concat Function")
                sr.concat()

            elif (user_input == "13"):
                logger.info("Choosen field Function")
                sr.field()

            elif (user_input == "14"):
                logger.info("Choosen insert Function")
                sr.insert()

            elif (user_input == "15"):
                logger.info("Choosen string_seperation Functions")
                sr.string_seperation()

            elif (user_input == "16"):
                logger.info("Choosen Trim Functions")
                sr.trim()

            elif user_input == "q":
                logger.info("Choosen to quit")
                break

            else:
                print("Please Select Proper Option")

    except:
        raise Exception("Program Stopped")

features()