import sys
from PyQt5.QtWidgets import QWidget,QLabel,QApplication

class Example (QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):

        lbl1=QLabel('Grinappo', self)
        lbl1.move(15,10)

        lb2=QLabel('phones', self)
        lb2.move(35,40)

        lb3=QLabel('computer', self)
        lb3.move(55, 70)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle('Absolute')
        self.show()

if __name__ == '__main__':
     app=QApplication(sys.argv)
     x= Example()
     sys.exit(app.exec_())

