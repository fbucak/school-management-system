from PyQt5 import QtWidgets,uic
import studentLogin
import teacherLogin
from DbConnect import DBConnection
from PyQt5.QtGui import QPixmap


class login(QtWidgets.QMainWindow):
    
    def __init__(self,db):
        super(login, self).__init__()
        uic.loadUi('ui/loginpage.ui', self)
        qpixmap = QPixmap('untitled-10.png')
        self.logo.setPixmap(qpixmap)
        self.db=db
        self.forStudent.clicked.connect(self.StudentLoginPage)
        self.forTeacher.clicked.connect(self.TeacherLoginPage)
        self.show()

    def StudentLoginPage (self):
        self.inci=studentLogin.student_entry(self.db)
        self.inci.show()
        self.close()
        

    def TeacherLoginPage(self):
        self.inci=teacherLogin.teacher_entry(self.db)
        self.inci.show()
        self.close()
        
        