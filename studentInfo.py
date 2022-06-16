from turtle import shape
from PyQt5 import QtWidgets,uic
import studentLogin

class studentInfoScreen(QtWidgets.QMainWindow):
    def __init__(self,db,number):
        super(studentInfoScreen, self).__init__()
        self.db=db
        self.number=number
        uic.loadUi('ui/studentInfo.ui', self)
        self.getStudentInfo()
        self.getGrades()
        self.studentExit.clicked.connect(self.studentInfoExit)
        
        self.show()

    def studentInfoExit(self):
            self.inci=studentLogin.student_entry(self.db)
            self.inci.show()
            self.close()
    def getStudentInfo(self):
            cursor=self.db.connection.cursor()
            cursor.execute("""
            select students_no,concat(first_name,' ',last_name) from students where students_no={} """.format(self.number),
            )
            self.student=cursor.fetchall()
            self.sNameLabel_2.setText(str(self.student[0][1]))
            self.sNoLabel.setText(str(self.student[0][0]))
    def getGrades(self):
            cursor=self.db.connection.cursor()
            cursor.execute("""select subjects.subject_name,grades.grade from subjects
inner join grades on subjects.subject_id=grades.subject_id
inner join students on students.student_id=grades.student_id
where students_no={} """.format(self.number),
            )
            self.student=cursor.fetchall()
            print(self.student)
            row=0
            self.tableWidget_2.setRowCount(len(self.student))
            self.tableWidget_2.setColumnCount(2)
            for s in self.student:
                self.tableWidget_2.setItem(row,0,QtWidgets.QTableWidgetItem(self.student[row][0]))
                self.tableWidget_2.setItem(row,1,QtWidgets.QTableWidgetItem(str(self.student[row][1])))
                row=row+1

    

    