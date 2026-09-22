import numpy as np

# Create a one-dimensional array containing numbers from 1 to 10
arr = np.arange(1, 11)

print("Original Array:", arr)

# Slicing operations
print("First 5 elements:", arr[:5])
print("Last 5 elements:", arr[5:])
print("Elements from index 2 to 6:", arr[2:7])
print("Alternate elements:", arr[::2])

# Statistical measures
print("Sum:", np.sum(arr))
print("Mean:", np.mean(arr))
print("Maximum:", np.max(arr))
print("Minimum:", np.min(arr))

# Broadcasting
arr = arr + 5
print("Array after adding 5 using broadcasting:", arr)

arr = arr * 2
print("Array after multiplying by 2 using broadcasting:", arr)



"""
                OUTPUT:

Original Array: [ 1  2  3  4  5  6  7  8  9 10]

First 5 elements: [1 2 3 4 5]
Last 5 elements: [ 6  7  8  9 10]
Elements from index 2 to 6: [3 4 5 6 7]
Alternate elements: [1 3 5 7 9]

Sum: 55
Mean: 5.5
Maximum: 10
Minimum: 1

Array after adding 5 using broadcasting: [ 6  7  8  9 10 11 12 13 14 15]
Array after multiplying by 2 using broadcasting: [12 14 16 18 20 22 24 26 28 30]
"""