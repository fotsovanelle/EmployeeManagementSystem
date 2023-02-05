import sys
import const
from PermanentEmployee import PermEmployee
from staff import Staff
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication

class PermanentEmployeeForm(QDialog):
    staff = Staff()
    def __init__(self):
        super(PermanentEmployeeForm,self).__init__()
        loadUi("PerForm.ui",self)

        self.MonthBonus.setText("0")
        if not self.Marital_status.isChecked():
            self.Num_children.setVisible(False)
            self.MonthBonus.setVisible(False)
        
        #the buttons
        self.HireEmployee.clicked.connect(self.HireEmployeePressed)
        self.UpdateEmployee.clicked.connect(self.UpdateEmployeePressed)    
        self.Marital_status.clicked.connect(self.MaritalStatusPressed)
        self.DismissEmployee.clicked.connect(self.dismiss_employee) 
        self.MuteEmployee.clicked.connect(self.mute_EmployeePressed)

    def MaritalStatusPressed(self):
        if not self.Marital_status.isChecked():
            self.Num_children.setVisible(False)
            self.MonthBonus.setVisible(False)
        else:
            self.Num_children.setVisible(True)
            self.MonthBonus.setVisible(True)    

    def HireEmployeePressed(self):
        employee = PermEmployee(str(self.Name.toPlainText()),str(self.DaysWorked.value()),str(self.Monthly_salary.toPlainText()),str(self.Num_children.value()),
        str(self.Marital_status.isChecked()),str(self.MonthBonus.toPlainText()))
        self.staff.insert_permanent_employee(employee)

        self.Name.setText("")
        self.DaysWorked.setValue(0)
        self.Marital_status.setChecked(False)
        self.Monthly_salary.setText("")
        self.Num_children.setValue(0)
        self.MonthBonus.setText("0")
  

    def UpdateEmployeePressed(self):
        employee = PermEmployee(str(self.Name.toPlainText()),str(self.DaysWorked.value()),str(self.Monthly_salary.toPlainText()),str(self.Num_children.value()),
        str(self.Marital_status.isChecked()),str(self.MonthBonus.toPlainText()))
        self.staff.update_permanent_employee(employee)

        self.Name.setText("")
        self.DaysWorked.setValue(0)
        self.Marital_status.setChecked(False)
        self.Monthly_salary.setText("")
        self.Num_children.setValue(0)
        self.MonthBonus.setText("0")         


    def dismiss_employee(self):
         employee = PermEmployee(str(self.Name.toPlainText()),str(0),str(0),str(0),str(0),str(0))
         self.staff.delete_permanent_employee(employee)        

         self.Name.setText("")
         self.DaysWorked.setValue(0)
         self.Marital_status.setChecked(False)
         self.Monthly_salary.setText("")
         self.Num_children.setValue(0)
         self.MonthBonus.setText("0")

    def mute_EmployeePressed(self):
        employee = PermEmployee(str(self.Name.toPlainText()),str(self.DaysWorked.value()),str(self.Monthly_salary.toPlainText()),str(self.Num_children.value()),
        str(self.Marital_status.isChecked()),str(self.MonthBonus.toPlainText()))
        self.staff.mute_permanent_employee(employee) 

        self.Name.setText("")
        self.DaysWorked.setValue(0)
        self.Marital_status.setChecked(False)
        self.Monthly_salary.setText("")
        self.Num_children.setValue(0)
        self.MonthBonus.setText("0")