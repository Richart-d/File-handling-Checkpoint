import numpy as np

with open("loan.csv", "r") as f:
    data = f.read()

data = np.genfromtxt("loan.csv", delimiter=",", usecols=8, filling_values=0)

## create a 1D array
array = np.array(data)

#calculate the mean of the array
mean = np.mean(array)
print(f"The mean is: {mean}")

median = np.median(array)
print(f"\nThe median is: {median}")

std = np.std(array)
print(f"\nThe std is: {std}")

max = np.max(array)
print(f"\nThe max is: {max}")

min = np.min(array)
print(f"\nThe min is: {min}")

var = np.var(array)
print(f"\nThe Varience is: {var}")