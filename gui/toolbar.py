import sys
from PyQt5.QtWidgets import QWidget,QMainWindow, QAction, qApp, QApplication

class tool_bar(QWidget and QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
     
    def initUI(self):

        exitAct=QAction('Exit',self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)

        self.toolbar =self.addToolBar('Exit')
        # self.toolbar1= self.addToolBar('Home') must hav action unit
        self.toolbar.addAction(exitAct)

        self.setGeometry(300,300,300,300)
        self.setWindowTitle("ToolBar")
        self.show()

if __name__ == '__main__':

    app = QApplication(sys.argv)
    TB= tool_bar()
    sys.exit(app.exec_())
