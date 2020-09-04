import numpy as np

#2×2 vs 2×2
A = np.array([[1, 2], [3, 4]])
print(A.shape)
B = np.array([[5, 6], [7, 8]])
print(B.shape)
print(np.dot(A,B))

#2×3 vs 3×2
A = np.array([[1,2,3],[4,5,6]])
print(A.shape)
B = np.array([[1,2], [3,4], [5,6]])
print(B.shape)
print(np.dot(A,B))

#Error:2×3 vs 2×2
#A = np.array([[1,2,3],[4,5,6]])
#print(A.shape)
#C = np.array([[1,2], [3,4]])
#print(C.shape)
#print(np.dot(A,C))

#3×2 vs 2×1
A = np.array([[1,2],[3,4],[5,6]])
print(A.shape)
B = np.array([7,8])
print(B.shape)
print(np.dot(A,B))