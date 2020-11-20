import math as mt
import numpy as np


x1 = -3766966.35160
y1 = 3211876.65329
z1 = 4008333.98853

xz = 4367564.465
yz = 1249621.409
zz = 4415320.144

x2 = -3524499.75252
y2 = -1049128.14019
z2 = 5194459.89105

x618 = -174282.27677
y618 = 3571333.06337
z618 = 5264196.01230

def cart2sph (x, y,  z):
    xsqPlusysq = x**2 + y**2
    r = mt.sqrt(xsqPlusysq + z**2)
    fi = mt.degrees(mt.atan2(z, mt.sqrt(xsqPlusysq)))
    lam = mt.degrees(mt.atan2(y, x))
    return fi, lam, r

print(cart2sph (xz, yz, zz))

# print(mt.degrees(0.8901665453802591))
# print(mt.degrees(2.4355663202397198))


# FiSt= mt.degrees(mt.atan2(z1,mt.sqrt(x1**2 + y1**2)))#krivo?
# LambdaSt= mt.degrees(mt.atan2(y1,x1))
# rSt= mt.sqrt((x1**2)+(y1**2)+(z1**2))

#print(FiSt, LambdaSt, rSt)



# fi = mt.degrees(mt.atan2(z1, mt.sqrt(x1**2 + y1**2)))
#print(fi)
# a = x1**2#OK
# b = y1**2#OK
# c_zagrada = a+b#OK
# d = mt.sqrt(c_zagrada)#OK
# div= z1/d#OK
# z = mt.atan2(z1, d)
# fi = mt.degrees(z)

# print (a)
# print (b)
# print (c_zagrada)
# print(d)
# print(div)
# print(z)
# print(fi)