# Form implementation generated from reading ui file 'qt6/main.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(326, 141)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.inputBt = QtWidgets.QPushButton(parent=self.centralwidget)
        self.inputBt.setObjectName("inputBt")
        self.gridLayout.addWidget(self.inputBt, 0, 0, 1, 1)
        self.inputPath = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.inputPath.setObjectName("inputPath")
        self.gridLayout.addWidget(self.inputPath, 0, 1, 1, 1)
        self.outputBt = QtWidgets.QPushButton(parent=self.centralwidget)
        self.outputBt.setObjectName("outputBt")
        self.gridLayout.addWidget(self.outputBt, 1, 0, 1, 1)
        self.outputPath = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.outputPath.setObjectName("outputPath")
        self.gridLayout.addWidget(self.outputPath, 1, 1, 1, 1)
        self.trimBt = QtWidgets.QPushButton(parent=self.centralwidget)
        self.trimBt.setObjectName("trimBt")
        self.gridLayout.addWidget(self.trimBt, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 326, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.inputBt.setText(_translate("MainWindow", "Input folder"))
        self.outputBt.setText(_translate("MainWindow", "Output folder"))
        self.trimBt.setText(_translate("MainWindow", "Trim"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())