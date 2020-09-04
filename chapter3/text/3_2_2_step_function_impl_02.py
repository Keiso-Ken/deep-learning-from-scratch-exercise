import numpy as np
def step_function(x):
    y = x > 0
    return y.astype(np.int)

#test
x = np.array([-1,-0,0.1,2])
print(step_function(x))

#explanation of detail
x = np.array([-1.0,1.0,2.0])
print(x)
y = x > 0
print(y)
y = y.astype(np.int)
print(y)



