from PyQt5 import QtWidgets,uic
import windowOne
class student_entry(QtWidgets.QMainWindow):
        def __init__(self):
            super(student_entry, self).__init__()
            uic.loadUi('ui/studentLoginPage.ui', self)
            self.backbutton.clicked.connect(self.entry_show)
        
        def entry_show(self):
            self.inci=windowOne.login()
            self.inci.show()
            self.close()