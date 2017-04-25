#!/usr/bin/env python

from numpy import cos,pi


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

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def n(self):
        return self.n

a1 = Vec(1,1,-1)
a2 = Vec(1,-1,1)
a3 = Vec(-1,1,1)

a = []
for i in range(12):
    a.append([])

for n in range(2,-3,-1):
    for m in range(2,-3,-1):
        for l in range(2,-3,-1):
            tmp = a1 * n + a2 * m + a3 * l
            if tmp.n<12:
                a[tmp.n].append(tmp)

# Problem 7 (a)
print "Problem 7 (a)"
print "G2(num):"
for i in range(12):
    print "%d(%d):" % (i, len(a[i])),
    for j in a[i]:
        print j,
    print " "

# Problem 7 (b)
for i in range(3):
    print ""

print "Problem 7 (b)"

print "G2(num):"
for i in range(12):
    print "%d(%d):" % (i, len(a[i])),
    for j in a[i]:
        print cos(pi/4 * (j.dot(Vec(1,1,1)))),
        #print j,
    print " "

for i in range(3):
    print ""
print "0.707106781187 menas sqrt(2)/2"
print "The small number means 0"

# Problem 7 (c)
for i in range(3):
    print ""

s = "{"
for ny in range(1,-2,-1):
    for my in range(1,-2,-1):
        for ly in range(1,-2,-1):
            s += "{"
            for nx in range(1,-2,-1):
                for mx in range(1,-2,-1):
                    for lx in range(1,-2,-1):
                        if (nx == ny) and (mx == my) and (lx == ly):
                            s += "1/2 ((kx + %d)^2 + (ky + %d)^2 + (kz + %d)^2)," % (nx, mx, lx)

                        else:
                            tmp = Vec(nx-ny, mx-my, lx-ly)
                            c = 0 
                            if tmp.n == 3:
                                c = -0.23
                            if tmp.n == 8:
                                c = 0.01
                            if tmp.n == 11:
                                c = 0.06
                            s += "%0.6le," % (c * cos(pi/4 * tmp.dot(Vec(1,1,1))))
            s = s[:-1]
            s += "},"

s = s[:-1] + "}"
print s
