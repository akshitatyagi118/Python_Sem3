import pandas as pd
import numpy as np

# Create a Series containing 10 random numbers
series = pd.Series(np.random.randint(1, 100, 10))

print("Original Series:")
print(series)

# Indexing
print("\nValue at index 2:")
print(series[2])

# Filtering
print("\nValues greater than 50:")
print(series[series > 50])

# Statistical operations
print("\nMean:", series.mean())
print("Median:", series.median())
print("Minimum:", series.min())
print("Maximum:", series.max())


"""
        OUTPUT

Original Series:
0    45
1    78
2    23
3    91
4    56
5    12
6    67
7    34
8    89
9    40
dtype: int64

Value at index 2:
23

Values greater than 50:
1    78
3    91
4    56
6    67
8    89
dtype: int64

Mean: 53.5
Median: 50.5
Minimum: 12
Maximum: 91
"""