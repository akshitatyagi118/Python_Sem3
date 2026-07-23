# Decorator to add a report header
def report_header(func):
	def wrapper(*args, **kwargs):
		# wrapper() is an inner function. *args and **kwargs allow it to accept any number of
		# positional and keyword arguments.
		print("=" * 40)
		print(" STUDENT REPORT")
		print("=" * 40)
		result = func(*args, **kwargs)
		print("=" * 40)
		return result

	return wrapper

class Report:
	college = "MIT ADT Engineering College"

	# Constructor (Magic Method)
	def __init__(self, name, roll, marks):
		self.name = name
		self.roll = roll
		self.marks = marks

	# Class Method
	@classmethod
	def change_college(cls, new_name):
		cls.college = new_name

	# Magic Method
	def __str__(self):
		return f"Name : {self.name}\nRoll No : {self.roll}\nMarks : {self.marks}"

	# Decorator applied to display report
	@report_header
	def display_report(self):
		print(f"College : {Report.college}")
		print(self)
		if self.marks >= 40:
			print("Result : PASS")
		else:
			print("Result : FAIL")

# Main Program
student1 = Report("Akshita", 1596, 95)
student1.display_report()

print()

# Change college name using class method
Report.change_college("IIT Bombay")

student2 = Report("Soham", 1335, 35)
student2.display_report()

'''
OUTPUT:

========================================
 STUDENT REPORT
========================================
College : MIT ADT Engineering College
Name : Akshita
Roll No : 1596
Marks : 95
Result : PASS
========================================

========================================
 STUDENT REPORT
========================================
College : IIT Bombay
Name : Soham
Roll No : 1335
Marks : 35
Result : FAIL
========================================

'''