"""Perimeter Of A Triangle-----------------------------------------------------------------------------"""

length1 = float(input("Enter Edge 1 : "))
length2 = float(input("Enter Edge 2 : "))
length3 = float(input("Enter Edge 3 : "))

if float(length1 + length2 > length3):
    if float(length1 + length3 > length2):
        if float(length3 + length2 > length1):
            result = float(length1 + length2 + length3)
            print("the Perimater is: " , float(result))

else: print("the input is invalid")