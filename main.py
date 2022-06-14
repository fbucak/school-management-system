from PyQt5 import QtWidgets
import sys
from DbConnect import DBConnection
import Login

app = QtWidgets.QApplication(sys.argv)
db=DBConnection()
window = Login.login(db)
app.exec_()