'''
@Author: Sankar
@Date: 2021-04-26 06:46:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-26 09:38:09
@Title : Functions
'''
from SQL_Connect import CRUD
from log import logger

class AggregateFunctions():
    '''
    Class:
        AggregateFunctions
    Description:
        To perform Math Functions in MySQL
    Functions:
        count()
        sum()
        min()
        max()
        average()
    Variable:
        None
    '''
    def __init__(self):
        self.connect = CRUD()

    def count(self):
        try: 
            cursor = self.connect._CRUD__db.cursor()

            cursor.execute('SELECT subject,COUNT(*) AS Subject_Count FROM student_info group by subject order by Subject_count')

            result = cursor.fetchall()

            logger.info(result)

        except:
            logger.exception("Count Aborted")

    def sum(self):
        try: 
            cursor = self.connect._CRUD__db.cursor()

            cursor.execute('SELECT subject,SUM(marks) AS Total_marks FROM student_info group by subject order by Total_marks DESC')

            result = cursor.fetchall()

            logger.info(result)

        except:
            logger.exception("Sum Aborted")

    def min(self):
        try: 
            cursor = self.connect._CRUD__db.cursor()

            cursor.execute('SELECT subject,MIN(marks) AS min_marks FROM student_info group by subject order by min_marks')

            result = cursor.fetchall()

            logger.info(result)

        except:
            logger.exception("MIN Aborted")

    def max(self):
        try: 
            cursor = self.connect._CRUD__db.cursor()

            cursor.execute('SELECT subject,MAX(marks) AS max_marks FROM student_info group by subject order by max_marks;')

            result = cursor.fetchall()

            logger.info(result)

        except:
            logger.exception("MAX Aborted")

    def average(self):
        try: 
            cursor = self.connect._CRUD__db.cursor()

            cursor.execute('SELECT subject,AVG(marks) AS avg_marks FROM student_info group by subject order by avg_marks;')

            result = cursor.fetchall()

            logger.info(result)

        except:
            logger.exception("Average Aborted")

class DateFunctions():
    '''
    Class:
        DateFunctions
    Description:
        To perform DateTime Functions in MySQL
    Functions:
        timeStamp()
        dateAdd()
        dateSub()
        date_format()
        get_date()
        time_stamp_diff()
    Variable:
        None
    '''

    def __init__(self):
        self.connect = CRUD()

    def timeStamp(self):
        try: 
            cursor = self.connect._CRUD__db.cursor()

            cursor.execute('SELECT CURRENT_TIMESTAMP')

            result = cursor.fetchall()

            logger.info(result)

        except:
            logger.exception("TimeStamp Aborted")

    def dateAdd(self):
        try: 
            cursor = self.connect._CRUD__db.cursor()

            cursor.execute("SELECT DATE_ADD('2018-05-01',INTERVAL 1 DAY)")

            result = cursor.fetchall()

            logger.info(result)

        except:
            logger.exception("DateADD Aborted")

    def dateSub(self):
        try: 
            cursor = self.connect._CRUD__db.cursor()

            cursor.execute("SELECT DATE_SUB('2018-05-01',INTERVAL 1 YEAR)")

            result = cursor.fetchall()

            logger.info(result)

        except:
            logger.exception("DateSUB Aborted")

    def date_format(self):
        try: 
            cursor = self.connect._CRUD__db.cursor()

            statements = ["SELECT DATE_FORMAT('2009-10-04 22:23:00', '%W %M %Y')", 
                          "SELECT DATE_FORMAT('2007-10-04 22:23:00', '%H:%i:%s')",
                          "SELECT DATE_FORMAT('1900-10-04 22:23:00','%D %y %a %d %m %b %j')"]
            
            for i in statements:
                cursor.execute(i)
                result = cursor.fetchall()
                logger.info(result)

        except:
            logger.exception("Date_Format Aborted")

    def get_date(self):
        try: 
            cursor = self.connect._CRUD__db.cursor()

            statements = ["SELECT DAYNAME('2007-02-03')", 
                          "SELECT DAYOFMONTH('2007-02-03')",
                          "SELECT DAYOFWEEK('2007-02-03')", 
                          "SELECT DAYOFYEAR('2007-02-03')",
                          "SELECT EXTRACT(YEAR FROM '2019-07-02')",
                          "SELECT STR_TO_DATE('01,5,2013','%d,%m,%Y')",
                          "SELECT STR_TO_DATE('10.31.2003',GET_FORMAT(DATE,'USA'))"]
            
            for i in statements:
                cursor.execute(i)
                result = cursor.fetchall()
                logger.info(result)

        except:
            logger.exception("Get_date Aborted")

    def time_stamp_diff(self):
        try: 
            cursor = self.connect._CRUD__db.cursor()

            statements = ["SELECT TIMESTAMPDIFF(MONTH,'2003-02-01','2003-05-01')",
                          "SELECT TIMESTAMPDIFF(YEAR,'2002-05-01','2001-01-01')",
                          "SELECT TIMESTAMPDIFF(MINUTE,'2003-02-01','2003-05-01 12:05:55')"]
            
            for i in statements:
                cursor.execute(i)
                result = cursor.fetchall()
                logger.info(result)

        except:
            logger.exception("TimeStamp Diff Aborted")

class StringFunctions():
    '''
    Class:
        StringFunctions
    Description:
        To perform String Functions in MySQL
    Functions:
        concat()
        field()
        insert()
        string_seperation()
        trim()
    Variable:
        None
    '''
    def __init__(self):
        self.connect = CRUD()

    def concat(self):
        try: 
            cursor = self.connect._CRUD__db.cursor()

            statements = ["SELECT CONCAT(stud_name,subject) FROM student_info",
                          "SELECT CONCAT_WS(',',stud_name,subject) FROM student_info"]
            
            for i in statements:
                cursor.execute(i)
                result = cursor.fetchall()
                logger.info(result)

        except:
            logger.exception("Concat Aborted")

    def field(self):
        try: 
            cursor = self.connect._CRUD__db.cursor()

            statements = ["SELECT ELT(4, 'Aa', 'Bb', 'Cc', 'Dd')",
                          "SELECT FIELD('Bb', 'Aa', 'Bb', 'Cc', 'Dd', 'Ff')",
                          "SELECT FIND_IN_SET('b','a,b,c,d')"]
            
            for i in statements:
                cursor.execute(i)
                result = cursor.fetchall()
                logger.info(result)

        except:
            logger.exception("Field Aborted")

    def insert(self):
        try: 
            cursor = self.connect._CRUD__db.cursor()

            statements = ["SELECT INSERT('Quadratic', 3, 4, 'What')",
                          "SELECT LOCATE('bar', 'foobarbar')",
                          "SELECT LOCATE('bar', 'foobarbar', 5)"]
            
            for i in statements:
                cursor.execute(i)
                result = cursor.fetchall()
                logger.info(result)

        except:
            logger.exception("Insert Aborted")

    def string_seperation(self):
        try: 
            cursor = self.connect._CRUD__db.cursor()

            statements = ["SELECT LOWER('QUADRATICALLY')",
                          "SELECT LEFT('foobarbar', 5)",
                          "SELECT LENGTH('text')",
                          "SELECT LPAD('hi',4,'??')",
                          "SELECT REPEAT('MySQL', 3)",
                          "SELECT REPLACE('www.mysql.com', 'w', 'Ww')", 
                          "SELECT REVERSE('abc')",
                          "SELECT RIGHT('foobarbar', 4)", 
                          "SELECT RPAD('hi',5,'?')",
                          "SELECT SUBSTRING('Quadratically',5,6)",
                          "SELECT SUBSTRING_INDEX('www.mysql.com', '.', 2)"]
            
            for i in statements:
                cursor.execute(i)
                result = cursor.fetchall()
                logger.info(result)

        except:
            logger.exception("String Seperation Aborted")

    def trim(self):
        try: 
            cursor = self.connect._CRUD__db.cursor()

            statements = ["SELECT LTRIM('  barbar')", 
                          "SELECT RTRIM('barbar   ')", 
                          "SELECT TRIM('  bar   ')", 
                          "SELECT TRIM(LEADING 'x' FROM 'xxxbarxxx')",
                          "SELECT TRIM(BOTH 'x' FROM 'xxxbarxxx')",
                          "SELECT TRIM(TRAILING 'xyz' FROM 'barxxyz')"]
            
            for i in statements:
                cursor.execute(i)
                result = cursor.fetchall()
                logger.info(result)

        except:
            logger.exception("TRIM Aborted")