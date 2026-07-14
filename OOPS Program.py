# Base Class
class Person:
    def __init__(self, name):
        self.name = name      # Encapsulation

    def display(self):        # Polymorphism
        print("Name:", self.name)


# Derived Class (Inheritance)
class Student(Person):
    def __init__(self, name, roll_no):
        super().__init__(name)
        self.roll_no = roll_no

    def display(self):        # Method Overriding (Polymorphism)
        print("Student Name:", self.name)
        print("Roll No:", self.roll_no)


# Another Derived Class
class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def display(self):
        print("Teacher Name:", self.name)
        print("Subject:", self.subject)


# Main Program
while True:
    print("\n--- OOP Demo ---")
    print("1. Student")
    print("2. Teacher")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        roll = input("Enter roll number: ")
        s = Student(name, roll)   # Object Creation
        s.display()

    elif choice == "2":
        name = input("Enter teacher name: ")
        subject = input("Enter subject: ")
        t = Teacher(name, subject)  # Object Creation
        t.display()

    elif choice == "3":
        print("Thank you!")
        break

    else:
        print("Invalid choice!")