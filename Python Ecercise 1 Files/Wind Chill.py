"""WIND-CHILL------------------------------------------------------------------------------------------"""

import math

Temp = True

while (Temp):
        Temp = eval(input("insert Temperature between -58 and 41 : "))
        if(-58 < Temp < 41):
            Temp = False
        else:
            "insert Temperature between -58 and 41 : "

Wind = True

while (Wind):
        Wind = eval(input("insert Wind Speed >= 2mph : "))
        if(Wind >= 2):
            Wind = False
        else:
            "insert Wind Speed > 2mph : "

wci = 35.74 + 0.6215 * Temp - 35.75 * math.pow(Wind, 0.16) + 0.4275 * Temp * math.pow(Wind, 0.16)

print("The wind chill index is %.3f:" % wci)











