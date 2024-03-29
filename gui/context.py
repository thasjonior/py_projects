import sys
from PyQt5.QtWidgets import QMainWindow, qApp, QMenu, QApplication

class Context(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.setGeometry(300, 300,400,400)
        self.setWindowTitle('Context')
        self.show()
        
# this fx creates the context menu
    def contextMenuEvent(self,event):

        cmenu= QMenu(self)
        newAct=cmenu.addAction('New')
        opnAct=cmenu.addAction('Open')
        qtAct=cmenu.addAction('Quit')
        action=cmenu.exec_(self.mapToGlobal(event.pos()))

        if action == qtAct:
            qApp.quit()

if __name__ == '__main__':

    app=QApplication(sys.argv)
    cont=Context()
    sys.exit(app.exec_())