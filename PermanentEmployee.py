import employee
import const

class PermEmployee(employee.Employee):

    def __init__(self, name,number_of_days_worked,fixed_month_salary,number_of_children,marital_status,monthly_bonus ):
        super().__init__(name,const.category[0])
        self.number_of_days_worked = number_of_days_worked
        self.fixed_month_salary = fixed_month_salary
        self.number_of_children = number_of_children
        self.marital_status = marital_status
        self.monthly_bonus = monthly_bonus

    def __str__(self):
        return ("\nname : ", self.name,
        "\nstatus: ", self.status,
        "\nWorked days: ", self.number_of_days_worked,
        "\nfixed salary: ", self.fixed_month_salary,
        "\nnumber of children: ", self.number_of_children,
        "\nmarital status :", self.marital_status,
        "\nmonthly bonus: ",self.monthly_bonus,
         "\nsold volume: " , self.sold_volume,
        "\nPercentage commission: ", self.commission_percentage)    
            
    def __repr__(self) -> str:
        return f"{self.name}, {self.number_of_days_worked}"