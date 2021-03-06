from PyQt5 import QtWidgets,uic
import Login
import teacherInfo

class teacher_entry(QtWidgets.QMainWindow):
        def __init__(self,db):
            super(teacher_entry, self).__init__()
            uic.loadUi('ui/teacherLoginPage.ui', self)
            self.db=db
            self.backbutton2.clicked.connect(self.entry_show)
            self.teacherLoginButton.clicked.connect(self.teacherInfo_show)
        
        def entry_show(self):
            self.inci=Login.login(self.db)
            self.inci.show()
            self.close()
        def teacherInfo_show(self):
            tnumber=self.teacherName.text()
            tpassword=self.teacherPassword.text()
            if self.db.checkTeacher(tnumber,tpassword):
                self.inci=teacherInfo.teacherInfoScreen(self.db,tnumber)
                self.inci.show()
                self.close()
            else:
                self.tLoginPageLabel.setText("Wrong Password or Username")
                self.db.checkTeacher(tnumber,tpassword)
       