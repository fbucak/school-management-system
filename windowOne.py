from PyQt5 import QtWidgets,uic
import student
import teacher


class login(QtWidgets.QMainWindow):
    
    def __init__(self):
        super(login, self).__init__()
        uic.loadUi('ui/loginpage.ui', self)
        self.forStudent.clicked.connect(self.StudentLoginPage)
        self.forTeacher.clicked.connect(self.TeacherLoginPage)
        self.show()

    def StudentLoginPage (self):
        self.inci=student.student_entry()
        self.inci.show()
        self.close()
        #self.tabWidget.setCurrentIndex(5)
        

    def TeacherLoginPage(self):
        self.inci=teacher.teacher_entry()
        self.inci.show()
        self.close()
        #self.tabWidget.setCurrentIndex(3)
        