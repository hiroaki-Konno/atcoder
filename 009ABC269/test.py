import numpy as np

arr = np.array([1, 5, 2, 6, 3, 4]).reshape((3, 2,))

print(np.amax(arr, axis=0))
# [3 6]
print(np.amax(arr, axis=1))
# [5 6 4]
