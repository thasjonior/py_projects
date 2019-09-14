
import employee
import sys
# from PyQt5 import QtGui,QtCore
from PyQt5.QtWidgets import QDialog,QLayout,QFormLayout,QWidget,QHBoxLayout,QLineEdit,QApplication,QVBoxLayout,QPushButton,QGroupBox,QGridLayout

class db_manager(QDialog):
        def __init__(self):
                super().__init__()
                self.initUI()
        def initUI(self):

                # self.get_data()
                # self.modify_data()
                self.Create_layout()
                self.setGeometry(500,500,500,300)
                self.setWindowTitle('Students_Data')
                self.show()

        def get_data(self):

                flo=QFormLayout(self)
                SName=QLineEdit(self)
                flo.addRow("Student_Name:",SName)
                SId=QLineEdit(self)
                flo.addRow("Student_Id:",SId)
                SAge=QLineEdit(self)
                flo.addRow("Student_Age:",SAge)
                SMajor=QLineEdit(self)
                flo.addRow("Student_Major:",SMajor)

        def modify_data(self):
                flo=QFormLayout(self)
                Mname=QLineEdit(self)
                flo.addRow("Enter name",Mname)

                Particular=QLineEdit(self)
                flo.addRow("Particular:",Particular)

                New=QLineEdit(self)
                flo.addRow("New",New)





        def Create_layout(self):

                self.groupbox=QGroupBox("Enter new student data")

                Glayout=QGridLayout(self)

                btn1=QPushButton("Submit",self)
                Glayout.addWidget(btn1, 0,1)

                btn2=QPushButton("Search",self)
                Glayout.addWidget(btn2,1,1)

                btn3=QPushButton("Update",self)
                Glayout.addWidget(btn3,2,1)

                btn4=QPushButton("Delete",self)
                Glayout.addWidget(btn4,3,0)

                btn5=QPushButton("Submit",self)
                Glayout.addWidget(btn5, 3,1)



                # Enter_btn=QPushButton("Submit",self)
                
                # Enter_btn.clicked.connect(self.Pr)

        # def Submit_btn(self):
        #         btn=QPushButton("Submit",self)
        # def Delete_btn(self):
        #         btn=QPushButton("Delete",self)
        # def Update_btn(self):
        #         btn=QPushButton("Update",self)
        # def Search_btn(self):
        #         btn=QPushButton("Search",self)
        # def SubmitUpdates_btn(self):
        #         btn=QPushButton("Submit",self)

if __name__=='__main__':
        app=QApplication(sys.argv)
        db=db_manager()
        sys.exit(app.exec_())


# # employee.db_file('Yuda.db') 
# emp=employee.Student('Agness','A908ETM',23,'Engineering')
# emp1=employee.Student('Gladness','G1232OsK',21,'Accountancy')
# SO=employee.Student('Iren','I6781EaJ',21,'Art')
# SO1=employee.Student('Evelyne','E0907KiY',21,'Medicine')

# # employee.Create_table()
# employee.Insert_data_tuple(SO)
# employee.Insert_data_dictionary(SO1)
# employee.Delete_data_Name('Evelyne')
# employee.Update_data('Timm','Irine','u88',12,'IS')
# # print(employee.Select_allData('Timm'))



