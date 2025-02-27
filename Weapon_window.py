# -*- coding: utf-8 -*-
import sys
# Form implementation generated from reading ui file 'Weapon_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import Change_but
import Delete_but

class Weapon_win(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(813, 421)
        self.Change_but = Change_but.Change_button(self)
        self.Change_but.setGeometry(QtCore.QRect(650, 30, 60, 30))
        self.Change_but.setStyleSheet("Background-color:white")
        self.Change_but.setText("Change")
        self.Delete_but = Delete_but.Delete_button(self)
        self.Delete_but.setGeometry(QtCore.QRect(720, 30, 60, 30))
        self.Delete_but.setStyleSheet("Background-color:white")
        self.Delete_but.setText("Delete")
        self.pic = QtWidgets.QLabel(Form)
        self.pic.setGeometry(QtCore.QRect(10, 100, 211, 141))
        self.pic.setStyleSheet("\n"
"background-color: rgb(255, 255, 255);")
        self.pic.setText("")
        self.pic.setScaledContents(True)
        self.pic.setObjectName("pic")
        self.Damage = QtWidgets.QLabel(Form)
        self.Damage.setGeometry(QtCore.QRect(230, 30, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Damage.setFont(font)
        self.Damage.setObjectName("Damage")
        self.FiringMode = QtWidgets.QLabel(Form)
        self.FiringMode.setGeometry(QtCore.QRect(230, 90, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.FiringMode.setFont(font)
        self.FiringMode.setObjectName("FiringMode")
        self.Magazine_capacity = QtWidgets.QLabel(Form)
        self.Magazine_capacity.setGeometry(QtCore.QRect(230, 140, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Magazine_capacity.setFont(font)
        self.Magazine_capacity.setObjectName("Magazine_capacity")
        self.magazines = QtWidgets.QLabel(Form)
        self.magazines.setGeometry(QtCore.QRect(230, 200, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.magazines.setFont(font)
        self.magazines.setObjectName("magazines")
        self.Bullets_remaining = QtWidgets.QLabel(Form)
        self.Bullets_remaining.setGeometry(QtCore.QRect(230, 270, 351, 51))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.Bullets_remaining.setFont(font)
        self.Bullets_remaining.setObjectName("Bullets_remaining")

        self.retranslateUi(Form)
        self.Change_but.clicked.connect(self.close_all)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Damage.setText(_translate("Form", "Damage"))
        self.FiringMode.setText(_translate("Form", "FiringMode"))
        self.Magazine_capacity.setText(_translate("Form", "Magazine_capacity"))
        self.magazines.setText(_translate("Form", "Magazines"))
        self.Bullets_remaining.setText(_translate("Form", "Bullets_remaining"))

    def close_all(self):
        self.parent().parent().parent().parent().close()

    def set_Damage(self,Damage : int):
        self.Damage.setText("Damage:" + str(Damage))
    def set_FiringMode(self,FiringMode : str):
        self.FiringMode.setText("FiringMode:" + FiringMode)
    def set_Magazine_capacity(self,capacity : int):
        self.Magazine_capacity.setText("Magazine_capacity:" + str(capacity))
    def set_magazines(self,magazines : int):
        self.magazines.setText("magazines:" + str(magazines))
    def set_Bullets_remaining(self,Bullets_remaining : int):
        self.Bullets_remaining.setText("Bullets_remaining:" + str(Bullets_remaining))
    def set_pic(self,path : str):
        self.pic.setPixmap(QtGui.QPixmap(path))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = Weapon_win()
    window.show()
    sys.exit(app.exec_())