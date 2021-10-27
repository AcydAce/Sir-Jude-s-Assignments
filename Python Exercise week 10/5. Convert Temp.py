def convert_temp():
    Tf = int(input("Insert Fahrenheit: "))  # user input
    Tc = 5 / 9 *(Tf - 32)                   # formula for Celcius
    Tk = Tc + 273.15                        # formula for Kelvin

    print("the temperature in fahrenheit is:", Tf)
    print("the temperature in celsius is:", Tc)  # result
    print("the temperature in Kelvin is:", Tk)

convert_temp()