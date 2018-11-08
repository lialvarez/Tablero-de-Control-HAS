from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtCore import pyqtSlot
import sys
import design
from Box import Box, BoxManager
import datetime
from time import sleep


class TableroHAS(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self, boxMngr, parent=None):
        super(TableroHAS, self).__init__(parent)
        self.setupUi(self)
        self.my_table.setFocusPolicy(QtCore.Qt.NoFocus)  
        self.boxMngr = BoxManager()
        self.boxMngr = boxMngr
        self.boxMngr.inboundBox.connect(self.add_box)
        self.pushButton_remove.clicked.connect(self.remove_row)

    def append_row(self, boxList):
        columnCount = self.my_table.columnCount()
        rowCount = self.my_table.rowCount()
        box = Box(None, None)
        box = boxList.pop()
        data = [box.code, box.peso, box.t_ingreso, box.llenada, box.tapada]
        
        if len(data) > 0:
            self.my_table.setRowCount(rowCount + 1)
            for i in range(columnCount):
                #Codigo que agrega elementos a la tabla
                if i >= 3:
                    # Codigo que agrega el CheckBox
                    chkBoxItem = QtWidgets.QTableWidgetItem()
                    chkBoxItem.setFlags(QtCore.Qt.ItemIsEnabled)
                    if data[i] == True:
                        chkBoxItem.setCheckState(QtCore.Qt.Checked)
                    else:
                        chkBoxItem.setCheckState(QtCore.Qt.Unchecked)
                    self.my_table.setItem(rowCount, i, chkBoxItem)
                else:
                    self.my_table.setItem(rowCount,i, QtWidgets.QTableWidgetItem(str(data[i])))


    def remove_row(self):
        rowCount = self.my_table.rowCount()
        if rowCount > 0:
            self.my_table.removeRow(0)

    @pyqtSlot(list)
    def add_box(self, l):
        ''' Agregar caja a la intefaz '''
        print('Caja agregada')
        self.append_row(l)

def main():

    boxMngr = BoxManager()
    app = QtWidgets.QApplication(sys.argv)
    form = TableroHAS(boxMngr)
    form.show() 
    timer = QtCore.QTimer()
    timer.timeout.connect(boxMngr.crearCaja)
    timer.start(1000)
    app.exec_()

if __name__ == '__main__':
    main()