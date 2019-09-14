import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QAction

class check_menu(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):

        self.statusbar= self.statusBar()
        self.statusbar.showMessage('Ready')

        menubar = self.menuBar()
        viewMenu= menubar.addMenu('View')

        x=QAction('Veiw Statusbar', self, checkable=True)
        x.setStatusTip('View Statusbar')
        x.setChecked(True)
        x.triggered.connect(self.toggleMenu)

        viewMenu.addAction(x)

        self.setGeometry(300,300,300,220)
        self.setWindowTitle('Check menu')
        self.show()

    def toggleMenu(self,state):

        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

if __name__ =='__main__':

    app =QApplication(sys.argv)
    check=check_menu()
    sys.exit(app.exec_())

