from PyQt5 import QtWidgets,uic
import Login
import studentInfo
class student_entry(QtWidgets.QMainWindow):
        def __init__(self,db):
            super(student_entry, self).__init__()
            uic.loadUi('ui/studentLoginPage.ui', self)
            self.db=db
            self.backbutton.clicked.connect(self.entry_show)
            self.studentLoginButton.clicked.connect(self.studentCheck)
            
            
        
        def entry_show(self):
            self.inci=Login.login(self.db)
            self.inci.show()
            self.close()
            
        def studentCheck(self):
            number=self.studentNumber.text()
            password=self.studentPassword.text()
            if self.db.checkStudent(number,password):
                self.inci=studentInfo.studentInfoScreen(self.db,number)
                self.inci.show()
                self.close()
            else:
                self.sLoginPageLabel.setText("Wrong Password or Student Number")
                self.db.checkStudent(number,password)



            


            
