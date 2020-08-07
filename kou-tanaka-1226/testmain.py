import numpy as np
import binarylogicaloperation as blo
import add as add1


print("########################################")
print("# Get all patterns of binary operation #")
print("########################################")
print(
"P" + "\t" + 
"Q" + "\t" + 
"AND" + "\t" +
"NAND" + "\t" +
"XP" + "\t" +
"NXP" + "\t" +
"XQ" + "\t" +
"NXQ" + "\t" +
"ATRUE" + "\t" +
"AFALSE" + "\t" +
"ISP" + "\t" +
"NOTP" + "\t" +
"ISQ" + "\t" +
"NOTQ" + "\t" +
"OR" + "\t" +
"NOR" + "\t" +
"XOR" + "\t" +
"NXOR"
)
for p in [0,1]:
	for q in [0,1]:
		print(p, end="\t")
		print(q, end="\t")
		print(blo.nand_(p, q), end="\t")
		print(blo.and_(p, q),  end="\t")
		print(blo.xp_(p, q), end="\t")
		print(blo.nxp_(p, q), end="\t")
		print(blo.xq_(p, q), end="\t")
		print(blo.nxq_(p, q), end="\t")
		print(blo.atrue_(p, q), end="\t")
		print(blo.afalse_(p, q), end="\t")
		print(blo.isp_(p, q), end="\t")
		print(blo.notp_(p, q), end="\t")
		print(blo.isq_(p, q), end="\t")
		print(blo.notq_(p, q), end="\t")
		print(blo.or_(p, q), end="\t")
		print(blo.nor_(p, q), end="\t")
		print(blo.xor_(p, q), end="\t")
		print(blo.nxor_(p, q))

print("")
print("########################################")
print("## Calculate 5 vs 5 binary digits sum ##")
print("########################################")

a=[1,1,1,1,1]
b=[1,1,1,1,1]

c = add1.add55(a,b)
a_ = [0] + a
b_ = [0] + b
print(a_)
print("+")
print(b_)
print("=")
print(c)
