import sys
import os
from PyQt5.QtWidgets import QWidget,QMenu,QListWidget,QMessageBox,QApplication,QLabel,QFileDialog,QPushButton,QTextEdit,QGridLayout,QVBoxLayout

class mainapp (QWidget):

    def __init__(self):
        super().__init__()
        self. initUI()
    
    def initUI(self):

        self.setMain_window()
        self.container1=[]
        self.setGeometry(500,500,500,600)
        self.setWindowTitle("A_N_T_I.duplicates")
        self.show()

    def setMain_window(self):
        grid=QGridLayout(self)

        Folder_btn=QPushButton("Add folder to inspect!",self)
        Folder_btn.clicked.connect(self.print_duplicates)
        grid.addWidget(Folder_btn,0,0)

        open_btn=QPushButton("Open",self)
        grid.addWidget(open_btn,0,1)

        self.info_lb=QLabel("All information to be displayed here......................",self)
        grid.addWidget(self.info_lb, 1,0,1,2)

        btn1=QPushButton("Button1",self)
        grid.addWidget(btn1,2,0)

        btn2=QPushButton("Delete selected",self)
        btn2.clicked.connect(self.delete_selected)
        grid.addWidget(btn2, 2,1)

        self.displayfield=QListWidget(self)
        self.displayfield.setSelectionMode(3)
        self.displayfield.itemClicked.connect(self.get_selected)
        grid.addWidget(self.displayfield, 3,0,1,2)

    def get_maindir(self):
        dir=os.environ['HOME']
        return QFileDialog.getExistingDirectory(parent=self, caption="Select a directory to inspect ", directory=dir)
    
    def print_duplicates(self):
        path=self.get_maindir()
        l=QListWidget(self)
        self.dups=self.findDuplicates(path)
        for item in self.dups:
            new=item/1024
            self.displayfield.addItem(f"files with size {new} MB")
            for value in self.dups.get(item):
                self.displayfield.addItem(value)
    # this gets all files from the directory 
    def getDuplicates(self,path, dictionary):
        try:
            for entry in os.scandir(path):
                if entry.is_file():
                    # check if this file size is a key in found_files
                    if dictionary.get(entry.stat().st_size):
                        dictionary[entry.stat().st_size].append(entry.path)
                    else:
                        dictionary[entry.stat().st_size] = [entry.path]
                elif entry.is_dir():
                    self.getDuplicates(entry.path, dictionary)
        except PermissionError and OSError as e:
            pass
            # print(e)

    #this sort all files to get only the duplicates
    def findDuplicates(self,path):
        found_files = {}
        self.getDuplicates(path, found_files)
        duplicates = {}
        for size, files in found_files.items():
            if len(files) > 1:
                duplicates[size] = files
        return duplicates

    def get_selected(self,item):
        source=self.sender()
        print(item.text())
        return self.container1.append(source)

    def delete_selected(self):
        if not self.displayfield.selectedItems():
            self.info_lb.setText("Nothing is selected")
            return

        txtbox=QMessageBox(self)
        txtbox.setText("you sure")
        txtbox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        var=txtbox.exec()
        if var == 1024:
            for item in self.displayfield.selectedItems():
                print("Deleting...")
                os.remove(item.text())
                self.displayfield.takeItem(self.displayfield.row(item))
        else:
            return





if __name__ == '__main__':
    app=QApplication(sys.argv)
    a_d=mainapp()
    sys.exit(app.exec_())