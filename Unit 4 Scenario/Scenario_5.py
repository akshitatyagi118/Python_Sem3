import numpy as np
import pandas as pd

# Consumer names
consumers = ["Akash", "Rahul", "Priya", "Neha", "Rohan"]

# Electricity bills using NumPy array
bills = np.array([2500, 3500, 1800, 4200, 3000])

# Calculate mean, median, maximum and minimum bill
mean_bill = np.mean(bills)
median_bill = np.median(bills)
maximum_bill = np.max(bills)
minimum_bill = np.min(bills)

# Display bill analysis
print("Electricity Bill Analysis")
print("-------------------------")
print("Mean Bill    :", mean_bill)
print("Median Bill  :", median_bill)
print("Maximum Bill :", maximum_bill)
print("Minimum Bill :", minimum_bill)

# Create Pandas DataFrame
df = pd.DataFrame({
    "Consumer": consumers,
    "Bill Amount": bills
})

print("\nElectricity Bill Details")
print(df)

# Display consumers whose bill exceeds ₹3000
print("\nConsumers with Bill Greater than ₹3000")
print(df[df["Bill Amount"] > 3000])

"""
OUTPUT

Electricity Bill Analysis
-------------------------
Mean Bill    : 3000.0
Median Bill  : 3000.0
Maximum Bill : 4200
Minimum Bill : 1800

Electricity Bill Details
  Consumer  Bill Amount
0    Akash         2500
1    Rahul         3500
2    Priya         1800
3     Neha         4200
4    Rohan         3000

Consumers with Bill Greater than ₹3000
  Consumer  Bill Amount
1    Rahul         3500
3     Neha         4200
"""