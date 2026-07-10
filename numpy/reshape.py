import numpy as np

numbers = np.array([1, 2, 3, 4, 5, 6])

print(numbers)

print("\nShape:")
print(numbers.shape)

matrix = numbers.reshape(2, 3)

print(matrix)

print("\nShape:")
print(matrix.shape)