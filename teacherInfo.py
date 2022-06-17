from PyQt5 import QtWidgets,uic,QtGui
import studentLogin
import teacherLogin
from PyQt5.QtWidgets import QPushButton
import Lesson

lessons=["Matematik","Fizik","Kimya"]
class teacherInfoScreen(QtWidgets.QMainWindow):
    
    def __init__(self,db,tnumber):
        super(teacherInfoScreen, self).__init__()
        uic.loadUi('ui/teacherInfo.ui', self)
        self.db=db
        self.tnumber=tnumber
        self.teacherExit.clicked.connect(self.teacherInfoExit)
        self.showButton.clicked.connect(self.goToLessonPage)
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
    def goToLessonPage(self):
        self.inci=Lesson.lesson(self.db,self.lessonName.text())
        self.inci.show()
        self.close()
   