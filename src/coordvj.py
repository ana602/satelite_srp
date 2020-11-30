import math

def pol2car(fi, lmd,r):
    x = r* math.cos(math.radians(fi))*math.cos(math.radians(lmd))
    y = r* math.cos(math.radians(fi))*math.sin(math.radians(lmd))
    z = r* math.sin(math.radians(fi))
    return x, y, z



fi = 13.840000
lmd = -152.250000
r = 6372000.0 + 20200000.0

x, y, z = pol2car (fi, lmd, r)
print(x,y,z)

def car2pol(xKoor, yKoor, zKoor):
        Fi= math.degrees(math.atan2(zKoor,(math.sqrt((xKoor**2)+(yKoor**2)))))
        Lmb= math.degrees(math.atan2(yKoor,xKoor))
        r= math.sqrt((xKoor**2)+(yKoor**2)+(zKoor**2))
        return Fi, Lmb, r

#print(car2pol(x,y,z))