from PyQt5 import QtWidgets,uic,QtGui
import studentLogin
import teacherLogin
from PyQt5.QtWidgets import QPushButton


lessons=["Matematik","Fizik","Kimya"]
class teacherInfoScreen(QtWidgets.QMainWindow):
    
    def __init__(self,db):
        super(teacherInfoScreen, self).__init__()
        uic.loadUi('ui/teacherInfo.ui', self)
        self.db=db
        self.teacherExit.clicked.connect(self.teacherInfoExit)
        # self.forStudent.clicked.connect(self.StudentLoginPage)
        # self.forTeacher.clicked.connect(self.TeacherLoginPage)
        self.show()
        

    def StudentLoginPage (self):
        self.inci=studentLogin.student_entry(self.db)
        self.inci.show()
        self.close()
    def teacherInfoExit(self):
            self.inci=teacherLogin.teacher_entry(self.db)
            self.inci.show()
            self.close()
        

    def TeacherLoginPage(self):
        self.inci=teacherLogin.teacher_entry(self.db)
        self.inci.show()
        self.close()
   