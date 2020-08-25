import numpy as np
def relu(x):
    return np.maximum(0,x)

# test
x = np.array([-1.0, 1.0, 2.0])
print(relu(x))
