#!/usr/bin/env python

"""
Projekt do predmetu KRY
Zadanie: Elipticke krivky
Autor: Martin Maga (xmagam00)
"""

import sys



Fp = "0xffffffff00000001000000000000000000000000ffffffffffffffffffffffff"
a = "-0x3"
b =  "0x5ac635d8aa3a93e7b3ebbd55769886bc651d06b0cc53b0f63bce3c3e27d2604b"
Bp = [0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296, 0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5]
Pk = [0x52910a011565810be90d03a299cb55851bab33236b7459b21db82b9f5c1874fe, 0xe3d03339f660528d511c2b1865bcdfd105490ffc4c597233dd2b2504ca42a562]

print "Fp"
print int(Fp,16)

print "a"
print int(a,16)

print "b"
print int(b,16)

print "x"
print int("0x6b17d1f2e12c4247f8bce6e563a440f277037d812deb33a0f4a13945d898c296",16)

print "y"
print int("0x4fe342e2fe1a7f9b8ee7eb4a7c0f9e162bce33576b315ececbb6406837bf51f5",16)

sys.exit(0)
