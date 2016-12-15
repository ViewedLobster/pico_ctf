import math
import euclidean
import sys

C = (236857987845294655469221, 12418605208975891779391)
n = 928669833265826932708591

b = (C[1] ** 2 - C[0] ** 3) % n

print(b)

def STR(a):
    a = str(a)
    # Yes, this is a little bit silly :-)
    for i in range(0, len(a) - 1, 2):
        print(chr(int(a[i:i+2])))



class ec_point():

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):

        return hex(self.x) + " " + hex(self.y)


p = n
a = 0
g_x = 0x7d29778100c65a1da1783716588dce2b8b4aee8e228f1896
g_y = 0x38a90f22637337334b49dcb66a6dc8f9978aca7648a943b0
q = 0xffffffffffffffffffffffff7a62d031c83f4294f640ec13

G = ec_point(C[0], C[1])


def point_add(point1, point2):

    k1 = (point2.y - point1.y) % p
    k2 = f_inverse((point2.x - point1.x) % p) % p
    
    s = (k1*k2) % p
    x3 = ((s**2) - point1.x - point2.x ) % p


    y3 = (s*(point1.x - x3) - point1.y) % p


    return ec_point(x3, y3)

def point_double(point):

    k1 = (3*point.x**2 + a) % p
    k2 = f_inverse((2*point.y) % p) % p

    s = (k1*k2) % p

    x3 = ((s**2) - 2*point.x) % p
    y3 = (s*(point.x - x3) - point.y) % p

    return ec_point(x3, y3)


def point_mult(point, factor):

    if factor == 1:
        return point

    exp = point
    bitstring = get_int_bit_string(factor)

    for i in range(1, len(bitstring)):
        exp = point_double(exp)

        if bitstring[i] == "1":
            exp = point_add(point, exp)


    return exp


def f_inverse(felem):

    (a, b, r) = euclidean.ext_euclid(p, felem)

    return r


def get_int_bit_string(e):
    # converts e into a binary string
    bitstring = bin(e)

    # returns all characters from 2 and on, the first chars are 0b
    return bitstring[2:]

d = 87441340171043308346177
M = point_mult(G, d)

print(STR(M.x)+STR(M.y))
