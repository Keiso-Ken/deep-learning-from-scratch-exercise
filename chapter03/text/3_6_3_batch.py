import sys, os
sys.path.append(os.pardir)
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image
import pickle

#sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# softmax function improved
def softmax(a):
    c = np.max(a)             #improved
    exp_a = np.exp(a-c)       #improved
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y

def get_data():
    (x_train, t_train), (x_test, t_test) = \
        load_mnist(normalize = True, flatten = True, one_hot_label=False)
    return x_test, t_test

def init_network():
    with open("sample_weight.pkl", 'rb') as f:
        network = pickle.load(f)
    return network

def predict(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']
    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = softmax(a3)
    return y

x, t = get_data()
network = init_network()
W1, W2, W3 = network['W1'],network['W2'],network['W3']
print(x[0].shape)
print(W1.shape)
print(W2.shape)
print(W3.shape)

#batch
batch_size = 100
accuracy_cnt = 0

for i in range(0,len(x),batch_size):
    x_batch = x[i:i+batch_size]
    y_batch = predict(network, x_batch)
    p=np.argmax(y_batch, axis=1)
    accuracy_cnt+= np.sum(p==t[i:i+batch_size])
print("Accuracy:" + str(float(accuracy_cnt)/len(x)))

#explanation 1
print(list(range(0,10)))
print(list(range(0,10,3)))

#explanation 2
x = np.array([[0.1, 0.8, 0.1], [0.3, 0.1, 0.6], [0.2, 0.5, 0.3], [0.8,0.1,0.1]])
y = np.argmax(x,axis=1)
print(y)
for i in range(0,4):
    print (x[i][y[i]])

#explanation 3
y = np.array([1,2,1,0])
t = np.array([1,2,0,0])
print(y==t)
print(np.sum(y==t))
