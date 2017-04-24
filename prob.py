#!/usr/bin/env python

class Vec:
    def __init__(self, x,y,z):
        self.x=x
        self.y=y
        self.z=z
        self.n=x**2 + y**2 + z**2 
    def __add__(self, other):
        return Vec(self.x + other.x, self.y + other.y, self.z + other.z)
    def __str__(self):
        return str("(%d,%d,%d)"%(self.x, self.y, self.z))
    def __sub__(self, other):
        return Vec(self.x - other.x, self.y - other.y, self.z - other.z)
    def __mul__(self, lam):
        return Vec(lam*self.x, lam*self.y, lam*self.z)
    
    def n(self):
        return self.n

a1 = Vec(1,1,-1)
a2 = Vec(1,-1,1)
a3 = Vec(-1,1,1)

a = []
for i in range(12):
    a.append([])

for n in range(-7,8):
    for m in range(-7,8):
        for l in range(-7,8):
            tmp = a1 * n + a2 * m + a3 * l
            if tmp.n<12:
                a[tmp.n].append(tmp)

for i in range(12):
    print "%d(%d):" % (i, len(a[i])),
    for j in a[i]:
        print j,
    print " "
