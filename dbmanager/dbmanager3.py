# few bugs ,long functions,create window,db general functioning idea
import dbsource2
import sys
import os
import re
import time
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QMainWindow,QFormLayout,QAction,QDialog,QFileDialog,QFormLayout,QTextEdit,QListWidget,QLabel,QMenu,QWidget,QHBoxLayout,QLineEdit,QApplication,QVBoxLayout,QPushButton,qApp,QMenu,QGroupBox,QGridLayout

class db_source(QWidget ):
        def __init__(self):

            super().__init__()
            self.initUI()
        def initUI(self):
            self.main_layout=QVBoxLayout(self)
            self.Main_window()
            self.setGeometry(500,500,500,300)
            self.setWindowTitle('Students_Data')
            self.tempo_dict={}
            self.show()           


#main window
        def Main_window(self):
            self.sub_widget1=QWidget(self)
            grid=QGridLayout(self)
            self.add_widget(self.sub_widget1,grid)
            
            srch_bar=QLineEdit(self)
            grid.addWidget(srch_bar, 0,0)
            self.pick_db_file()
            srch_btn=QPushButton("Search",self)
            grid.addWidget(srch_btn, 0,1)

            self.results=QListWidget(self)
            grid.addWidget(self.results, 1,0,1,2)

            view_btn=QPushButton("View Table",self)
            view_btn.clicked.connect(self.get_data)
            grid.addWidget(view_btn, 2,0)
            
            self.open_btn=QPushButton("Open",self)
            self.open_btn.setMenu(self.menu)
            self.open_btn.clicked.connect(self.pick_db_file)
            grid.addWidget(self.open_btn, 2,1)

            crt_btn=QPushButton("Create Table",self)
            crt_btn.clicked.connect(self.createtable_window)
            grid.addWidget(crt_btn, 3,0)

            
#createtable window
        def createtable_window(self):

            self.replace_widget(self.sub_widget1)
            self.sub_widget2=QWidget(self)
            self.grid=QGridLayout(self)
            self.add_widget(self.sub_widget2,self.grid)

            self.main_layout.addWidget(self.sub_widget2)

            
            
            TName=QLineEdit(self)
            self.grid.addWidget(TName,0,0,1,2)

            self.col_no=QLineEdit(self)
            self.grid.addWidget(self.col_no,1,0)

            self.submit_btn=QPushButton('submit',self)
            self.submit_btn.clicked.connect(self.get_columns)
            self.grid.addWidget(self.submit_btn,1,1)

            self.sub_widget2.setLayout(self.grid)
            self.sub_widget2.show()

#modification window
        def get_data(self):
            self.get_user_columns()
            for val in self.tempo_dict:
                print(val)
            try:
                if self.sub_widget1:
                    print("bug here")
                    self.replace_widget(self.sub_widget1)
                    self.edit=True
                if self.sub_widget2:
                    print("bug there")
                    self.replace_widget(self.sub_widget2)
                    self.edit=False
                    self.create=True
            except AttributeError as e:
                print("cant replace widget tha is not created")

            self.sub_widget3=QWidget(self)
            Glayout=QGridLayout(self)
            self.add_widget(self.sub_widget3,Glayout)

            LMname=QLabel("Enter name:",self)
            Glayout.addWidget(LMname, 0,0)
            self.SSname=QLineEdit(self)
            Glayout.addWidget(self.SSname, 0,1)
            Searchbtn=QPushButton("Search",self)
            Searchbtn.clicked.connect(self.retrive_data)
            Glayout.addWidget(Searchbtn, 0,2)

            if self.edit:
                self.Notice=QLabel("NOTE:",self)
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
                num=5

            elif self.create:
                row = 1
                for key,value in self.tempo_dict.items():
                    Glayout.addWidget(QLabel(value,self),row,0)
                    Glayout.addWidget(QLineEdit(self),row,1)
                    row+=1
                num=int(self.col_no.text())+1


            self.Submitbtn=QPushButton("Submit",self)
            self.Submitbtn.clicked.connect(self.get_new_data)
            Glayout.addWidget(self.Submitbtn, num,0)
            Deletebtn=QPushButton("Delete",self)
            Deletebtn.clicked.connect(self.delete_all_data)
            Glayout.addWidget(Deletebtn, num,1)
            Cancelbtn=QPushButton("Cancel",self)
            Cancelbtn.clicked.connect(self.cancel_operation)
            Glayout.addWidget(Cancelbtn, num,2)
            self.tempo_dict.clear()

            

        def pick_db_file(self):
            self.menu=QMenu(self)
            for file in  os.scandir(r'/home/judethaddeus/myprojects/py_projects/dbmanager'):
                partten=r'(\.db)$'
                matches=re.findall(partten,file.name)
                for _ in  range(len(matches)):
                    action=self.menu.addAction(file.name)
                    action.triggered.connect( self.trial)
        def trial(self):
            source=self.sender()
            dbsource2.conn=dbsource2.get_dbFile(source.text())
            dbsource2.c=dbsource2.conn.cursor()
            print(source.text()) 
            self.Present_Table()

        def get_new_data(self):
            print(self.SName.text())
            Sdata=dbsource2.Student(self.SName.text(),self.SId.text(),self.SAge.text(),self.SMajor.text())
            dbsource2.Insert_data_tuple(Sdata)
            self.SName.clear()
            self.SId.clear()
            self.SAge.clear()
            self.SMajor.clear()

        def retrive_data(self):
            dbsource2.container
            dbsource2.Select_allData(self.SSname.text())
            if not dbsource2.container:
                self.Notice.clear()
                self.Notice.setText(f"No results found for : {self.SSname.text()}")
                self.Notice.setStyleSheet("color:red")                
                return
            self.SName.setText(dbsource2.container[0])
            self.SId.setText(dbsource2.container[1])
            self.SAge.setText(str(dbsource2.container[2]))
            self.SMajor.setText(dbsource2.container[3])
            try:
                self.Submitbtn.clicked.disconnect(self.get_new_data)
                self.Submitbtn.setText("Update")
                self.Submitbtn.clicked.connect(self.Update_chages)
            except :
                pass
            dbsource2.container.clear()

        def Update_chages(self):
            self.Submitbtn.setText("Submit")
            self.Submitbtn.clicked.disconnect(self.Update_chages)
            self.Submitbtn.clicked.connect(self.get_new_data)
            Modified_data=dbsource2.Student(self.SName.text(),self.SId.text(),self.SAge.text(),self.SMajor.text())
            print(Modified_data)
            dbsource2.Update_data(Modified_data,self.SSname.text())
            self.SSname.clear()
            self.SName.clear()
            self.SId.clear()
            self.SAge.clear()
            self.SMajor.clear()

        def delete_all_data(self):
            dbsource2.Delete_data_Name(self.SSname.text())
            self.SSname.clear()
            self.SName.clear()
            self.SId.clear()
            self.SAge.clear()
            self.SMajor.clear()

        def Present_Table(self):
            self.results.clear()
            dbsource2.ss.clear()
            dbsource2.Read_all_contents()
            for row in dbsource2.ss:
                self.results.addItem(str(row))
            print("Table presented")
      
        def cancel_operation(self):
            try:
                if self.sub_widget1:
                    print("bug1")
                    self.replace_widget(self.sub_widget1)
                if self.sub_widget2:
                    print("bug2")
                    self.replace_widget(self.sub_widget2)
                if self.sub_widget3:
                    print("bug3")
                    self.replace_widget(self.sub_widget3)
            except AttributeError as e:
                print("this replace any previous widget to home widget")
            finally:
                self.Main_window()

        def get_columns(self):
            from PyQt5.QtCore import QRect
            cols=int(self.col_no.text())
            layout_item=self.grid.itemAtPosition(2,0)
            if layout_item:
                print(layout_item.itemAt(0).widget().text())               
                self.grid.removeItem(layout_item)
                layout_item.setGeometry(QRect(0,0,0,0))
            self.tempo_dict={}
            form_layout=QFormLayout(self)
            for i in range(cols):
                name=f"Column {i+1}"
                one=i+2
                i=QLabel(name,self)
                id=QLineEdit(self)
                form_layout.addRow(i,id)
            self.grid.addLayout(form_layout,2,0,1,2)

            # for y in range(cols):
            #     one=y+2
            #     id=QLineEdit(self)
            #     self.grid.addWidget(id,one,1)
            #     self.tempo_dict[y]=''
                    

            create_btn=QPushButton("create",self)
            create_btn.clicked.connect(self.get_data)
            self.grid.addWidget(create_btn,3,0,1,2)

        def replace_widget(self,widget):
            self.main_layout.removeWidget(widget)
            widget.hide()

        def add_widget(self,widget,layout):
            self.main_layout.addWidget(widget)
            widget.setLayout(layout)
            widget.show()
        
        def get_user_columns(self):
            # for item in self.tempo_list
            for key in self.tempo_dict:
                self.tempo_dict[key]=key.text()

if __name__=='__main__':
        app=QApplication(sys.argv)
        db=db_source()
        sys.exit(app.exec_())



