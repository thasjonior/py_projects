import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QTextEdit, QAction

class all2gether (QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        textEdit = QTextEdit()
        self.setCentralWidget(textEdit)

        x=QAction('Exit',self)
        x.setShortcut('Ctrl+Q')
        x.setStatusTip('Exit application')
        x.triggered.connect(self.close)

        self.statusBar()

        menubar=self.menuBar()
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(x)

        toolbar = self.addToolBar('Exit')
        toolbar.addAction(x)

        self.setGeometry(300,300,300,200)
        self.setWindowTitle('All2gether')
        self.show()
    
if __name__ == '__main__':

    app=QApplication(sys.argv)
    a2g= all2gether()
    sys.exit(app.exec_())
    