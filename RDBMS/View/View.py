'''
@Author: Sankar
@Date: 2021-04-24 06:46:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-26 11:05:09
@Title : View in MySQL
'''
from SQL_Connect import CRUD
from log import logger

def create_view():
    '''
    Description:
        Create a view in MySQL
    Parameter:
        None
    Return:
        None
    '''
    try:
        connect = CRUD() 
        cursor = connect._CRUD__db.cursor()
        viewName = input("Enter view name: ")

        cursor.execute("CREATE VIEW {} AS SELECT * FROM employee_details".format(viewName))
    
        connect._CRUD__db.commit()

        logger.info("View Created: {}".format(viewName))
    except:
        logger.error("Creating View Aborted")

def show_view():
    '''
    Description:
        Show View
    Parameter:
        None
    Return:
        None
    '''
    try:
        connect = CRUD() 
        cursor = connect._CRUD__db.cursor()
        viewName = input("Enter view name: ")

        cursor.execute("SELECT * FROM {}".format(viewName))
    
        result = cursor.fetchall()

        for i in result:
            logger.info(i)
    except:
        logger.error("Show View Aborted")

def drop_view():
    '''
    Description:
        Drop View
    Parameter:
        None
    Return:
        None
    '''
    try:
        connect = CRUD() 
        cursor = connect._CRUD__db.cursor()
        viewName = input("Enter view name: ")

        cursor.execute("DROP VIEW {}".format(viewName))
    
        connect._CRUD__db.commit()

        logger.info("View Dropped: {}".format(viewName))
    except:
        logger.error("Dropping View Aborted")

def alter_view():
    '''
    Description:
        Alter View
    Parameter:
        None
    Return:
        None
    '''
    try:
        connect = CRUD() 
        cursor = connect._CRUD__db.cursor()
        viewName = input("Enter view name: ")

        cursor.execute("CREATE OR REPLACE VIEW {} AS SELECT name, salary FROM employee_details".format(viewName))
    
        connect._CRUD__db.commit()

        logger.info("View Altered: {}".format(viewName))
    except:
        logger.error("Altering View Aborted")