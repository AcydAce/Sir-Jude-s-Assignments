def convert_temp():
    Tf = int(input("Insert Fahrenheit: "))
    Tc = 5 / 9 *(Tf - 32)
    Tk = Tc + 273.15

    print("the temperature in fahrenheit is:", Tf)
    print("the temperature in celsius is:", Tc)
    print("the temperature in Kelvin is:", Tk)

convert_temp()