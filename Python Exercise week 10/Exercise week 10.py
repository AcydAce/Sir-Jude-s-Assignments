""" 1
def convert_to_day():

    hour = int(input("Insert Hour:"))
    minute = int(input("Insert minute:"))
    second = int(input("Insert second:"))

    return hour, minute, second


h, m, s, = convert_to_day()

seconds_to_day = s / 86400
minute_to_day = m / 3600
hour_to_day = h / 24

get_day = seconds_to_day + minute_to_day + hour_to_day

print("the number of days is %.4f::" % float(get_day))
"""

"""
def calc_weight_on_planet(weight, grav=23.1):

    base = 9.8
    form = weight / base * grav
    
    return form


print(calc_weight_on_planet(120,9.8) , end= "lb\n")

print(calc_weight_on_planet(120,) , end= "lb\n")

print(calc_weight_on_planet(120,23.1) , end= "lb")
"""

"""
def num_atom(amount,weight=196.97):

    avogadro = 6.022 * 10 ** 23
    form = amount * avogadro / weight

    return form


print("the atomic weight of:\n")
print("gold:",num_atom(10),"\n")
print("carbon:",num_atom(10,12.001),"\n")
print("hydrogen:",num_atom(10,1.008),"\n")
"""

"""
def calc_new_height():

    width = int(input("Enter the current width: "))
    height = int(input("Enter the current height: "))
    new_width = int(input("Enter the new width: "))
    new_res = height / width * new_width

    return new_res

print("The new height is: ", calc_new_height())
"""

def convert_temp():
    Tf = int(input("Insert Fahrenheit: "))
    Tc = 5 / 9 *(Tf - 32)
    Tk = Tc + 273.15

    print("the temperature in fahrenheit is:", Tf)
    print("the temperature in celsius is:", Tc)
    print("the temperature in Kelvin is:", Tk)

convert_temp()