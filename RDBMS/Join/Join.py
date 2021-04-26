'''
@Author: Sankar
@Date: 2021-04-24 08:46:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-26 09:38:09
@Title : JOIN
'''
from SQL_Connect import CRUD
from log import logger

def inner_join():
    '''
    Description:
        Inner Join
    Parameter:
        None
    Return:
        None
    '''
    try:
        connect = CRUD() 
        cursor = connect._CRUD__db.cursor()

        cursor.execute("SELECT * FROM employee_details ed INNER JOIN payroll_details pd ON ed.id = pd.employee_id")
    
        result = cursor.fetchall()

        for i in result:
            logger.info(i)

    except:
        logger.error("INNER JOIN Aborted")

def outer_left_join():
    '''
    Description:
       Outer Left Join
    Parameter:
        None
    Return:
        None
    '''
    try:
        connect = CRUD() 
        cursor = connect._CRUD__db.cursor()

        cursor.execute("SELECT * FROM employee_details ed LEFT OUTER JOIN payroll_details pd ON ed.id = pd.employee_id")
    
        result = cursor.fetchall()

        for i in result:
            logger.info(i)

    except:
        logger.error("LEFT OUTER JOIN Aborted")

def right_outer_join():
    '''
    Description:
        Outer Right Join
    Parameter:
        None
    Return:
        None
    '''
    try:
        connect = CRUD() 
        cursor = connect._CRUD__db.cursor()

        cursor.execute("SELECT * FROM employee_details ed RIGHT OUTER JOIN payroll_details pd ON ed.id = pd.employee_id")
    
        result = cursor.fetchall()

        for i in result:
            logger.info(i)

    except:
        logger.error("RIGHT OUTER JOIN Aborted")

def cross_join():
    '''
    Description:
        Cross Join
    Parameter:
        None
    Return:
        None
    '''
    try:
        connect = CRUD() 
        cursor = connect._CRUD__db.cursor()

        cursor.execute("SELECT * FROM employee_details ed CROSS JOIN payroll_details pd")
    
        result = cursor.fetchall()

        for i in result:
            logger.info(i)

    except:
        logger.error("CROSS JOIN Aborted")

def self_join():
    '''
    Description:
        Cross Join
    Parameter:
        None
    Return:
        None
    '''
    try:
        connect = CRUD() 
        cursor = connect._CRUD__db.cursor()

        cursor.execute("SELECT * FROM employee_details ed1, employee_details ed2 WHERE ed1.salary = ed2.salary AND ed2.salary <30000")
    
        result = cursor.fetchall()

        for i in result:
            logger.info(i)

    except:
        logger.error("SELF JOIN Aborted")