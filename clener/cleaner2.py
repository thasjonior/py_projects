import sys
import re 
import time
import os
from PyQt5.QtWidgets import QWidget,QApplication,QGridLayout,QCheckBox,QPushButton,QScrollArea
from PyQt5.QtCore import QFileInfo, Qt
from PyQt5.QtGui import QIcon

class cleaner(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300,300,400,550)
        self.setWindowTitle("-C.L.E.A.N.E.R-")
        self.show()

if __name__=='__main__':
    app=QApplication(sys.argv)
    cln=cleaner()
    sys.exit(app.exec_())