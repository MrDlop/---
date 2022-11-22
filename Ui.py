from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(554, 379)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.move(0, 0)
        self.pushButton.setCheckable(True)
        self.pushButton.setObjectName("pushButton")

        QtCore.QMetaObject.connectSlotsByName(MainWindow)
