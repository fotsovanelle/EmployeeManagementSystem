import employee
import const

class TempEmployee(employee.Employee):

    def __init__(self, name, hourlySalary, number_of_hours_worked):
        super().__init__(name,const.category[0])
        self.hourlySalary = hourlySalary
        self.number_of_hours_worked = number_of_hours_worked

    def __str__(self):
        return ("\nname: ", self.name,
        "\nstatus : ", self.status,
        "\nhourly salary:  ", self.hourlySalary,
        "\nnumber of hours worked: ", self.number_of_hours_worked)
       