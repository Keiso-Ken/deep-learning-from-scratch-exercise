# PERCEPTRON
import numpy as np
class CPerceptron:
	def __init__(self, w1, w2, b):
		self.w1 = w1
		self.w2 = w2
		self.b  = b

	def Eval(self, p, q):
		x   = np.array([p, q])
		w   = np.array([self.w1, self.w2])
		val = np.sum(w*x) + self.b
		ret = val > 0.0
		return ret.astype(np.int)

