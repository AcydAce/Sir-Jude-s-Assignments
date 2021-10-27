def num_atom(amount,weight=196.97):

    avogadro = 6.022 * 10 ** 23
    form = amount * avogadro / weight  # formula

    return form


print("the atomic weight of:\n")
print("gold:",num_atom(10),"\n")
print("carbon:",num_atom(10,12.001),"\n")  # result
print("hydrogen:",num_atom(10,1.008),"\n")