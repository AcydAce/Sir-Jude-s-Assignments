def calc_new_height():

    width = int(input("Enter the current width: "))
    height = int(input("Enter the current height: "))  #  user input
    new_width = int(input("Enter the new width: "))
    new_res = height / width * new_width

    return new_res

print("The new height is: ", calc_new_height())  # result