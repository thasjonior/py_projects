
import dbsource
import sys
from PyQt5.QtWidgets import QDialog,QFormLayout,QLabel,QMenu,QWidget,QHBoxLayout,QLineEdit,QApplication,QVBoxLayout,QPushButton,qApp,QGroupBox,QGridLayout

class db_source(QDialog):
        def __init__(self):

            super().__init__()
            self.initUI()
        def initUI(self):

            
            self.get_data()
            self.setGeometry(500,500,500,300)
            self.setWindowTitle('Students_Data')
            self.show()

        def get_data(self):
            # dbsource.Create_table()
            Glayout=QGridLayout(self)

            db_filebtn=QPushButton("Choose file",self)
            db_file=QMenu(self)
            db_filebtn.setMenu(db_file)
            Glayout.addWidget(db_filebtn, 0,1)

            Lname=QLabel("Student_Name",self)
            Glayout.addWidget(Lname, 1,0)
            self.SName=QLineEdit(self)
            Glayout.addWidget(self.SName, 1,1)

            Lid=QLabel("Student_Id:",self)
            Glayout.addWidget(Lid, 2,0)
            self.SId=QLineEdit(self)
            Glayout.addWidget(self.SId, 2,1)

            Lage=QLabel("Student_Age",self)  
            Glayout.addWidget(Lage, 3,0)  
            self.SAge=QLineEdit(self)
            Glayout.addWidget(self.SAge ,3,1)

            Lmajor=QLabel("Student_Major:", self)
            Glayout.addWidget(Lmajor, 4,0)
            self.SMajor=QLineEdit(self)
            Glayout.addWidget(self.SMajor, 4,1)

            self.Submitbtn=QPushButton("Submit",self)
            self.Submitbtn.clicked.connect(self.get_new_data)
            Glayout.addWidget(self.Submitbtn, 5,2)

            L2=QLabel(".....Modify Student's Delaits:...", self)
            Glayout.addWidget(L2, 6,0,1,2)

            LMname=QLabel("Enter name:",self)
            Glayout.addWidget(LMname, 7,0)
            self.SSname=QLineEdit(self)
            Glayout.addWidget(self.SSname, 7,1)
            Searchbtn=QPushButton("Search",self)
            Searchbtn.clicked.connect(self.retrive_data)
            Glayout.addWidget(Searchbtn, 7,2)

            LResults=QLabel("..........Search Results.....",self)
            Glayout.addWidget(LResults, 8,1)

            

            MName=QLabel("Student_Name",self)
            Glayout.addWidget(MName, 9,0)
            self.Mname=QLineEdit(self)
            Glayout.addWidget(self.Mname, 9,1)

            MId=QLabel("Student_Id:",self)
            Glayout.addWidget(MId, 10,0)
            self.Mid=QLineEdit(self)
            Glayout.addWidget(self.Mid, 10,1)

            MAge=QLabel("Student_Age",self)  
            Glayout.addWidget(MAge, 11,0)  
            self.Mage=QLineEdit(self)
            Glayout.addWidget(self.Mage ,11,1)

            MMajor=QLabel("Student_Major:", self)
            Glayout.addWidget(MMajor, 12,0)
            self.Mmajor=QLineEdit(self)
            Glayout.addWidget(self.Mmajor, 12,1)

            Deletebtn=QPushButton("Delete",self)
            Deletebtn.clicked.connect(self.delete_all_data)
            Glayout.addWidget(Deletebtn, 13,0)
            M_submitbtn=QPushButton("Update Changes",self)
            M_submitbtn.clicked.connect(self.Update_chages)
            Glayout.addWidget(M_submitbtn, 13,1)
            Updatebtn=QPushButton("Cancel",self)
            Glayout.addWidget(Updatebtn, 13,2)


          

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
                self.SName.setText(f"No such information {self.SName.text()}")
                self.SName.setStyleSheet("color:red")
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
            self.SName.clear()
            self.SId.clear()
            self.SAge.clear()
            self.SMajor.clear()

        def delete_all_data(self):
            dbsource.Delete_data_Name(self.SSname.text())
            self.SSname.clear()
            self.Mname.clear()
            self.Mid.clear()
            self.Mage.clear()
            self.Mmajor.clear()




if __name__=='__main__':
        app=QApplication(sys.argv)
        db=db_source()
        sys.exit(app.exec_())



