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


def calc_weight_on_planet(weight, grav=23.1):
    base = 9.8
    form = weight / base * grav
    return form


print(calc_weight_on_planet(120,9.8) , end= "lb\n")

print(calc_weight_on_planet(120,) , end= "lb\n")

print(calc_weight_on_planet(120,23.1) , end= "lb")