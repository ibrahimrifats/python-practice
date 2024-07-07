class SalaryNotInRange(Exception):
    """Exception raised when salary is not in range."""
    
    def __init__(self, salary, message="Salary must be between 5000 and 15000"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)

try:
    salary = int(input("Enter salary: "))
    
    if not (5000 < salary < 15000):
        raise SalaryNotInRange(salary)
    
except ValueError:
    print("Please enter a valid integer for salary.")
    
except SalaryNotInRange as e:
    print(e.message)
