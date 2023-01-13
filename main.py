weight = float(input("whats your weight? "))


weight_type = input("(K)g or (l)bs? ")


if weight_type == "k" or weight_type == "K":


    print("Your weight in lbs = ", round(weight * 2.205, 1))


if weight_type == "L" or weight_type == "l":


    print("Your weight in kgs = ", round(weight / 2.205, 1))