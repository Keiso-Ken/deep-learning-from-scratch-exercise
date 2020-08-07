# NAND
import perceptron as perc
def nand_(p,q):
	perc1 = perc.CPerceptron(-1.0,-1.0, 2.0)
	return perc1.Eval(p,q)

# OTHERS

#AND
def and_(p,q):
	val = nand_(p,q)
	return nand_(val, val)

#XP
def xp_(p,q):
	val = nand_(p,q)
	return and_(p,val)

#NXP
def nxp_(p,q):
	val = nand_(p,q)
	return nand_(p,val)

#XP
def xq_(p,q):
	val = nand_(p,q)
	return and_(q,val)

#NXP
def nxq_(p,q):
	val = nand_(p,q)
	return nand_(q,val)

#ATRUE
def atrue_(p,q):
	val1 = and_(p,q)
	val2 = nand_(p,q)
	return nand_(val1,val2)

#AFALSE
def afalse_(p,q):
	val1 = and_(p,q)
	val2 = nand_(p,q)
	return and_(val1,val2)

#ISP
def isp_(p,q):
	val = atrue_(q,q)
	return and_(p,val)

#NOTP
def notp_(p,q):
	val = atrue_(q,q)
	return nand_(p,val)

#ISQ
def isq_(p,q):
	val = atrue_(p,p)
	return and_(q,val)

#NOTQ
def notq_(p,q):
	val = atrue_(p,p)
	return nand_(q,val)

#OR
def or_(p,q):
	val1 = notp_(p,q)
	val2 = notq_(p,q)
	return nand_(val1,val2)

#NOR
def nor_(p,q):
	val1 = notp_(p,q)
	val2 = notq_(p,q)
	return and_(val1,val2)

#XOR
def xor_(p,q):
	val1 = nand_(p,q)
	val2 = or_(p,q)
	return and_(val1,val2)

#NXOR
def nxor_(p,q):
	val1 = nand_(p,q)
	val2 = or_(p,q)
	return nand_(val1,val2)

