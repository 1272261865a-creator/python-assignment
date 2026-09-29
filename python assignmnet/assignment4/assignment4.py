""" Matrix Addition using Python Lists """ print("--- Matrix Addition using Python Lists ---")

matrix_A = [, , [7, 8, 9] ]

matrix_B = [, , [3, 2, 1] ]

list_result = [, , [0, 0, 0] ]

for i in range(len(matrix_A)): for j in range(len(matrix_A[0])): list_result[i][j] = matrix_A[i][j] + matrix_B[i][j]

for row in list_result: print(row)

""" Matrix Addition using NumPy Arrays """ print("\n--- Matrix Addition using NumPy ---") import numpy as np

array_A = np.array([, , [7, 8, 9] ])

array_B = np.array([, , [3, 2, 1] ])

numpy_result = array_A + array_B

print(numpy_result)
