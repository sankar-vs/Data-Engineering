'''
@Author: Sankar
@Date: 2021-04-24 08:46:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-24 09:38:09
@Title : Indexing
'''
from SQL_Connect import CRUD
from log import logger

def create_indexing():
    '''
    Description:
        To Create a Index in MySQL
    Parameter:
        None
    Return:
        None
    '''
    try:
        connect = CRUD() 
        cursor = connect._CRUD__db.cursor()
        indexName = input("Enter index name: ")

        cursor.execute("CREATE INDEX {} ON employee_details(name, salary)".format(indexName))

        connect._CRUD__db.commit()

        logger.info("Index Created: {}".format(indexName))
    except:
        logger.error("Creating Index Aborted")

def drop_indexing():
    '''
    Description:
        To Drop a Index in MySQL
    Parameter:
        None
    Return:
        None
    '''
    try:
        connect = CRUD() 
        cursor = connect._CRUD__db.cursor()
        indexName = input("Enter index name: ")

        cursor.execute("DROP INDEX {} ON employee_details".format(indexName))

        connect._CRUD__db.commit()

        logger.info("Index Dropped: {}".format(indexName))
    except:
        logger.error("Dropping Index Aborted")

def search_by_name():
    '''
    Description:
        To Search by name in MySQL
    Parameter:
        None
    Return:
        None
    '''
    try:
        connect = CRUD() 
        cursor = connect._CRUD__db.cursor()

        name = input("Enter name: ")

        cursor.execute("SELECT * FROM employee_details WHERE name = '{}'".format(name))

        result = cursor.fetchall()

        for i in result:
            logger.info(i)
    except:
        logger.error("Retrieve by data Aborted")
