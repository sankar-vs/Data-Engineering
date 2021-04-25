from SQL_Connect import CRUD
from log import logger

def create_indexing():
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
    try:
        connect = CRUD() 
        cursor = connect._CRUD__db.cursor()

        name = input("Enter name: ")

        cursor.execute("SELECT * FROM employee_details WHERE name = {}".format(name))

        result = cursor.fetchall()

        for i in result:
            logger.info(i)
    except:
        logger.error("Retrieve by data Aborted")

create_indexing()
search_by_name()
drop_indexing()