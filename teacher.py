from PyQt5 import QtWidgets,uic
import windowOne

class teacher_entry(QtWidgets.QMainWindow):
        def __init__(self):
            super(teacher_entry, self).__init__()
            uic.loadUi('ui/teacherLoginPage.ui', self)
            self.backbutton2.clicked.connect(self.entry_show)
        
        def entry_show(self):
            self.inci=windowOne.login()
            self.inci.show()
            self.close()