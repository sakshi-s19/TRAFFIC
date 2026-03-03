import numpy as np

# Original Traffic Matrix
T = np.array([[50, 30],
[20, 40]])

# Signal Matrix
S = np.array([[0.6, 0.2],
[0.3, 0.7]])

# After Cycle 1
T1 = np.dot(T, S)

# After Cycle 2
T2 = np.dot(T1, S)

# Totals
total_original = np.sum(T)
total_cycle1 = np.sum(T1)
total_cycle2 = np.sum(T2)

# Reduction
reduction1 = total_original - total_cycle1
reduction2 = total_original - total_cycle2

print("Original Traffic Matrix:\n", T)
print("\nAfter Cycle 1:\n", T1)
print("\nAfter Cycle 2:\n", T2)

print("\nTotal Before:", total_original)
print("Total After Cycle 1:", total_cycle1)
print("Total After Cycle 2:", total_cycle2)

print("\nReduction After Cycle 1:", reduction1)
print("Reduction After Cycle 2:", reduction2)
