import numpy as np

# Original Traffic Matrix before signal
T = np.array([[50, 30],
              [60, 40]])
print("where" \
"rows = current direction" 
"coloumn = target direction")

#after Signal optimizattion
S = np.array([[0.6, 0.2],
              [0.3, 0.7]])

# After Cycle 1(signal)
T1 = np.dot(T, S)

# After Cycle 2(signal)
T2 = np.dot(T1, S)

# Totaltrafiic matrix
T_original = np.sum(T)
T_cycle1 = np.sum(T1)
T_cycle2 = np.sum(T2)

# Reduction
reduction1 = T_original - T_cycle1
reduction2 = T_original - T_cycle2

print("Original Traffic Matrix:\n", T)
print(
"rows = current direction\n" 
"coloumn = target direction\n")
print("signal optimization matrix\n" \
"(reduce in flow of vehicle due to red signal)\n", S)
print("\nAfter Cycle 1:\n",T1) 
print("\nAfter Cycle 2:\n", T2)

print("\nTotal Before signal:", T_original)
print("After first signal optimization :", T_cycle1)
print("After second signal optimization :", T_cycle2)

print("\nReduction After Cycle 1:reduction1 = T_original - T_cycle1=", reduction1)
print("Reduction After Cycle 2:reduction2 = T_original - T_cycle2=", reduction2)
