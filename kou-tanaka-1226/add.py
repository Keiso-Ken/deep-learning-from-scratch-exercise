import binarylogicaloperation as blo

# digit 0
def digit0(a,b):
    return blo.xor_(a,b)

# carry from digit 0
def carry0(a,b):
    return blo.and_(a,b)

# digit n > 0
def digitn(a,b,c):
    return blo.xor_(blo.xor_(a,b),c)

# carry from digit n > 0
def carryn(a,b,c):
    return blo.or_(blo.or_(blo.and_(a,b), blo.and_(b,c)), blo.and_(c,a))

# 5 vs 5 binary digits adding
def add55(a,b):
    # needs 6 digits
    c = [0,0,0,0,0,0]
    #cur_digit = 0
    carry = 0
    #digit0
    c[5] = digit0(a[4],b[4])
    carry = carry0(a[4],b[4])
    #digit1
    c[4] = digitn(a[3],b[3],carry)
    carry = carryn(a[3],b[3],carry)
    #digit2
    c[3] = digitn(a[2],b[2],carry)
    carry = carryn(a[2],b[2],carry)
    #digit3
    c[2] = digitn(a[1],b[1],carry)
    carry = carryn(a[1],b[1],carry)
    #digit4
    c[1] = digitn(a[0],b[0],carry)
    carry = carryn(a[0],b[0],carry)
    #digit5
    c[0] = carry

    return c
##