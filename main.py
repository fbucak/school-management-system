from PyQt5 import QtWidgets
import sys
import windowOne



app = QtWidgets.QApplication(sys.argv)
window = windowOne.login()
app.exec_()