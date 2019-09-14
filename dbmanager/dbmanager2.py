
import dbsource
import sys
import time
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QDialog,QFormLayout,QTextEdit,QLabel,QMenu,QWidget,QHBoxLayout,QLineEdit,QApplication,QVBoxLayout,QPushButton,qApp,QGroupBox,QGridLayout

class db_source(QDialog):
        def __init__(self):

            super().__init__()
            self.initUI()
        def initUI(self):
            # self.Main_window() 
            self.get_data() 
            self.setGeometry(500,500,500,300)
            self.setWindowTitle('Students_Data')
            self.show()

        def get_data(self):
            self.validator1=False
            Glayout=QGridLayout(self)



            LMname=QLabel("Enter name:",self)
            Glayout.addWidget(LMname, 0,0)
            self.SSname=QLineEdit(self)
            Glayout.addWidget(self.SSname, 0,1)
            Searchbtn=QPushButton("Search",self)
            Searchbtn.clicked.connect(self.retrive_data)
            Glayout.addWidget(Searchbtn, 0,2)

            self.Notice=QLineEdit(self)
            Glayout.addWidget(self.Notice, 1,1)

            Lname=QLabel("Name:",self)
            Glayout.addWidget(Lname, 2,0)
            self.SName=QLineEdit(self)
            Glayout.addWidget(self.SName, 2,1)

            Lid=QLabel("ID:",self)
            Glayout.addWidget(Lid, 3,0)
            self.SId=QLineEdit(self)
            Glayout.addWidget(self.SId, 3,1)

            Lage=QLabel("Age",self)  
            Glayout.addWidget(Lage, 4,0)  
            self.SAge=QLineEdit(self)
            Glayout.addWidget(self.SAge ,4,1)

            Lmajor=QLabel("Major:", self)
            Glayout.addWidget(Lmajor, 5,0)
            self.SMajor=QLineEdit(self)
            Glayout.addWidget(self.SMajor, 5,1)

            self.Submitbtn=QPushButton("Submit",self)
            self.Submitbtn.clicked.connect(self.get_new_data)
            Glayout.addWidget(self.Submitbtn, 6,0)
            Deletebtn=QPushButton("Delete",self)
            Deletebtn.clicked.connect(self.delete_all_data)
            Glayout.addWidget(Deletebtn, 6,1)
            Updatebtn=QPushButton("Cancel",self)
            Glayout.addWidget(Updatebtn, 6,2)



        def Main_window(self):
            self.validator1=True

            grid=QGridLayout(self)

            srch_bar=QLineEdit(self)
            grid.addWidget(srch_bar, 0,0)
            srch_btn=QPushButton("Search",self)
            grid.addWidget(srch_btn, 0,1)

            self.results=QTextEdit()
            grid.addWidget(self.results, 1,0,1,2)

            view_btn=QPushButton("View Table",self)
            grid.addWidget(view_btn, 2,0)

            crt_btn=QPushButton("Create Table",self)
            crt_btn.clicked.connect(self.get_data)
            grid.addWidget(crt_btn, 3,0)

          

        def get_new_data(self):
            print(self.SName.text())
            Sdata=dbsource.Student(self.SName.text(),self.SId.text(),self.SAge.text(),self.SMajor.text())
            dbsource.Insert_data_tuple(Sdata)
            self.SName.clear()
            self.SId.clear()
            self.SAge.clear()
            self.SMajor.clear()

        def retrive_data(self):
            dbsource.container
            dbsource.Select_allData(self.SSname.text())
            if not dbsource.container:
                self.Notice.clear()
                self.Notice.setText(f"No results found for : {self.SSname.text()}")
                self.Notice.setStyleSheet("color:red")                
                return
            self.SName.setText(dbsource.container[0])
            self.SId.setText(dbsource.container[1])
            self.SAge.setText(str(dbsource.container[2]))
            self.SMajor.setText(dbsource.container[3])
            try:
                self.Submitbtn.clicked.disconnect(self.get_new_data)
                self.Submitbtn.setText("Update")
                self.Submitbtn.clicked.connect(self.Update_chages)
            except :
                pass
            dbsource.container.clear()



        def Update_chages(self):
            self.Submitbtn.setText("Submit")
            self.Submitbtn.clicked.disconnect(self.Update_chages)
            self.Submitbtn.clicked.connect(self.get_new_data)
            Modified_data=dbsource.Student(self.SName.text(),self.SId.text(),self.SAge.text(),self.SMajor.text())
            print(Modified_data)
            dbsource.Update_data(Modified_data,self.SSname.text())
            self.SSname.clear()
            self.SName.clear()
            self.SId.clear()
            self.SAge.clear()
            self.SMajor.clear()

        def delete_all_data(self):
            dbsource.Delete_data_Name(self.SSname.text())
            self.SSname.clear()
            self.SName.clear()
            self.SId.clear()
            self.SAge.clear()
            self.SMajor.clear()




if __name__=='__main__':
        app=QApplication(sys.argv)
        db=db_source()
        sys.exit(app.exec_())



