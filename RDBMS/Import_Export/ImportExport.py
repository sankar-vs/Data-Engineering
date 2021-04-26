'''
@Author: Sankar
@Date: 2021-04-26 06:46:25
@Last Modified by: Sankar
@Last Modified time: 2021-04-26 09:38:09
@Title : Import and Export a CSV File
'''
from SQL_Connect import CRUD
from log import logger
import pandas as pd
import csv

class ImportExport():
    '''
    Class:
        ImportExport
    Description:
        To import and export csv file.
    Functions:
        import_csv()
        export_csv()
    Variable:
        None
    '''
    def __init__(self):
        self.connect = CRUD()

    def import_csv(self):
        try:
            data = pd.read_csv('E:/Practice/Data_Engineering/RDBMS/Import_Export/people.csv')   
            df = pd.DataFrame(data, columns= ['Name','Country','Age'])
            logger.info("DataFrame: \n{}".format(df))

            cursor = self.connect._CRUD__db.cursor()

            # cursor.execute('CREATE TABLE people_info (Name nvarchar(50), Country nvarchar(50), Age int)')
            
            for row in df.itertuples():
                cursor.execute("INSERT INTO people_info (Name, Country, Age)VALUES ('{}','{}',{})".format(row.Name,row.Country,row.Age))
            
            self.connect._CRUD__db.commit()

        except:
            logger.exception("Import Aborted")

    def export_csv(self):
        try:            
            df = pd.read_sql('SELECT * FROM people_info', self.connect._CRUD__db)
            df.to_csv('E:/Practice/Data_Engineering/RDBMS/Import_Export/Output.csv', index=False)

        except:
            logger.exception("Export Aborted")