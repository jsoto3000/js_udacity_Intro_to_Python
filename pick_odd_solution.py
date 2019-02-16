import numpy as np

X = np.arange(1,26).reshape(5,5)

Y = X[X % 2 != 0]