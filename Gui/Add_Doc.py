# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Add_Doc.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(466, 382)
        self.Comp = QtWidgets.QLineEdit(Form)
        self.Comp.setGeometry(QtCore.QRect(22, 110, 421, 22))
        self.Comp.setObjectName("Comp")
        self.Doc = QtWidgets.QLineEdit(Form)
        self.Doc.setGeometry(QtCore.QRect(20, 210, 421, 22))
        self.Doc.setObjectName("Doc")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 80, 411, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(20, 180, 411, 21))
        self.label_2.setObjectName("label_2")
        self.Submit = QtWidgets.QPushButton(Form)
        self.Submit.setGeometry(QtCore.QRect(320, 250, 121, 31))
        self.Submit.setObjectName("Submit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Please enter the serviced components\' ID."))
        self.label_2.setText(_translate("Form", "Please enter the documentation."))
        self.Submit.setText(_translate("Form", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
