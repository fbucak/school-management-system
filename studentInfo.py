from PyQt5 import QtWidgets,uic
import studentLogin

class studentInfoScreen(QtWidgets.QMainWindow):
    def __init__(self,student):
        super(studentInfoScreen, self).__init__()
        self.student=student
        uic.loadUi('ui/studentInfo.ui', self)
        self.studentExit.clicked.connect(self.studentInfoExit)
        self.sNameLine.setText(student[0][2])
        self.sNameLine1.setText(student[0][3])
        self.sAddorDeleteLine_3.setText(str(student[0][1]))
        self.show()

    def studentInfoExit(self):
            self.inci=studentLogin.student_entry(self.db)
            self.inci.show()
            self.close()