# improvement from dbmanager3
#more shot functions
#debug dbmanager3

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
            view_btn.clicked.connect(self.modify_window)
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

            
            self.grid.addWidget(QLabel("Table Name:",self),0,0)
            self.Tname=QLineEdit(self)
            self.grid.addWidget(self.Tname,0,1)
            self.grid.addWidget(QLabel("Columns numer:",self),1,0)
            self.col_no=QLineEdit(self)
            self.grid.addWidget(self.col_no,1,1)

            self.submit_btn=QPushButton('submit',self)
            self.submit_btn.clicked.connect(self.get_columns)
            self.grid.addWidget(self.submit_btn,2,1)


#modification window
        def modify_window(self):
            self.get_user_columns()

#make decision betwwen the edit mode or create mode onto the modification window
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

#search section in modification window
            LMname=QLabel("Enter name:",self)
            Glayout.addWidget(LMname, 0,0)
            self.SSname=QLineEdit(self)
            Glayout.addWidget(self.SSname, 0,1)
            Searchbtn=QPushButton("Search",self)
            Searchbtn.clicked.connect(self.retrive_data)
            Glayout.addWidget(Searchbtn, 0,2)
            
#edit mode in modification window
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
#create mode in modification window
            elif self.create:
                form_layout=QFormLayout(self)
                for key,value in self.tempo_dict.items():
                    form_layout.addRow(QLabel(value,self),QLineEdit(self))
                Glayout.addLayout(form_layout,1,0,1,3)
                num=int(self.col_no.text())+1

#modification window buttons
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

#this picks datbase file thart exist in databse folder
        def pick_db_file(self):
            self.menu=QMenu(self)
            for file in  os.scandir(r'/home/judethaddeus/myprojects/py_projects/dbmanager'):
                partten=r'(\.db)$'
                matches=re.findall(partten,file.name)
                for _ in  range(len(matches)):
                    action=self.menu.addAction(file.name)
                    action.triggered.connect( self.pull_dbfile)

#this pulls bdfile and asign if ready to be used in database system       
        def pull_dbfile(self):
            source=self.sender()
            dbsource2.conn=dbsource2.get_dbFile(source.text())
            dbsource2.c=dbsource2.conn.cursor()
            print(source.text()) 
            self.Present_Table()

#this pick new data from edit window 
        def get_new_data(self):
            print(self.SName.text())
            Sdata=dbsource2.Student(self.SName.text(),self.SId.text(),self.SAge.text(),self.SMajor.text())
            dbsource2.Insert_data_tuple(Sdata)
            self.clear_field(self.SName,self.SId,self.SAge,self.SMajor)

#this read data from the database and present them on the view
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

#this update changes by picking updates from display section
        def Update_chages(self):
            self.Submitbtn.setText("Submit")
            self.Submitbtn.clicked.disconnect(self.Update_chages)
            self.Submitbtn.clicked.connect(self.get_new_data)
            Modified_data=dbsource2.Student(self.SName.text(),self.SId.text(),self.SAge.text(),self.SMajor.text())
            print(Modified_data)
            dbsource2.Update_data(Modified_data,self.SSname.text())
            self.clear_field(self.SSname,self.SName,self.SId,self.SAge,self.SMajor)
#this cleans the edit field as well delete target content from database
        def delete_all_data(self):
            dbsource2.Delete_data_Name(self.SSname.text())
            self.clear_field(self.SSname,self.SName,self.SId,self.SAge,self.SMajor)

#this read all table from database and present it on display
        def Present_Table(self):
            self.clear_field(self.results,dbsource2.ss)
            dbsource2.Read_all_contents()
            for row in dbsource2.ss:
                self.results.addItem(str(row))
            print("Table presented")

#this cancels operation    and return to the main window
        def cancel_operation(self):
            try:
                self.replace_widget(self.sub_widget1)
                self.replace_widget(self.sub_widget2)
                self.replace_widget(self.sub_widget3)

            except AttributeError as e:
                print("this replace any previous widget to home widget")
            finally:
                self.Main_window()

#this colects columns name sa specified by user so to create table
        def get_columns(self):
            from PyQt5.QtCore import QRect
            cols=int(self.col_no.text())
            layout_item=self.grid.itemAtPosition(3,0)
            if layout_item:
                print(layout_item.itemAt(0).widget().text())               
                self.grid.removeItem(layout_item)
                layout_item.setGeometry(QRect(0,0,0,0))
            self.tempo_dict={}
            form_layout=QFormLayout(self)
            for i in range(cols):
                col_key=QLineEdit(self)
                self.tempo_dict[col_key]=''
                form_layout.addRow(QLabel(f"Column {i+1}",self),col_key)
            self.grid.addLayout(form_layout,3,0,1,2)

            create_btn=QPushButton("create",self)
            create_btn.clicked.connect(self.modify_window)
            self.grid.addWidget(create_btn,4,0,1,2)

#this removes formar widget ready to add new one
        def replace_widget(self,widget):
            self.main_layout.removeWidget(widget)
            widget.hide()

#this add new widget to main layout
        def add_widget(self,widget,layout):
            self.main_layout.addWidget(widget)
            widget.setLayout(layout)
            widget.show()

#this stores the column name specified by user so to be used later
        def get_user_columns(self):
            for key,val in self.tempo_dict.items():
                self.tempo_dict[key]=key.text()

#this clear contenst ni various field or methods
        def clear_field(self,*fields):
            for field in fields:
                field.clear()
                


if __name__=='__main__':
        app=QApplication(sys.argv)
        db=db_source()
        sys.exit(app.exec_())



