import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(data)

print("\nElement:")
print(data[1,1])

print("\nSecond row:")
print(data[1])

print("\nFirst column:")
print(data[:,0])