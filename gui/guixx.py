import sys
from PyQt5.QtWidgets import QWidget,QApplication
class Gudi(QWidget):
    def __init__(self):
        super().__init__()
        self.tata()
    def tata(self):
        
        self.setGeometry(300,300,300,200)
        self.setWindowTitle("GUDI")
        self.show()
if __name__ == '__main__':
    app=QApplication(sys.argv)
    Cx=Gudi()
    sys.exit(app.exec_())