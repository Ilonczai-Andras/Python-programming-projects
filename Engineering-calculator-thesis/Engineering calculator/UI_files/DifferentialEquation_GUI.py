# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\diff_egyenlet.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Egyenlet(object):
    def setupUi(self, Egyenlet):
        Egyenlet.setObjectName("Egyenlet")
        Egyenlet.resize(732, 509)
        Egyenlet.setStyleSheet(" QMainWindow {\n"
"            background-color: #2E2E2E;\n"
"        }")
        self.centralwidget = QtWidgets.QWidget(Egyenlet)
        self.centralwidget.setStyleSheet(" QWidget#centralwidget {\n"
"            background-color: #2E2E2E;\n"
"        }")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setMaximumSize(QtCore.QSize(16777215, 90))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("QLabel#label_3{\n"
"            color: #FFFFFF;\n"
"            font-size: 10pt;\n"
"            font-family: \'Courier New\', Courier, monospace;\n"
"            qproperty-alignment: \'AlignLeft;\n"
"        }")
        self.label_3.setObjectName("label_3")
        self.horizontalLayout.addWidget(self.label_3)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setMinimumSize(QtCore.QSize(0, 90))
        self.textEdit.setMaximumSize(QtCore.QSize(16777215, 90))
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("QTextEdit{\n"
"            color: #FFFFFF;\n"
"            background-color: #1C1C1C;\n"
"            font-family: \'Courier New\', Courier, monospace;\n"
"            font-size: 14pt;\n"
"        }")
        self.textEdit.setObjectName("textEdit")
        self.horizontalLayout.addWidget(self.textEdit)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setStyleSheet("QLineEdit {\n"
"            background-color: #1C1C1C;\n"
"            color: #FFFFFF;\n"
"            font-size: 10pt;\n"
"            font-family: \'Courier New\', Courier, monospace;\n"
"            border: 1px solid #555555;\n"
"            border-radius: 5px;\n"
"            padding: 5px;\n"
"        }")
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setStyleSheet("QPushButton {\n"
"            background-color: #1C1C1C;\n"
"            font-family: \'Courier New\', Courier, monospace;\n"
"            color: #FFFFFF;\n"
"            border: 1px solid #555555;\n"
"            border-radius: 10px;\n"
"            padding: 10px;\n"
"        }\n"
" QPushButton:hover {\n"
"            background-color: #5E5E5E;\n"
"        }\n"
"        QPushButton:pressed {\n"
"            background-color: #6E6E6E;\n"
"        }")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.horizontalLayout.setStretch(0, 3)
        self.horizontalLayout.setStretch(1, 2)
        self.horizontalLayout.setStretch(2, 2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Courier New")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("QLabel#label_2, QLabel#label_4{\n"
"            color: #FFFFFF;\n"
"            font-size: 14pt;\n"
"            font-family: \'Courier New\', Courier, monospace;\n"
"        }")
        self.label_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setStyleSheet("QLabel#label_2, QLabel#label_4{\n"
"            color: #FFFFFF;\n"
"            font-size: 14pt;\n"
"            font-family: \'Courier New\', Courier, monospace;\n"
"        }")
        self.label_4.setText("")
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_2.addWidget(self.label_4)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.canvaswidget = QtWidgets.QWidget(self.centralwidget)
        self.canvaswidget.setObjectName("canvaswidget")
        self.verticalLayout_3.addWidget(self.canvaswidget)
        self.verticalLayout_3.setStretch(0, 1)
        self.verticalLayout_3.setStretch(1, 1)
        self.verticalLayout_3.setStretch(2, 5)
        Egyenlet.setCentralWidget(self.centralwidget)

        self.retranslateUi(Egyenlet)
        QtCore.QMetaObject.connectSlotsByName(Egyenlet)

    def retranslateUi(self, Egyenlet):
        _translate = QtCore.QCoreApplication.translate
        Egyenlet.setWindowTitle(_translate("Egyenlet", "Egyenlet"))
        self.label_3.setText(_translate("Egyenlet", "Differential Equation"))
        self.lineEdit.setPlaceholderText(_translate("Egyenlet", "Initial value problem"))
        self.pushButton.setText(_translate("Egyenlet", "Enter"))
        self.label_2.setText(_translate("Egyenlet", "Result"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Egyenlet = QtWidgets.QMainWindow()
    ui = Ui_Egyenlet()
    ui.setupUi(Egyenlet)
    Egyenlet.show()
    sys.exit(app.exec_())
