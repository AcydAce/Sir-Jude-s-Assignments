"""Hexagon Area----------------------------------------------------------------------------------------"""

import math

side = float(input("Insert Side Length: "))

hexagonArea = ((3 * math.sqrt(3) * (side * side)) / 2)

print("Area %.3f:" % float(hexagonArea))