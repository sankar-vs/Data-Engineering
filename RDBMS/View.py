from SQL_Connect import CRUD
from log import logger

def create_view():
    try:
        connect = CRUD() 
        print("done1")
        cursor = connect._CRUD__db.cursor()
        print("Done2")
        indexName = input("Enter index name: ")

        cursor.excecute("CREATE INDEX {} ON employee_details(name, salary)".format(indexName))
        print("Done3")
        connect._CRUD__db.commit()

        logger.info("Index Created: {}".format(indexName))
    except:
        logger.error("Creating View Aborted")