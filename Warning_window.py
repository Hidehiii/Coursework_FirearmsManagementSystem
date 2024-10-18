# -*- coding: utf-8 -*-
import sys
# Form implementation generated from reading ui file 'Warning_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Account_Dialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(),self.height())
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(412, 291)
        self.text_lab = QtWidgets.QLabel(Dialog)
        self.text_lab.setGeometry(QtCore.QRect(-10, 100, 391, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text_lab.setFont(font)
        self.text_lab.setObjectName("text_lab")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Warn"))
        self.text_lab.setText(_translate("Dialog", "      The account already exists"))

class Signup_succeed(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(),self.height())
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(412, 291)
        self.text_lab = QtWidgets.QLabel(Dialog)
        self.text_lab.setGeometry(QtCore.QRect(-10, 100, 391, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text_lab.setFont(font)
        self.text_lab.setObjectName("text_lab")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Warn"))
        self.text_lab.setText(_translate("Dialog", "            Sign up succeed"))

class Error(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(),self.height())
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(412, 291)
        self.text_lab = QtWidgets.QLabel(Dialog)
        self.text_lab.setGeometry(QtCore.QRect(-10, 100, 391, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text_lab.setFont(font)
        self.text_lab.setObjectName("text_lab")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Warn"))
        self.text_lab.setText(_translate("Dialog", "                Error"))

class Add_weapon(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.width(),self.height())
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(412, 291)
        self.text_lab = QtWidgets.QLabel(Dialog)
        self.text_lab.setGeometry(QtCore.QRect(-10, 100, 391, 61))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text_lab.setFont(font)
        self.text_lab.setObjectName("text_lab")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Warn"))
        self.text_lab.setText(_translate("Dialog", "             Add succeed"))



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w1 = Account_Dialog()
    w2 = Signup_succeed()
    w3 = Error()
    w4 = Add_weapon()
    w4.show()
    w3.show()
    w2.show()
    w1.show()
    sys.exit(app.exec_())