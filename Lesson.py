from PyQt5 import QtWidgets,uic,QtGui
import studentLogin
import teacherLogin
from PyQt5.QtWidgets import QPushButton
import teacherInfo

class lesson(QtWidgets.QMainWindow):
     def __init__(self,db,lessonName,tnumber):
         super(lesson, self).__init__()
         uic.loadUi('ui/LessonPage.ui', self)
         self.db=db
         self.lessonName=lessonName
         self.tnumber=tnumber
         self.sAddButton.clicked.connect(self.addStudent)
         self.sDeleteButton.clicked.connect(self.deleteStudent)
         self.lessonTitle.setText(lessonName)
         self.LessonBackButton.clicked.connect(self.backTeacherInfo)
         self.sListButton.clicked.connect(self.getStudentList)
         self.addGradeButton.clicked.connect(self.addGrade)
         self.deleteGradeButton.clicked.connect(self.deleteGrade)
         
         self.show()
     def backTeacherInfo(self):
         self.inci=teacherInfo.teacherInfoScreen(self.db,self.tnumber)
         self.inci.show()
         self.close()

     def addStudent(self):
         
         number=self.sNoLine.text()
         subjectId=self.db.getSubjectId(self.lessonName)
         studentId=self.db.getStudentId(number)
   
         try:
            self.db.connection.cursor().execute("""insert into student_subject (student_id,subject_id)
values({},{})""".format(studentId,subjectId) )
            self.db.connection.commit()
            
         except:
            print("Please check your subject id or student number")
     def deleteStudent(self):
         number=self.sNoLine.text()
         subjectId=self.db.getSubjectId(self.lessonName)
         studentId=self.db.getStudentId(number)
         try:
            self.db.connection.cursor().execute("""delete from student_subject where student_id={} and subject_id={}""".format(studentId,subjectId))

            self.db.connection.commit()
         except:
            print("Please check your subject id or student number")
     def addGrade(self) :
        number=self.gStudentId.text()
        subjectId=self.db.getSubjectId(self.lessonName)
        studentId=self.db.getStudentId(number)
        grade=self.sAddorDeleteLine.text()
        try:
            self.db.connection.cursor().execute("""insert into grades (subject_id,student_id,grade)
values({},{},{})""".format(subjectId,studentId,grade) )
            self.db.connection.commit()
            
        except:
            print("Please check your subject id or student number")
     def deleteGrade(self):
        number=self.gStudentId.text()
        subjectId=self.db.getSubjectId(self.lessonName)
        studentId=self.db.getStudentId(number)
        try:
            self.db.connection.cursor().execute("""delete from grades where subject_id={} and student_id={}
""".format(subjectId,studentId) )
            self.db.connection.commit()
            
        except:
            print("Please check your subject id or student number")

     def getStudentList(self):
        cursor=self.db.connection.cursor()
        cursor.execute("""select students.students_no,students.first_name,students.last_name,subjects.subject_name, grades.grade from grades
full join students on students.student_id=grades.student_id
inner join student_subject on student_subject.student_id=students.student_id
inner join subjects on subjects.subject_id=student_subject.subject_id
inner join teacher_subject on teacher_subject.subject_id=subjects.subject_id
inner join teachers on teachers.teacher_id=teacher_subject.teacher_id
where username='{}' and subjects.subject_name='{}'""".format(self.tnumber,self.lessonName))
        self.studentList=cursor.fetchall()
        print("studentList uzunlugu"+str(len(self.studentList)))
        row=0
        self.tableWidget_Student.setRowCount(len(self.studentList))
        self.tableWidget_Student.setColumnCount(5)
        print(self.studentList)
        for s in self.studentList:
                print(self.studentList[row])
                self.tableWidget_Student.setItem(row,0,QtWidgets.QTableWidgetItem(str(self.studentList[row][0])))
                self.tableWidget_Student.setItem(row,1,QtWidgets.QTableWidgetItem(self.studentList[row][1]))
                self.tableWidget_Student.setItem(row,2,QtWidgets.QTableWidgetItem(self.studentList[row][2]))
                self.tableWidget_Student.setItem(row,3,QtWidgets.QTableWidgetItem(self.studentList[row][3]))
                self.tableWidget_Student.setItem(row,4,QtWidgets.QTableWidgetItem(str(self.studentList[row][4])))
                row=row+1
        


         