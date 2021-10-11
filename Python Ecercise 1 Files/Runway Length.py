"""Runway Length---------------------------------------------------------------------------------------"""

v = float(input("Enter speed: "))
a = float(input("Enter acceleration: "))

length = (v * v) / (2 * a)

print('The minimum runway length for this airplane is %.4f' % length)