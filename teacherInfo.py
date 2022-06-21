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
        self.lAddButton.clicked.connect(self.addLesson)
        self.lDeleteButton.clicked.connect(self.deleteLesson)
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
        ###
        print(self.teacherInf,"hello")
        lessons=[x[1] for x in self.teacherInf] 
        lessonNAME=self.lessonName.text()
        if lessonNAME in lessons:
            self.inci=Lesson.lesson(self.db,lessonNAME,self.tnumber)
            self.inci.show()
            self.close()
        else:
            self.lNameLabel_5.setText("This lesson is not yours.")
            
            
        ###
    def getTeacherInfo(self):
        cursor=self.db.connection.cursor()
        cursor.execute("""select teachers.first_name,subjects.subject_name from teachers
inner join teacher_subject on teacher_subject.teacher_id=teachers.teacher_id
inner join subjects on teacher_subject.subject_id=subjects.subject_id
where username='{}' """.format(self.tnumber)
            )
        self.teacherInf=cursor.fetchall()
        if len(self.teacherInf)==0:
            self.lNameLabel_3.setText("You dont have any lesson")
        else:
            self.tNameLabel_2.setText(self.teacherInf[0][0].upper())
            self.teacherLessons=""
            print(self.teacherInf)
            for i in range(len(self.teacherInf)):
                self.teacherLessons=self.teacherLessons+self.teacherInf[i][1]+"\n"
            self.lNameLabel_3.setText(self.teacherLessons)

    def addLesson(self):
    
          cursor=self.db.connection.cursor()
          cursor.execute("""select subject_name from subjects """.format(self.tnumber)
             )
          self.all_lessons=cursor.fetchall()
          lessons=[x[1] for x in self.teacherInf] 
          self.all_lessons=[x[0] for x in self.all_lessons] 
          lessonName=self.lAddorDeleteLine.text()
          subjectId=self.db.getSubjectId(lessonName)
          teacherId=self.db.getTeacherId(self.tnumber)
          if lessonName in lessons:
             self.error_.setText("This lesson already exist")
          elif (lessonName) in self.all_lessons:
             self.error_.setText(" ")
             self.db.connection.cursor().execute("""insert into teacher_subject (teacher_id,subject_id)
 values({},{})""".format(teacherId,subjectId) )
             self.db.connection.commit()
             
          else:
             self.error_.setText("This lesson does not exist on lessons")
          self.getTeacherInfo()

    def deleteLesson(self):
          lessonName=self.lAddorDeleteLine.text()
          subjectId=self.db.getSubjectId(lessonName)
          teacherId=self.db.getTeacherId(self.tnumber)
          lessons=[x[1] for x in self.teacherInf] 
          if lessonName not in lessons:
                 self.error_.setText("This lesson is not on the list")
          else:
             self.error_.setText(" ")
             self.db.connection.cursor().execute("""delete from teacher_subject where teacher_id={} and subject_id={}
 """.format(teacherId,subjectId) )
             self.db.connection.commit()
          self.getTeacherInfo()
         
    def get_lesson_update(self):
         cursor=self.db.connection.cursor()
         cursor.execute("""select subject_name from subjects """.format(self.tnumber)
            )
         self.all_lessons=cursor.fetchall()
         self.lessons=[x[1] for x in self.teacherInf] 
         
        
        
            
            
        

    




   