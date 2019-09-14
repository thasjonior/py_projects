#this will file will be for general purpose only
import sqlite3
import os
from PyQt5.QtWidgets import QFileDialog

class db_class:

    def __init__(self,*values):
        for value in values:
            self.value=value

# this fetch what file to be used as specified by user
def get_dbFile(FileName=None):
        if not FileName:
                print("me in use")
                return sqlite3.connect('Example.db')

        else:
                print("huku niko " + FileName)
                return sqlite3.connect(FileName)
        
conn=get_dbFile()
c=conn.cursor()


# CREATE  TABLE 
# this receive table name and table colums from user and return new table to be used
def create_table(tablename,col1,*colms):
        statment="CREATE TABLE IF NOT EXISTS {}({} BLOB"
        arg_list=[tablename,col1] 
        for colm in colms:
                statment+=",{} BLOB"
                arg_list.append(colm)
        statment +=")"
        command=statment.format(*arg_list)
        with conn:
                c.execute(command)

# INSERT 
# this insert data to a table base on user option
def Insert_data_tuple(studentObject,*values):
        with conn:
            statment =("INSERT INTO{} VALUES{})"
            arg_list=[tablename]
            for value in values:
                arg_list.append(value)
            
            command=statment.format(*arg_list)
            c.execute(command)
             c.execute("INSERT INTO Students_Data VALUES(?,?,?,?)",(studentObject.Name,studentObject.Id,studentObject.Age,studentObject.Major))
SELECT by row
SELECT by table
DELETE one row
DELETE entire table

