class Employee:
    def __init__(self, employee_id, name, salary):
        self.employee_id = employee_id
        self.name = name
        self.salary = salary
        self.category = self.categorize()

    def categorize(self):
        if self.salary >= 70000:
            return "High Salary"
        elif self.salary >= 40000:
            return "Medium Salary"
        else:
            return "Low Salary"

    def display(self):
        print(f"Employee ID: {self.employee_id}")
        print(f"Name: {self.name}")
        print(f"Salary: ₹{self.salary}")
        print(f"Category: {self.category}")
        print("-" * 30)


class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)
        print("Employee added successfully!")

    def display_all(self):
        if not self.employees:
            print("No employees available.")
        else:
            print("\n===== Employee Information =====")
            for employee in self.employees:
                employee.display()


# Create Company object
company = Company()

# Add employees
employee1 = Employee(101, "Rahul", 85000)
employee2 = Employee(102, "Priya", 55000)
employee3 = Employee(103, "Amit", 30000)

company.add_employee(employee1)
company.add_employee(employee2)
company.add_employee(employee3)

# Display all employees
company.display_all()


# OUTPUT:
# Employee added successfully!
# Employee added successfully!
# Employee added successfully!
#
# ===== Employee Information =====
# Employee ID: 101
# Name: Rahul
# Salary: ₹85000
# Category: High Salary
# ------------------------------
# Employee ID: 102
# Name: Priya
# Salary: ₹55000
# Category: Medium Salary
# ------------------------------
# Employee ID: 103
# Name: Amit
# Salary: ₹30000
# Category: Low Salary
# ------------------------------