import numpy as np



X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
Y = np.array([1, 1, 1, 2, 2, 2])

A = [0,1,2,3,4,5]
B = [0,1,2,3,4,5]
for a in range(0,5):
     A[a] = X[a][0]
for a in range(0,5):
     B[a] = X[a][1]


import matplotlib.pyplot as plt
plt.plot(X,'bo')
plt.plot([-0.8,-1],'ro')

plt.ylabel('y-label')
plt.show()



