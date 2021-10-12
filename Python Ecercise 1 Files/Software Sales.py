Package = 99

Quant = int(input("Enter the number of packages purchased : "))

if Quant < 10:
        Disc = 100
if 10 <= Quant <= 19:
        Disc = 10
if 20 <= Quant <= 49:
        Disc = 20
if 50 <= Quant <= 99:
        Disc = 30
if Quant >= 100:
        Disc = 40

Total = Package * Quant
DiscAmount = Total * Disc / 100

if Disc == 100:
    DiscAmount = 0

TotAmount = Total - DiscAmount

print("Discount Amount @", Disc, "% :", DiscAmount)
print("Total Amount %.2f:" % TotAmount)


