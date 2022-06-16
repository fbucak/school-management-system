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
        self.getTeacherInfo()
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
    def getTeacherInfo(self):
        cursor=self.db.connection.cursor()
        cursor.execute("""select teachers.first_name,subjects.subject_name from teachers
inner join teacher_subject on teacher_subject.teacher_id=teachers.teacher_id
inner join subjects on teacher_subject.subject_id=subjects.subject_id
where username='{}' """.format(self.tnumber)
            )
        self.teacherInf=cursor.fetchall()
        self.tNameLabel_2.setText(self.teacherInf[0][0])
        self.teacherLessons=""
        for i in range(len(self.teacherInf)):
            self.teacherLessons=self.teacherLessons+self.teacherInf[i][1]
        self.lNameLabel_3.setText(self.teacherLessons)



   