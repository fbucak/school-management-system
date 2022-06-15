from PyQt5 import QtWidgets,uic,QtGui
import studentLogin
import teacherLogin
from PyQt5.QtWidgets import QPushButton

class lesson(QtWidgets.QMainWindow):
     def __init__(self,db,lessonName):
         super(lesson, self).__init__()
         uic.loadUi('ui/LessonPage.ui', self)
         self.db=db
         self.lessonName=lessonName
         self.sAddButton.clicked.connect(self.addStudent)
         self.sDeleteButton.clicked.connect(self.deleteStudent)
         self.lessonTitle.setText(lessonName)
         self.show()

     def addStudent(self):
         
         number=self.sNoLine.text()
         subjectId=self.subjectIdLine.text()
         try:
            self.db.connection.cursor().execute("""insert into student_subject (student_id,subject_id)
values({},{})""".format(number,subjectId) )
            self.db.connection.commit()
            
         except:
            print("Please check your subject id or student number")
     def deleteStudent(self):
         number=self.sNoLine.text()
         subjectId=self.subjectIdLine.text()
         try:
            self.db.connection.cursor().execute("""delete from student_subject where student_id={} and subject_id={}""".format(number,subjectId))
            print("hi")
            self.db.connection.commit()
         except:
            print("Please check your subject id or student number")
     def addGrade(self) :
        number=self.gStudentId.text()
        


         