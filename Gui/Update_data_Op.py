# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Update_data_Op.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Compstuff(object):
    def setupUi(self, Compstuff):
        Compstuff.setObjectName("Compstuff")
        Compstuff.resize(366, 384)
        Compstuff.setStyleSheet("")
        self.comboBox = QtWidgets.QComboBox(Compstuff)
        self.comboBox.setGeometry(QtCore.QRect(0, 50, 331, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.Elemstuff = QtWidgets.QComboBox(Compstuff)
        self.Elemstuff.setGeometry(QtCore.QRect(0, 120, 331, 22))
        self.Elemstuff.setObjectName("Elemstuff")
        self.Elemstuff.addItem("")
        self.Elemstuff.addItem("")
        self.Elemstuff.addItem("")
        self.Elemstuff.addItem("")
        self.Elemstuff.addItem("")
        self.Elemstuff.addItem("")
        self.Elemstuff.addItem("")
        self.Elemstuff.addItem("")
        self.Elemstuff.addItem("")
        self.Elemstuff.addItem("")
        self.Elemstuff.addItem("")
        self.Elemstuff.addItem("")
        self.infostuff = QtWidgets.QLineEdit(Compstuff)
        self.infostuff.setGeometry(QtCore.QRect(0, 210, 361, 101))
        self.infostuff.setObjectName("infostuff")
        self.label = QtWidgets.QLabel(Compstuff)
        self.label.setGeometry(QtCore.QRect(10, 180, 401, 16))
        self.label.setObjectName("label")
        self.submi = QtWidgets.QPushButton(Compstuff)
        self.submi.setGeometry(QtCore.QRect(270, 320, 93, 28))
        self.submi.setObjectName("submi")

        self.retranslateUi(Compstuff)
        QtCore.QMetaObject.connectSlotsByName(Compstuff)

    def retranslateUi(self, Compstuff):
        _translate = QtCore.QCoreApplication.translate
        Compstuff.setWindowTitle(_translate("Compstuff", "Form"))
        self.comboBox.setItemText(0, _translate("Compstuff", "Select Operation"))
        self.Elemstuff.setItemText(0, _translate("Compstuff", "Select Element"))
        self.Elemstuff.setItemText(1, _translate("Compstuff", "Inspection"))
        self.Elemstuff.setItemText(2, _translate("Compstuff", "Frequency"))
        self.Elemstuff.setItemText(3, _translate("Compstuff", "Hours"))
        self.Elemstuff.setItemText(4, _translate("Compstuff", "Months"))
        self.Elemstuff.setItemText(5, _translate("Compstuff", "HCW"))
        self.Elemstuff.setItemText(6, _translate("Compstuff", "DCW"))
        self.Elemstuff.setItemText(7, _translate("Compstuff", "C_Tach"))
        self.Elemstuff.setItemText(8, _translate("Compstuff", "NDH"))
        self.Elemstuff.setItemText(9, _translate("Compstuff", "NDD"))
        self.Elemstuff.setItemText(10, _translate("Compstuff", "T_rem"))
        self.Elemstuff.setItemText(11, _translate("Compstuff", "Note"))
        self.label.setText(_translate("Compstuff", "Please enter the updated info"))
        self.submi.setText(_translate("Compstuff", "Submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Compstuff = QtWidgets.QWidget()
    ui = Ui_Compstuff()
    ui.setupUi(Compstuff)
    Compstuff.show()
    sys.exit(app.exec_())
