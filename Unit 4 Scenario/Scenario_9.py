import numpy as np
import pandas as pd

# Course names
courses = ["Python", "Data Structures", "AI", "Web Development", "Machine Learning"]

# Course fees using NumPy array
fees = np.array([20000, 28000, 35000, 22000, 40000])

# Calculate average, maximum and minimum fee
average_fee = np.mean(fees)
maximum_fee = np.max(fees)
minimum_fee = np.min(fees)

# Display fee analysis
print("Course Fee Analysis")
print("-------------------")
print("Average Fee :", average_fee)
print("Maximum Fee :", maximum_fee)
print("Minimum Fee :", minimum_fee)

# Create Pandas DataFrame
df = pd.DataFrame({
    "Course": courses,
    "Fee": fees
})

print("\nCourse Details")
print(df)

# Display courses whose fee is greater than ₹25,000
print("\nCourses with Fee Greater than ₹25,000")
print(df[df["Fee"] > 25000])


"""
            OUTPUT

            
Course Fee Analysis
-------------------
Average Fee : 29000.0
Maximum Fee : 40000
Minimum Fee : 20000

Course Details
             Course    Fee
0            Python  20000
1   Data Structures  28000
2                AI  35000
3   Web Development  22000
4  Machine Learning  40000

Courses with Fee Greater than ₹25,000
             Course    Fee
1   Data Structures  28000
2                AI  35000
4  Machine Learning  40000
"""