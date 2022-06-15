from PyQt5 import QtWidgets,uic
import studentLogin

class studentInfoScreen(QtWidgets.QMainWindow):
    def __init__(self,db,number):
        super(studentInfoScreen, self).__init__()
        self.db=db
        self.number=number
        uic.loadUi('ui/studentInfo.ui', self)
        self.studentExit.clicked.connect(self.studentInfoExit)
        self.show()

    def studentInfoExit(self):
            self.inci=studentLogin.student_entry(self.db)
            self.inci.show()
            self.close()