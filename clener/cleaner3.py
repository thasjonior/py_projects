import sys
import os
import re 
import time
import os
from PyQt5.QtWidgets import QWidget,QApplication,QListWidgetItem,QFileDialog,QListWidget,QGridLayout,QCheckBox,QPushButton,QScrollArea,QVBoxLayout
from PyQt5.QtCore import QFileInfo, Qt
from PyQt5.QtGui import QIcon

class Cleaner (QWidget):

    def __init__(self):
        super().__init__()
        self.root = QFileInfo(__file__).absolutePath()
        self.song_dir1=r'/home/judethaddeus/Documents/tester'
        self.song_dir=r'/home/judethaddeus/Music'
        self.items ={}
        self.trash=[]
        self.initUI()

    def initUI(self):
        self.main_window()
        self.setGeometry(700,700,700,500)  
        self.setWindowTitle("C.L.E.A.N.E.R")
        self.show()
        # self.get_files(self.song_dir)
        # self.lst=QListWidget(self)
        
        # for self.item in self.items:


    def main_window(self):

        grid=QGridLayout(self)   
        
        main_folder=QPushButton('choose folder',self) 
        main_folder.clicked.connect(self.present_files)
        grid.addWidget(main_folder,0,0,1,2) 

        dlt_btn=QPushButton('Delete Selected',self)
        dlt_btn.clicked.connect(self.Delete_checked)
        grid.addWidget(dlt_btn,1,0)

        cancel_btn=QPushButton("Cancel",self)
        grid.addWidget(cancel_btn,1,1)

        self.lst=QListWidget(self)
        self.lst.setSelectionMode(3)
        self.lst.itemClicked.connect(self.get_selected)
        grid.addWidget(self.lst,2,0,2,2)




    def get_dir(self):
        return QFileDialog.getExistingDirectory(parent=self, caption='choose folder',directory=os.environ['HOME'])

    #deletes checked items already in trash
    def Delete_checked(self):
        for f in self.trash:
            print("removed")
            os.remove(f)
    #sort if item is checked or unchecked and add or remove from trash respectively
    def checkStatus(self):
        selected =self.sender()
        if selected:
            print (selected)
            self.addToTrash(self.items.get(self.item))
        else:
            print("not selected")
            self.removeFromTrash(self.item[0])
    #add checked item into trash container
    def addToTrash(self,filename):
        self.trash.append(filename)
        print(self.trash)
    #revome unchecked item from trash
    def removeFromTrash(self,filename):
        if len(self.trash)>0:
            self.trash.remove(filename)
       
    #sort file by (.mp3) extension  
    def Excluded(self,x):
        try:
            pattern=r'(.mp3)$'
            result=re.findall(pattern,x.name)
            if result :
                    return True              

        except TypeError as error:
                print(error)

    #sort file by time since last accessed
    def check_outdated(self,x):
            timelimit=24*60*60
            maxtime= os.stat(x).st_atime
            nowtime=time.time()
            timediff= nowtime - maxtime
            if timediff > timelimit:
                    return True

    #clolect targets to items container
    def get_files(self,song_dir):
        for f in os.scandir(song_dir):
            if f.is_file() and self.Excluded(f) and self.check_outdated(f.path):
                self.items[f.name]=f.path
            elif f.is_dir():
                self.get_files(f.path)

    def present_files(self):
        self.get_files(self.get_dir())
        for item in self.items:
            Ilist=QListWidgetItem(self.lst)
            Ilist.setIcon(QIcon(r'/home/judethaddeus/Documents/My_projects/py_projects/clener/officialfm-logo.png'))
            Ilist.setText(item)




    def get_selected(self,item):
         source=self.sender()
         print(item.txt)



if __name__=='__main__':
    app=QApplication(sys.argv)
    cln=Cleaner()
    sys.exit(app.exec_())