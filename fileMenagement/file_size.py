import os
import sys
import re
import source_code as source 
from PyQt5.QtWidgets import QWidget,QApplication,QPushButton,QFileDialog,QGridLayout,QTextEdit,QListWidget

class file_size (QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.main_window()
        self.setGeometry(500,500,500,600)
        self.setWindowTitle("File_Size...manager")
        self.show()

    def main_window(self):
        grid=QGridLayout(self)

        maindir=QPushButton('select directory')
        maindir.clicked.connect(self.present_files)
        grid.addWidget(maindir,0,0,1,2)

        btn1=QPushButton("Create Record ",self)
        btn1.clicked.connect(self.create_record)
        grid.addWidget(btn1,1,0)

        btn2=QPushButton("Delete Record",self)
        btn2.clicked.connect(self.delete_record)
        grid.addWidget(btn2,1,1)

        self.info=QListWidget(self)
        grid.addWidget(self.info,2,0,1,2)

    def get_maindir(self): 
        return QFileDialog.getExistingDirectory(parent=self,caption='select directory',directory=os.environ['HOME'])
        

                    
#this display filesize.txt present in given directory            
    def present_files(self):
        self.info.clear()
        source.path=self.get_maindir()
        source.collect_targets(source.path)
        for item in source.dict:
            self.info.addItem(item)
        source.dict.clear()
        
#this creates filesize.txt into the entire directory given
    def create_record(self):
        self.info.clear()
        source.path=self.get_maindir()
        source.GetFile(source.path)
        for item in source.dict:
            self.info.addItem(item)
        source.dict.clear()

#this deletes all filesize.txt from entire directory given
    def delete_record(self):
        self.info.clear()
        source.dict.clear()
        source.delete_all_Sfile(source.path)

                
if __name__ =='__main__':
    app=QApplication(sys.argv)
    fs=file_size()
    sys.exit(app.exec_())