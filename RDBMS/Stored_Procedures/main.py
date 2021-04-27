'''
@Author: Sankar
@Date: 2021-04-26 08:46:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-26 10:50:09
@Title : Main for Stored Procedures in MySQL
'''
from Stored_procedures import StoredProcedures
from log import logger

def features():
    '''
    Description:
        Performs features on call of Stored Procedures in MySQL
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
            print("1 - Stored Procedure without arguments")
            print("2 - Stored Procedure with argument IN")
            print("3 - Stored Procedure with argument OUT")
            print("4 - Stored Procedure with argument INOUT")
            print("5 - Stored Procedure with more than 1 argument")
            print("6 - Show Stored Procedure")
            print("q - Quit")
            user_input = input("Select Option: ")

            sp = StoredProcedures()

            if (user_input == "1"):
                logger.info("Choosen without arguments")
                sp.call_get_merit_student()

            elif (user_input == "2"):
                logger.info("Choosen with argument IN")
                sp.call_get_student_by_limit()
            
            elif (user_input == "3"):
                logger.info("Choosen with argument OUT")
                sp.call_max_display_marks()

            elif (user_input == "4"):
                logger.info("Choosen with argument INOUT")
                sp.call_display_marks()

            elif (user_input == "5"):
                logger.info("Choosen with more than 1 argument")
                sp.call_display_students_by_limit()

            elif (user_input == "6"):
                logger.info("Choosen Show Stored Procedure")
                sp.show_stored_procedures()

            elif user_input == "q":
                logger.info("Choosen to quit")
                break

            else:
                print("Please Select Proper Option")

    except:
        raise Exception("Program Stopped")

features()