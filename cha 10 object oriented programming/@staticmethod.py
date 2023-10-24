

class Employee:
    company = "Google"
    sagar = "Employee"

    def getsalary(self,signature):
        print(f"Salary for this employee workig in {self.Company} is {self.salary}/n{signature}")
    
    @staticmethod
    def greet():
        print("Good morning, sir")

    @staticmethod
    def time():
        print("The time is 6PM in morining") 

Sagar = Employee()

Sagar.salary = 100000
Sagar.greet()
Sagar.time()     