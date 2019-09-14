import sqlite3

class Student:
    def __init__(self,Name,Id=None,Age=None,Major=None):
        self.Name =Name
        self.Id = Id
        self.Age=Age
        self.Major=Major

    def __str__(self):
        return f"{{Name:{self.Name},Id:{self.Id},Age:{self.Age},Major:{self.Major}}}"




# class Data:

#         def __init__(self,Name,Id=None,Age=None,Major=None):
#                 self.DName =Name
#                 self.DId = Id
#                 self.DAge=Age
#                 self.DMajor=Major

ExmapleDb=True
StudentDb=True

if StudentDb:
        conn=sqlite3.connect('Example.db') 
elif ExmapleDb:
        conn=sqlite3.connect('Student.db')


# conn=sqlite3.connect('Example.db')
c=conn.cursor()

#CREATE TABLE
def Create_table():
        with conn:
                c.execute("""CREATE TABLE Students_Data(
                        Name text,
                        ID blob,
                        Age integer,
                        Major text
                                )""")


#  INSERT data normally
# c.execute("INSERT INTO Students_Data VALUES ('Yudathadei','Y0973ETM',22,'CS')")
#  INSERT data using dictionary format
def Insert_data_dictionary(studentObject):
        with conn:
                c.execute("INSERT INTO Students_Data VALUES (:Name,:ID,:Age,:Major)",{'Name':studentObject.Name,'ID':studentObject.Id,'Age':studentObject.Age,'Major':studentObject.Major})

#  INSERT data using tuple format
def Insert_data_tuple(studentObject):
        with conn:
                c.execute("INSERT INTO Students_Data VALUES(?,?,?,?)",(studentObject.Name,studentObject.Id,studentObject.Age,studentObject.Major))
#  DELETE data
def Delete_data_Name(StudentName):
        with conn:
                c.execute("DELETE FROM Students_Data WHERE  Name=(?)",(StudentName,))
#  UPDATE data
def Update_data(studentObject,OldName):
        with conn:
                 c.execute("UPDATE Students_Data SET Name=(?),Id=(?),Age=(?),Major=(?) WHERE  Name=(?)",(studentObject.Name,studentObject.Id,studentObject.Age,studentObject.Major,OldName))

                                                
#  SELECT only one item
def Select_oneData(StudentName ,Particular):
        with conn:
                c.execute("SELECT (?) FROM Students_Data WHERE Name=(?)",(Particular,StudentName))
                return c.fetchall()

container=[]
#select all data
def Select_allData(StudentName):
        with conn:
                c.execute("SELECT * FROM Students_Data WHERE Name=(?)",(StudentName,))
                for item in  c.fetchall() :
                        for detail in item:
                                container.append(detail)
#Read all table content

def Read_all_contents():
        with conn:
                c.execute("SELECT * FROM Students_Data ")
                c.fetchall

                                
                

