"""Perimeter Of A Triangle-----------------------------------------------------------------------------"""

length1 = float(input("Enter Length 1 : "))
length2 = float(input("Enter Length 2 : "))
length3 = float(input("Enter Length 3 : "))

if float(length1 + length2 > length3):
    if float(length1 + length3 > length2):
        if float(length3 + length2 > length1):
            result = float(length1 + length2 + length3)
            print("the Perimater is: " , float(result))

else: print("the input is invalid")