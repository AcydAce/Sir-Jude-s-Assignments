"""Tip Calculator--------------------------------------------------------------------------------------"""

Total = float(input("Insert Sub Total: $"))
Tip = float(input("Insert Tip: $"))

Tip_Total = float(Total * Tip / 100)
Total_Total = float(Total + Tip_Total)

print("Tip %.2f:" % float(Tip_Total))
print("Total %.2f:" % float(Total_Total))