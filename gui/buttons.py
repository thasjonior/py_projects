import sys
from PyQt5.QtWidgets import (QWidget,QScrollArea,QPushButton,QVBoxLayout,QVBoxLayout, QApplication)

class Button(QWidget):

    def __init__(self):
        super(). __init__()
        self.initUI()

    def initUI(self):
        sa=QScrollArea(self)
        okButton= QPushButton('OK')
        cancelButton=QPushButton('Cancel')
        okButton1= QPushButton('OK')
        cancelButton1=QPushButton('Cancel')
        okButton2= QPushButton('OK')
        cancelButton2=QPushButton('Cancel')
        okButton3= QPushButton('OK')
        cancelButton3=QPushButton('Cancel')

        hbox=QVBoxLayout()
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addWidget(okButton1)
        hbox.addWidget(cancelButton1)
        hbox.addWidget(okButton2)
        hbox.addWidget(cancelButton2)
        hbox.addWidget(okButton3)
        hbox.addWidget(cancelButton3)

        vbox=QVBoxLayout()
        vbox.addStretch(-1)
        vbox.addLayout(hbox)

        sa.setLayout(vbox)

        self.setGeometry(300,300,300,150)
        self.setWindowTitle('Buttons')
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    bb= Button()
    sys.exit(app.exec_())
