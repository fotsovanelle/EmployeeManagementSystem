import sys
import const
from temporalEmployee import TempEmployee
from staff import Staff
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog,QApplication


class TemporalEmployeeForm(QDialog):
    staff = Staff()
    def __init__(self):
        super(TemporalEmployeeForm,self).__init__()
        loadUi("TemForm.ui",self)

        self.HireEmployee.clicked.connect(self.HireEmployeePressed)
        self.UpdateEmployee.clicked.connect(self.UpdateEmployeePressed)
        self.DismissEmployee.clicked.connect(self.dismiss_employee)
        self.MuteEmployee.clicked.connect(self.mute_EmployeePressed)

    def HireEmployeePressed(self):
        employee = TempEmployee(str(self.Name.toPlainText()),str(self.HourlyPay.toPlainText()),str(self.Hours_worked.value()))
        self.staff.insert_temporal_employee(employee) 

        self.Name.setText("")
        self.Hours_worked.setValue(0)
        self.HourlyPay.setText("")



    def UpdateEmployeePressed(self):
        employee = TempEmployee(str(self.Name.toPlainText()),str(self.HourlyPay.toPlainText()),str(self.Hours_worked.value()))
        self.staff.insert_temporal_employee(employee)
        self.staff.update_temporal_employee(employee)

        self.Name.setText("")
        self.Hours_worked.setValue(0)
        self.HourlyPay.setText("")     

    def dismiss_employee(self):
        employee =TempEmployee(str(self.Name.toPlainText()),str(0),str(0))
        self.staff.delete_temporal__employee(employee)  

        self.Name.setText("")
        self.Hours_worked.setValue(0)
        self.HourlyPay.setText("")  


    def mute_EmployeePressed(self):
        employee = TempEmployee(str(self.Name.toPlainText()),str(self.HourlyPay.toPlainText()),str(self.Hours_worked.value()))
        self.staff.mute_temporal_employee(employee) 

        self.Name.setText("")
        self.Hours_worked.setValue(0)
        self.HourlyPay.setText("") 