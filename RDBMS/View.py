from SQL_Connect import CRUD
from log import logger

def create_view():
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
    try:
        connect = CRUD() 
        cursor = connect._CRUD__db.cursor()
        viewName = input("Enter view name: ")

        cursor.execute("CREATE OR REPLACE VIEW {} AS SELECT name, salary FROM employee_details".format(viewName))
    
        connect._CRUD__db.commit()

        logger.info("View Altered: {}".format(viewName))
    except:
        logger.error("Altering View Aborted")