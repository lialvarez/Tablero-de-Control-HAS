# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModal)
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_en_proceso = QtWidgets.QWidget()
        self.tab_en_proceso.setObjectName("tab_en_proceso")
        self.frame = QtWidgets.QFrame(self.tab_en_proceso)
        self.frame.setGeometry(QtCore.QRect(10, 10, 761, 321))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_add = QtWidgets.QPushButton(self.frame)
        self.pushButton_add.setObjectName("pushButton_add")
        self.gridLayout.addWidget(self.pushButton_add, 1, 0, 1, 1)
        self.pushButton_remove = QtWidgets.QPushButton(self.frame)
        self.pushButton_remove.setObjectName("pushButton_remove")
        self.gridLayout.addWidget(self.pushButton_remove, 1, 1, 1, 1)
        self.my_table = QtWidgets.QTableWidget(self.frame)
        self.my_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.my_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.my_table.setObjectName("my_table")
        self.my_table.setColumnCount(5)
        self.my_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.my_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.my_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.my_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.my_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.my_table.setHorizontalHeaderItem(4, item)
        self.gridLayout.addWidget(self.my_table, 0, 0, 1, 2)
        self.tabWidget.addTab(self.tab_en_proceso, "")
        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_add.setText(_translate("MainWindow", "Añadir"))
        self.pushButton_remove.setText(_translate("MainWindow", "Eliminar"))
        item = self.my_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Nro. Caja"))
        item = self.my_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Peso [g]"))
        item = self.my_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Hora Ingreso"))
        item = self.my_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Llenado"))
        item = self.my_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Tapado"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_en_proceso), _translate("MainWindow", "Unidades En Proceso"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

