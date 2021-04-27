'''
@Author: Sankar
@Date: 2021-04-26 10:46:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-27 10:46:09
@Title : Window Functions
'''
from SQL_Connect import CRUD
from log import logger

def window_function():
    try: 
        connect = CRUD()
        cursor = connect._CRUD__db.cursor()

        cursor.execute('SELECT stud_name,subject,marks, SUM(marks) OVER (partition by subject) Total_marks FROM student_info')

        result = cursor.fetchall()

        for i in result:
            logger.info(i)

    except:
        logger.exception("Function Aborted")

window_function()