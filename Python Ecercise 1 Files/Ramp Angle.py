"""Ramp Angle------------------------------------------------------------------------------------------"""

import math

F = float(input("input force: "))
m = float(input("input mass: "))
g = 9.8

asin = (F / (m * g))
result = math.degrees(asin)

print("angle %.1f:" % float(result))