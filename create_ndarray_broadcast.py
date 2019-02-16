import numpy as np

# Use Broadcasting to create a 4 x 4 ndarray that has its first
# column full of 1s, its second column full of 2s, its third
# column full of 3s, etc.. 

# We create a 4 x 4 ndarray full of ones. 
# X = np.full((4,4), 1)


X = np.ones((4,4))

# We print X
print()
print('X = \n', X)
print()

# We print information about Z
print('X has dimensions:', X.shape)
print('X is an object of type:', type(X))
print('The elements in X are of type:', X.dtype)

Y =  np.arange(1,5)

# We print Y
print()
print('Y = \n', Y)
print()

# We print information about Y
print('Y has dimensions:', Y.shape)
print('Y is an object of type:', type(Y))
print('The elements in Y are of type:', Y.dtype) 



Z = np.ones((4,4)) * np.arange(1,5)

# We print Z
print()
print('Z = \n', Z)
print()

# We print information about Z
print('Z has dimensions:', Z.shape)
print('Z is an object of type:', type(Z))
print('The elements in Z are of type:', Z.dtype)  
