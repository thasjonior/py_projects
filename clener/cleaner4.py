import sys
import os
import re 
import os
import time
from PyQt5.QtWidgets import QWidget,QApplication,QListWidgetItem,QFileDialog,QLineEdit,QListWidget,QGridLayout,QCheckBox,QPushButton,QMessageBox
from PyQt5.QtCore import QFileInfo, Qt
from PyQt5.QtGui import QIcon

class Cleaner (QWidget):

    def __init__(self):
        super().__init__()
        self.items ={}
        self.initUI()

    def initUI(self):
        self.main_window()
        self.setGeometry(700,700,700,500)  
        self.setWindowTitle("Clean Outdated files")
        self.show()

    def main_window(self):

        grid=QGridLayout(self)   
        
        main_folder=QPushButton('choose folder',self) 
        main_folder.clicked.connect(self.show_files)
        grid.addWidget(main_folder,0,0,1,2) 

        self.dayslimit=QLineEdit("7",self)
        grid.addWidget(self.dayslimit,1,0)

        set_btn=QPushButton('Set',self)
        set_btn.clicked.connect(self.get_dayslimit)
        grid.addWidget(set_btn,1,1)

        dlt_btn=QPushButton('Delete Selected',self)
        dlt_btn.clicked.connect(self.Delete_selected)
        grid.addWidget(dlt_btn,2,0)

        cancel_btn=QPushButton("Cancel",self)
        grid.addWidget(cancel_btn,2,1)

        self.lst=QListWidget(self)
        self.lst.setSelectionMode(3)
        self.lst.itemClicked.connect(self.get_selected)
        grid.addWidget(self.lst,3,0,2,2)

# this receive days for file being out ofdate and usless
    def get_dayslimit(self):
        # this had to be refreshing
        return int(self.dayslimit.text())

# this returns directory from user    
    def get_dir(self):
        return QFileDialog.getExistingDirectory(parent=self, caption='choose folder',directory=os.environ['HOME'])

#deletes seledcted files items already in trash
    def Delete_selected(self):
        if not self.lst.selectedItems():
            return
        confirm=QMessageBox(self)
        confirm.setText("Are sure to delete selected files")
        confirm.setStandardButtons(QMessageBox.Cancel | QMessageBox.Ok)
        var=confirm.exec()

        if var == 1024:
             for f in self.lst.selectedItems():
                print(f"deleteng...{f.text()}")
                try:
                    os.remove(f.text())
                except FileNotFoundError as e:
                    print(e)
                self.lst.takeItem(self.lst.row(f))
        for f in self.lst.selectedItems():
            print(f.text()) 

#sort file by time since last accessed
    def check_outdated(self,x,Y=None):
            timelimit=Y*24*60*60
            maxtime= os.stat(x).st_atime
            nowtime=time.time()
            timediff= nowtime - maxtime
            if timediff > timelimit:
                    return True  
#display target files onto the window by their directory 
    def show_files(self):
        dir=self.get_dir()
        self.present_files(dir)

#receive process and display target files onto the window
    def present_files(self,dir):
        self.lst.clear()
        def sort_files(dir):
            for item in os.scandir(dir):
                if item.is_file() and self.check_outdated(item.path,self.get_dayslimit()):
                    self.Ilist=QListWidgetItem(self.lst)
                    # Ilist.setIcon(QIcon(r'/home/judethaddeus/Documents/My_projects/py_projects/clener/officialfm-logo.png'))
                    self.set_specificIcon(str(item).lower())
                    self.Ilist.setText(item.path)
                elif item.is_dir():
                    sort_files(item.path)
        sort_files(dir)


    def set_specificIcon(self,item):
        photo=r'(.png|.jpg|.gif|.jpeg|.bmp|.jpg)'
        music=r'(.mp3)'
        vid=r'(.mp4)'
        pdf=r'(.pdf)'
        doc=r'(.doc|.txt)'
        if re.findall(music,item):
            print("music")
            self.Ilist.setIcon(QIcon(r'/home/judethaddeus/myprojects/py_projects/clener/music.png'))
        elif re.findall(photo,item):
            print("photo")
            self.Ilist.setIcon(QIcon(r'/home/judethaddeus/myprojects/py_projects/clener/photo.png'))
        elif re.findall(vid,item):
            print("video")
            self.Ilist.setIcon(QIcon(r'/home/judethaddeus/myprojects/py_projects/clener/vid.png'))
        elif re.findall(doc,item):
            print("document")
            self.Ilist.setIcon(QIcon(r'/home/judethaddeus/myprojects/py_projects/clener/doc.png'))
        elif re.findall(pdf,item):
            print("pdf")
            self.Ilist.setIcon(QIcon(r'/home/judethaddeus/myprojects/py_projects/clener/pdf.png'))
        else:
            print("another")
            self.Ilist.setIcon(QIcon(r'/home/judethaddeus/myprojects/py_projects/clener/ukw.png'))



    def get_selected(self,item):
         source=self.sender()
         print(item.text())

if __name__ =='__main__':
    app=QApplication(sys.argv)
    cln=Cleaner()
    sys.exit(app.exec_())