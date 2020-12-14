# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'columnSectionControl.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

# User Interface File

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setEnabled(True)
        Form.resize(904, 562)
        Form.setCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 881, 551))
        self.groupBox.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(10, 20, 181, 24))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.column_number = QtWidgets.QLineEdit(self.widget)
        self.column_number.setObjectName("column_number")
        self.horizontalLayout.addWidget(self.column_number)
        self.control_button = QtWidgets.QPushButton(self.groupBox)
        self.control_button.setGeometry(QtCore.QRect(10, 50, 93, 28))
        self.control_button.setObjectName("control_button")
        self.groupBox_2 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_2.setGeometry(QtCore.QRect(210, 20, 151, 521))
        self.groupBox_2.setObjectName("groupBox_2")
        self.columns_name_list = QtWidgets.QListWidget(self.groupBox_2)
        self.columns_name_list.setGeometry(QtCore.QRect(10, 20, 131, 481))
        self.columns_name_list.setObjectName("columns_name_list")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(380, 20, 151, 521))
        self.groupBox_3.setObjectName("groupBox_3")
        self.axial_load_list = QtWidgets.QListWidget(self.groupBox_3)
        self.axial_load_list.setGeometry(QtCore.QRect(10, 20, 131, 481))
        self.axial_load_list.setObjectName("axial_load_list")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(710, 20, 151, 521))
        self.groupBox_4.setObjectName("groupBox_4")
        self.check_list = QtWidgets.QListWidget(self.groupBox_4)
        self.check_list.setGeometry(QtCore.QRect(10, 20, 131, 481))
        self.check_list.setObjectName("check_list")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(20, 120, 121, 41))
        self.label_2.setObjectName("label_2")
        self.groupBox_5 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_5.setGeometry(QtCore.QRect(540, 20, 151, 521))
        self.groupBox_5.setObjectName("groupBox_5")
        self.capacity_list = QtWidgets.QListWidget(self.groupBox_5)
        self.capacity_list.setGeometry(QtCore.QRect(10, 20, 131, 481))
        self.capacity_list.setObjectName("capacity_list")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(20, 100, 151, 16))
        self.label_3.setObjectName("label_3")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.groupBox.setTitle(_translate("Form", "Info"))
        self.label.setText(_translate("Form", "1. Kat Kolon Adedi"))
        self.control_button.setText(_translate("Form", "Kontrol"))
        self.groupBox_2.setTitle(_translate("Form", "Kolonlar"))
        self.groupBox_3.setTitle(_translate("Form", "Eksenel Yük (kN)"))
        self.groupBox_4.setTitle(_translate("Form", "Sonuç"))
        self.label_2.setText(_translate("Form", "N <= 0.9*Ac*fcd"))
        self.groupBox_5.setTitle(_translate("Form", "Kapasite (kN)"))
        self.label_3.setText(_translate("Form", "TS500 2000 Denk. 7.7"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

