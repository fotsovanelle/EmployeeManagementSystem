import sqlite3
from PermanentEmployee import PermEmployee
from temporalEmployee import TempEmployee

class Staff:
    conn = sqlite3.connect('staff.db')
    c = conn.cursor()
    def __init__(self) -> None:
        self.conn
    def insert_permanent_employee(self,employee:PermEmployee):
        self.c.execute("insert into perEmployee values(?,?,?,?,?,?)",(employee.name,employee.number_of_days_worked,employee.fixed_month_salary,employee.number_of_children,employee.marital_status,employee.monthly_bonus))
        self.conn.commit()
    def insert_temporal_employee(self,employee:TempEmployee):
        self.c.execute("insert into temEmployee values(?,?,?)",(employee.name,employee.hourlySalary,str(employee.number_of_hours_worked)))
        self.conn.commit()    
    def update_temporal_employee(self,employee:TempEmployee):
        with self.conn:
            self.c.execute("""update temEmployee set hourlySalary = :hourlySalary, number_of_hours_worked = :number_of_hours_worked
            where name = :name""",{'name': employee.name, 'hourlySalary': employee.hourlySalary, 'number_of_hours_worked': str(employee.number_of_hours_worked)})
    def update_permanent_employee(self,employee:PermEmployee):
        with self.conn:
            self.c.execute("""update perEmployee set number_of_days_worked = :number_of_days_worked,fixed_month_salary = :fixed_month_salary,number_of_children = :number_of_children,marital_status = :marital_status,monthly_bonus = :monthly_bonus
            where name = :name""",{'name': employee.name, 'number_of_days_worked': employee.number_of_days_worked, 'fixed_month_salary': str(employee.fixed_month_salary), 'number_of_children': employee.number_of_children,'marital_status':employee.marital_status,'monthly_bonus':employee.monthly_bonus,})
    
    def delete_permanent_employee(self,employee:PermEmployee):
        with self.conn:
            self.c.execute("""delete from perEmployee 
            where name = :name""",{'name': employee.name})
    def delete_temporal__employee(self,employee:TempEmployee):
        with self.conn:
            self.c.execute("""delete from  temEmployee
            where name = :name """,{'name': employee.name})

    def mute_permanent_employee(self,employee:PermEmployee):
        accumilator = int(employee.number_of_days_worked)*(float(employee.monthly_bonus)+ float(employee.fixed_month_salary))/20
        hourly_pay = 1500
        numhours_worked = accumilator/hourly_pay
        tempEmplo = TempEmployee(employee.name,str(hourly_pay),str(numhours_worked))
        
        self.insert_temporal_employee(tempEmplo)
        self.delete_permanent_employee(employee)

    def mute_temporal_employee(self,employee:TempEmployee):
        MS = float(employee.hourlySalary)*int(employee.number_of_hours_worked) 
        WDS = int(employee.number_of_hours_worked)/8
        pemEmplo = PermEmployee(employee.name,str(WDS),str(MS),str(0),str("False"),str(0))

        self.insert_permanent_employee(pemEmplo)
        self.delete_temporal__employee(employee)         
        