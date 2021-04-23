'''
@Author: Sankar
@Date: 2021-04-21 06:46:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-21 09:38:09
@Title : CRUD Operation
'''
import mysql.connector
from decouple import config
from log import logger

class CRUD:
    '''
    Class:
        CRUD
    Description:
        To perform CRUD Operation
    Functions:
        createConnection()
        insert()
        retrieve()
        update()
        delete()
        alter_table()
        drop_table()
        create_table()
    Variable:
        None
    '''

    def __init__(self):
        self.__localhost = config('DB_HOST')
        self.__username = config('DB_USERNAME')
        self.__password = config('DB_PASSWORD')
        self.__database_name = config('DB_NAME')
        self.__table_name = config('DB_TABLENAME')
        self.createConnection()

    def createConnection(self):
        '''
        Description:
            To Create Connection to the SQL Server
        Parameter:
            None
        Return:
            None
        '''
        try:
            db = mysql.connector.connect(host = self.__localhost, user = self.__username,
                passwd = self.__password, database = self.__database_name)
            
            if (db):
                logger.info("Connection Successfull!")
            self.__db = db
        except:
            logger.error("Connection Unsuccessfull!")
            

    def insert(self):
        '''
        Description:
            To insert records
        Parameter:
            None
        Return:
            None
        '''
        try:
            name = input("Enter your name: ")
            salary = float(input("Enter Salary: "))

            logger.info("Entered: {}, {}".format(name, salary))
            
            cursor = self.__db.cursor()
            cursor.execute("INSERT INTO "+self.__table_name+" (name, salary) VALUES (%s,%s)", (name, salary))

            id = cursor.lastrowid
            deductions = salary * 0.2
            taxable_pay = salary - deductions
            tax = taxable_pay * 0.1
            netpay = salary - tax

            cursor.execute("INSERT INTO payroll_details (employee_id, basic_pay, deductions, taxable_pay, tax, netpay)" +
                " VALUE ({},{},{},{},{},{})".format(id, salary, deductions, taxable_pay, tax, netpay))

            self.__db.commit()
            logger.info("{} record inserted".format(cursor.rowcount))

        except:
            logger.error("Insert aborted")
            

    def retrieve(self):
        '''
        Description:
            To retrieve records
        Parameter:
            None
        Return:
            None
        '''
        try:
            cursor = self.__db.cursor()
            cursor.execute("SELECT * FROM "+self.__table_name)

            result = cursor.fetchall()

            for i in result:
                logger.info(i)
        except:
            logger.error("Retrieve aborted")

    def update(self):
        '''
        Description:
            To Update Records
        Parameter:
            None
        Return:
            None
        '''
        try:
            id = int(input("Update by id: "))
            name = input("Enter name: ")
            salary = float(input("Enter Salary: "))

            logger.info("Entered: {}, {}, {}".format(id, name, salary))
            cursor = self.__db.cursor()

            cursor.execute("UPDATE "+self.__table_name+" SET name=%s, salary=%s WHERE id = %s", (name, salary, id))

            self.__db.commit()

            logger.info("{} record updated".format(cursor.rowcount))
        except:
            logger.error("Update aborted")        

    def delete(self):
        '''
        Description:
            To Delete Records
        Parameter:
            None
        Return:
            None
        '''
        try:
            id = int(input("Delete by id: "))

            logger.info("Entered: {}".format(id))
            cursor = self.__db.cursor()

            cursor.execute("DELETE FROM {} WHERE id = {}".format(self.__table_name, id))

            self.__db.commit()

            logger.info(cursor.rowcount, "record deleted")
        except:
            logger.error("Delete aborted")

    def alter_table(self):
        '''
        Description:
            To Alter Table
        Parameter:
            None
        Return:
            None
        '''
        try:
            cursor = self.__db.cursor()

            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            for i in tables:
                print(i)

            table_name = input("Enter table name to insert fields: ")
            logger.info("Choose table {}".format(table_name))
            numberOfFields = int(input("Number of fields in table: "))

            field = {}
            for i in range(numberOfFields):
                field[(input("Enter field name: "))] = input("Choose from int, float and varchar: ")

            logger.info("Fields and its type if data {}".format(field))

            statements = []
            next = "id"
            for i in field:
                if (field[i] == "int"):
                    statements.append("ALTER TABLE "+table_name+" ADD "+i+" INT NOT NULL after "+next)
                    next = i
                elif (field[i] == "float"):
                    statements.append("ALTER TABLE "+table_name+" ADD "+i+" FLOAT NOT NULL after "+next)
                    next = i
                elif (field[i] == "varchar"):
                    statements.append("ALTER TABLE "+table_name+" ADD "+i+" VARCHAR(50) NOT NULL after "+next)
                    next = i
                else:
                    logger.info("Please enter the values properly! ")

            logger.info("Statement to be executed {}".format(statements))
            for i in statements:
                cursor.execute(i)
                self.__db.commit()

        except:
            logger.error("Create fields aborted")

    def drop_table(self):
        '''
        Description:
            To Drop a table
        Parameter:
            None
        Return:
            None
        '''
        try:
            cursor = self.__db.cursor()

            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            for i in tables:
                print(i)

            table_name = input("Enter table name to be deleted: ")

            logger.info("Table to be deleted: {}".format(table_name))

            cursor.execute("DROP TABLE "+table_name)

            self.__db.commit()
        except:
            logger.error("Drop table aborted")


    def create_table(self):
        '''
        Description:
            To Create a new table
        Parameter:
            None
        Return:
            None
        '''
        try:
            cursor = self.__db.cursor()

            cursor.execute("SHOW TABLES")
            tables = cursor.fetchall()
            for i in tables:
                print(i)

            table_name = input("Enter new table name: ")

            logger.info("Table to be created with id as a primary key: {}".format(table_name))

            cursor.execute("CREATE TABLE "+table_name+" (id INT unsigned NOT NULL AUTO_INCREMENT,PRIMARY  KEY (id))")

            self.__db.commit()
        except:
            logger.error("Create table aborted")