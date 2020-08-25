import numpy as np

#explanation
a = np.array([1010, 1000, 990])
exp_a = np.exp(a)
print(exp_a)
c = np.max(a)
print(a-c)
print(np.exp(a-c)/np.sum(np.exp(a-c)))

# softmax function improved
def softmax(a):
    c = np.max(a)             #improved
    exp_a = np.exp(a-c)       #improved
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

