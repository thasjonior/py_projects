import sys
import os
import re
import time
from PyQt5.QtWidgets import QMainWindow,QWidget,QPushButton, QScrollArea,QCheckBox,qApp,QWidget,QApplication ,QGridLayout,QLayout,QVBoxLayout
from PyQt5.QtCore import QFileInfo, Qt
from PyQt5.QtGui import QIcon



class Cleaner (QWidget):

    def __init__(self):
        super().__init__()
        self.root = QFileInfo(__file__).absolutePath()
        self.song_dir1=r'/home/judethaddeus/Documents/tester'
        self.song_dir=r'/home/judethaddeus/Music'
        self.items =[]
        self.trash=[]
        self.initUI()

    def initUI(self):
        
        grid=QGridLayout()
        self.get_files(self.song_dir)
        position=[(i,j) for i in range(30) for j in range (2)]
        for position, item in zip (position,self.items):
            self.cb=QCheckBox(item,self)
            self.cb.setIcon(QIcon(r'/home/judethaddeus/Documents/My_projects/py_projects/Cleaner/officialfm-logo.png'))
            self.cb.stateChanged.connect(self.checkStatus)
            grid.addWidget(self.cb, *position)

        # self.trash
        # delete_btn=QPushButton('Delete Marked',self)
        # delete_btn.clicked.connect(self.Delete_checked)

        self.setGeometry(700,700,700,500)  
        self.setWindowTitle("C.L.E.A.N.E.R")
        self.show()

    
    def Delete_checked(self):
        for f in self.trash:
            print("removed")
            os.remove(f)

    def checkStatus(self):
        checkbox=self.sender()
        print(checkbox)
        if checkbox:
            self.addToTrash(self.cb.text())
        else:
            self.removeFromTrash(checkbox.text())

    def addToTrash(self,filename):
        self.trash.append(filename)
        print(self.trash)

    def removeFromTrash(self,filename):
        if len(self.trash)>0:
            self.trash.remove(filename)
       

    def CheckedFile (self,S):
        self.box=QCheckBox(S,self)
        self.box.stateChanged.connect(self.clickBox)

    def Excluded(self,x):
        try:
            pattern=r'(.mp3)$'
            result=re.findall(pattern,x.name)
            if result :
                    return True              

        except TypeError as error:
                print(error)

    def check_outdated(self,x):
            timelimit=24*60*60
            maxtime= os.stat(x).st_atime
            nowtime=time.time()
            timediff= nowtime - maxtime
            if timediff > timelimit:
                    return True

    def get_files(self,song_dir):

        for f in os.scandir(song_dir):
            if f.is_file() and self.Excluded(f) and self.check_outdated(f.path):
                self.items.append(f.path)
            elif f.is_dir():
                self.get_files(f.path)








if __name__ == '__main__':
    app=QApplication(sys.argv)
    cln=Cleaner()
    sys.exit(app.exec_())