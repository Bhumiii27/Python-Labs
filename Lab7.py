import numpy as np

# a. 
print("a) 3x3 matrix with values from 2 to 10")
matrix = np.arange(2, 11).reshape(3, 3)
print(matrix, "\n")

# b. 
print("b) Reverse an array")
arr = np.array([1, 2, 3, 4, 5])
print("Original:", arr)
print("Reversed:", arr[::-1], "\n")

# c. 
print("c) Common values between two arrays")
arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([4, 5, 6, 7, 8])
print("Array1:", arr1)
print("Array2:", arr2)
print("Common values:", np.intersect1d(arr1, arr2), "\n")

# d. 
print("d) Repeat array elements")
arr = np.array([1, 2, 3])
print("Original:", arr)
print("Repeated:", np.repeat(arr, 2), "\n")

# e. 
print("e) Memory size of NumPy array")
arr = np.arange(10)
print("Array:", arr)
print("Memory size (in bytes):", arr.nbytes, "\n")

# f. 
print("f) Arrays of ones and zeros")
ones = np.ones((2, 3))
zeros = np.zeros((2, 3))
print("Ones:\n", ones)
print("Zeros:\n", zeros, "\n")

# g. 
print("g) 4th element of an array")
arr = np.array([10, 20, 30, 40, 50])
print("Array:", arr)
print("4th element:", arr[3])
