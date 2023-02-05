import sys
import const


from PerForm import PermanentEmployeeForm
from TemForm import TemporalEmployeeForm
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow,QApplication,QDialog
import sqlite3


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        loadUi("MainWindow.ui",self)

        self.loadDataToTables()

        self.TemporealEmployee.clicked.connect(self.actionHire_Temporal_EmployeePressed)
        self.PermanenEmployee.clicked.connect(self.actionHire_Permanent_EmployeePressed)
    
    def actionHire_Temporal_EmployeePressed(self):
         window = TemporalEmployeeForm()
         window.setModal(True)
         window.exec() 
         self.loadDataToTables()
             
    def actionHire_Permanent_EmployeePressed(self):
        window = PermanentEmployeeForm()
        window.setModal(True)
        window.exec() 
        self.loadDataToTables()

    def loadDataToTables(self):
        self.PermTable.clearContents()
        self.TemTable.clearContents()
        connection = sqlite3.connect("staff.db")
        cur = connection.cursor()
        sqlquery1 = ("select * from perEmployee limit 50")
        sqlquery2 = ("select * from temEmployee limit 50")
        

        self.PermTable.setRowCount(50)
        self.TemTable.setRowCount(50)
        tableRow = 0
        tableRowt1 = 0

        for row in cur.execute(sqlquery1):
            self.PermTable.setItem(tableRow,0,QtWidgets.QTableWidgetItem(row[0]))
            self.PermTable.setItem(tableRow,1,QtWidgets.QTableWidgetItem(row[1]))
            self.PermTable.setItem(tableRow,2,QtWidgets.QTableWidgetItem(row[2]))
            self.PermTable.setItem(tableRow,3,QtWidgets.QTableWidgetItem(row[3]))
            self.PermTable.setItem(tableRow,4,QtWidgets.QTableWidgetItem(row[4]))
            self.PermTable.setItem(tableRow,5,QtWidgets.QTableWidgetItem(row[5]))
            
            tableRow +=1

        for row in cur.execute(sqlquery2):
            self.TemTable.setItem(tableRowt1,0,QtWidgets.QTableWidgetItem(row[0]))
            self.TemTable.setItem(tableRowt1,1,QtWidgets.QTableWidgetItem(row[1]))
            self.TemTable.setItem(tableRowt1,2,QtWidgets.QTableWidgetItem(row[2]))
            
            tableRowt1 +=1    
