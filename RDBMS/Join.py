from SQL_Connect import CRUD
from log import logger

def inner_join():
    try:
        connect = CRUD() 
        cursor = connect._CRUD__db.cursor()

        cursor.excecute("SELECT * FROM employee_details ed INNER JOIN payroll_details pd ON ed.id = pd.employee_id")
    
        result = cursor.fetchall()

        for i in result:
            logger.info(i)

    except:
        logger.error("INNER JOIN Aborted")

def outer_left_join():
    try:
        connect = CRUD() 
        cursor = connect._CRUD__db.cursor()

        cursor.excecute("SELECT * FROM employee_details ed LEFT OUTER JOIN payroll_details pd ON ed.id = pd.employee_id")
    
        result = cursor.fetchall()

        for i in result:
            logger.info(i)

    except:
        logger.error("LEFT OUTER JOIN Aborted")

def right_outer_join():
    try:
        connect = CRUD() 
        cursor = connect._CRUD__db.cursor()

        cursor.excecute("SELECT * FROM employee_details ed RIGHT OUTER JOIN payroll_details pd ON ed.id = pd.employee_id")
    
        result = cursor.fetchall()

        for i in result:
            logger.info(i)

    except:
        logger.error("RIGHT OUTER JOIN Aborted")

def cross_join():
    try:
        connect = CRUD() 
        cursor = connect._CRUD__db.cursor()

        cursor.excecute("SELECT * FROM employee_details ed CROSS JOIN payroll_details pd")
    
        result = cursor.fetchall()

        for i in result:
            logger.info(i)

    except:
        logger.error("CROSS JOIN Aborted")