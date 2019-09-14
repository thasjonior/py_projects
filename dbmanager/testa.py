# import sys
# from PyQt5.QtWidgets import QWidget,QApplication,QGridLayout,QLabel,QLineEdit,QPushButton,QVBoxLayout,QFormLayout

# class guitesta(QWidget):
#     def __init__(self):
#         super().__init__()
#         self.initUI()
#     def initUI(self):
#         self.setWindowTitle("testa")
#         self.setGeometry(550,500,500,100)
#         self.show()
      

#         pass

# if __name__=='__main__':
#     app=QApplication(sys.argv)
#     gui=guitesta()
#     sys.exit(app.exec_())

class nn:
    def __init__(self,*n):
        for a in n:
            val=f'self.{a}'
            val=a

z=nn("moja","mbili")
print(z.moja)