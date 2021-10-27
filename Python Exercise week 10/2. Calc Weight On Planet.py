def calc_weight_on_planet(weight, grav=23.1):
    base = 9.8
    form = weight / base * grav  # formula
    return form


print(calc_weight_on_planet(120,9.8) , end= "lb\n")

print(calc_weight_on_planet(120,) , end= "lb\n")  # result

print(calc_weight_on_planet(120,23.1) , end= "lb")